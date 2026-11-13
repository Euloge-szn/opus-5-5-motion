"""Transcrit une voix off (ou un rush) mot par mot, avec le moment de chaque mot.

Usage : python outils/transcrire.py public/voix.wav public/voix.mots.json [langue]

- Écrit un fichier .mots.json : [{"mot", "debut", "fin"}, ...] (en secondes).
- Affiche chaque phrase avec son débit (mots par seconde) et signale (!!) les phrases
  à réécouter : dernier mot mal reconnu ou nettement plus faible, phrase qui ralentit.
- Accepte WAV, MP3, M4A, MP4… (le son est lu par ffmpeg). Langue par défaut : fr.

Ensuite, pour vérifier que la voix dit bien le script :
python outils/comparer.py script.txt public/voix.mots.json
"""
import json
import subprocess
import sys

import numpy as np
from faster_whisper import WhisperModel

sys.stdout.reconfigure(encoding="utf-8")  # accents lisibles dans le terminal Windows

src, dst = sys.argv[1], sys.argv[2]
langue = sys.argv[3] if len(sys.argv) > 3 else "fr"
SR = 16000

pcm = subprocess.run(
    ["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
    capture_output=True, check=True,
).stdout
son = np.frombuffer(pcm, dtype=np.float32)

# Modèle « small » : bon compromis précision / vitesse. Pas d'initial_prompt (il fait inventer du texte).
model = WhisperModel("small", device="cpu", compute_type="int8")
segs, _ = model.transcribe(son, language=langue, word_timestamps=True, beam_size=5)
mots = [w for s in segs for w in s.words]

with open(dst, "w", encoding="utf-8") as f:
    json.dump([{"mot": w.word.strip(), "debut": round(w.start, 2), "fin": round(w.end, 2)} for w in mots],
              f, ensure_ascii=False, indent=0)


def volume_db(t0, t1):
    x = son[int(t0 * SR):max(int(t1 * SR), int(t0 * SR) + 1)]
    return 20 * np.log10(np.sqrt(np.mean(x.astype(np.float64) ** 2)) + 1e-9)


print(f"Durée {len(son) / SR:.1f} s, {len(mots)} mots -> {dst}")
phrase, alertes = [], 0
for i, w in enumerate(mots):
    phrase.append(w)
    if w.word.strip()[-1:] in ".?!" or i == len(mots) - 1:
        der = phrase[-1]
        duree = der.end - phrase[0].start
        debit = len(phrase) / duree if duree > 0 else 0
        ecart = volume_db(der.start, der.end) - volume_db(phrase[0].start, der.end)
        alerte = der.probability < 0.6 or ecart < -6 or (duree > 1.5 and debit < 2.6)
        alertes += alerte
        texte = " ".join(x.word.strip() for x in phrase)
        print(f"{'!!' if alerte else '  '} {phrase[0].start:6.1f}s  {debit:4.1f} mots/s  "
              f"dernier mot {ecart:+5.1f} dB  {texte[-80:]}")
        phrase = []
print(f"Phrases à réécouter : {alertes}")
