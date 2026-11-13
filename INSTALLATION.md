# Installation (instructions pour Claude)

La personne qui t'envoie ce dépôt suit la formation **Opus 5.5 Motion**. Elle débute, elle n'a installé que l'application Claude, et elle t'a écrit à peu près : « Installe tout ce qu'il faut sur mon ordinateur à partir de ce dépôt. Fais tout à ma place, et explique-moi simplement ce que tu fais. »

Ton travail : tout installer à sa place, sans jamais l'envoyer sur un site pour installer un outil elle-même. À chaque étape, dis en une phrase simple ce que tu fais et pourquoi. Elle va accepter tes demandes d'autorisation : préviens-la qu'elles vont arriver et que c'est normal.

Si une étape échoue, cherche la cause et corrige-la toi-même. Ne passe à la suite que quand l'étape marche.

## 1. Regarder où on est

- Le dossier ouvert est son dossier de travail (souvent `Mes vidéos` sur le bureau). C'est **là** qu'on installe le projet, pas ailleurs.
- Repère le système : Windows ou macOS.
- **Vérifie la place libre sur le disque.** Il faut au moins 5 Go (les outils prennent environ 2 Go, les vidéos ensuite). S'il en manque, dis-le simplement et propose de faire de la place avant de continuer.

## 2. Copier le projet dans son dossier

- Si le dossier est vide, copie tout le contenu de ce dépôt **directement dedans** (pas dans un sous-dossier), y compris les dossiers cachés `.claude` et le fichier `.gitignore`.
- Avec Git : `git clone --depth 1 <lien du dépôt> .` (dossier vide), sinon cloner dans un dossier temporaire et copier le contenu.
- Sans Git : télécharger l'archive `<lien du dépôt>/archive/refs/heads/main.zip`, la décompresser, et copier le contenu.
- Si le dossier contient déjà des fichiers à elle, ne les écrase pas : demande-lui avant.
- Supprime le dossier `.git` copié : ce projet devient le sien.

## 3. Installer les outils qui manquent

Vérifie d'abord ce qui est déjà là (`node -v`, `ffmpeg -version`, `python --version`). N'installe que ce qui manque.

| Outil | À quoi il sert | Windows | macOS |
|---|---|---|---|
| **Node.js** (version 22 ou plus) | Faire tourner Remotion | `winget install -e --id OpenJS.NodeJS.LTS` | `brew install node` |
| **ffmpeg** | Mesurer et couper les sons et les vidéos | `winget install -e --id Gyan.FFmpeg` | `brew install ffmpeg` |
| **Python** (3.10 ou plus) | Transcrire les voix | `winget install -e --id Python.Python.3.12` | `brew install python` |

- Sur macOS sans Homebrew : l'installer d'abord (commande officielle de brew.sh). Il demandera le mot de passe de l'ordinateur : c'est elle qui le tape, jamais toi.
- Après une installation avec `winget`, la commande n'est souvent pas encore reconnue dans le même terminal : relis le `PATH` depuis le registre, ou utilise le chemin complet de l'outil.

## 4. Installer le projet

Depuis son dossier :

```bash
npm install
npx remotion browser ensure
python -m pip install faster-whisper
```

- `npm install` installe Remotion et ses modules (environ 1 à 3 minutes).
- `npx remotion browser ensure` télécharge le navigateur dont Remotion a besoin pour fabriquer les vidéos.
- `faster-whisper` sert à transcrire les voix (`outils/transcrire.py`). Le modèle de transcription (environ 500 Mo) se télécharge à la première utilisation.

## 5. Les skills Remotion

Ils sont déjà dans `.claude/skills/` : ce sont les fiches de savoir-faire officielles de Remotion (source : `remotion-dev/skills`). Rien à installer.
Explique-lui en une phrase : un skill, c'est le manuel qu'on donne à un nouvel employé très intelligent, pour qu'il travaille mieux.

## 6. Vérifier que tout marche

```bash
npx remotion still src/index.ts MaVideo out/test.png --frame=0
```

- Si l'image `out/test.png` est créée, tout est prêt. Supprime-la ensuite.
- Ne lance pas Remotion Studio maintenant : ce sera la prochaine étape de la formation.

## 7. Conclure

Dis-lui, en quelques lignes simples :

- ce qui a été installé et à quoi ça sert (Node.js, Remotion, ffmpeg, Python, les skills) ;
- où sont les choses : `public/` pour ses voix, images et sons, `mes-videos/` pour les vidéos finies, `CLAUDE.md` pour le fichier de règles ;
- que le projet contient une première vidéo vide, `MaVideo`, et que c'est normal ;
- que si les skills n'apparaissent pas tout de suite, il suffit d'ouvrir une nouvelle conversation dans ce même dossier.
