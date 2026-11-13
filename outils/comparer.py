"""Compare la transcription d'une voix au texte du script.
Usage : python outils/comparer.py script.txt public/voix.mots.json
Affiche les passages sautés ou ajoutés (3 mots ou plus), avec le moment dans la voix.
"""
import sys, json, re, unicodedata, difflib

sys.stdout.reconfigure(encoding="utf-8")  # accents lisibles dans le terminal Windows


def net(x):
    x = ''.join(c for c in unicodedata.normalize('NFD', x.lower()) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]', '', x)


texte = open(sys.argv[1], encoding='utf-8').read()
script = [net(w) for w in re.split(r"[\s'’-]+", texte) if net(w)]
mots = json.load(open(sys.argv[2], encoding='utf-8'))
voix, temps = [], []
for m in mots:
    for w in re.split(r"[\s'’-]+", m['mot']):
        if net(w):
            voix.append(net(w))
            temps.append(m['debut'])

sm = difflib.SequenceMatcher(None, script, voix, autojunk=False)
print(f'ressemblance {sm.ratio():.3f}')
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op == 'equal':
        continue
    if max(a1 - a0, b1 - b0) >= 3:
        t = temps[min(b0, len(temps) - 1)] if temps else 0
        print(f'{op} @ {t:.1f} s | script: {" ".join(script[a0:a1])[:120]} | voix: {" ".join(voix[b0:b1])[:120]}')
print(f'fin du script dans la voix : {mots[-1]["fin"]:.1f} s')
