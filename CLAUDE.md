# Fichier de règles du projet

Claude lit ce fichier au début de chaque conversation et le suit du début à la fin du projet.
Chaque fois qu'on décide quelque chose de nouveau, on l'ajoute ici (« ajoute ça au fichier de règles »).

## Installation

- Si le dossier `node_modules` n'existe pas, le projet n'est pas encore installé : suivre `INSTALLATION.md` avant toute autre chose.
- Les skills Remotion sont dans `.claude/skills/`. Les utiliser pour tout ce qui touche à Remotion (animation, sons, sous-titres, rendu).

## La personne avec qui tu travailles

- Elle débute et n'est pas développeuse : parle-lui en **français simple**, sans jargon, ou en l'expliquant en une phrase.
- Elle ne lit pas le code. Elle juge ce qu'elle voit et ce qu'elle entend.
- Quand quelque chose échoue, corrige-le toi-même, puis explique en une phrase ce qui s'est passé.
- Avant une commande, dis simplement ce qu'elle va faire.

## Le projet (à remplir)

- **Pour qui :** …
- **Le message :** …
- **Le format :** vertical 1080 × 1920 (TikTok, Reels, statut WhatsApp), sauf indication contraire.
- **La durée :** …
- **L'appel à l'action de la fin :** …

## Le style (à remplir)

- **Couleurs :** fond …, texte …, couleur d'accent … (avec leurs codes, par exemple `#FFD400`).
- **Police :** … (une Google Font, chargée avec `@remotion/google-fonts`).
- **Mouvement :** rebonds amortis (spring) et entrées rapides qui ralentissent (ease-out). Jamais de glissement linéaire.
- **Les mots flous définis :** si on dit « moderne », « dynamique » ou « pro », écrire ici ce que ça veut dire concrètement.

## Les interdits

- Pas d'emojis, pas de look « modèle tout fait ».
- Pas de fondu enchaîné à chaque transition : chaque scène naît de la précédente.
- Pas de texte collé aux bords : garder une marge. En vertical, rien d'important tout en bas ni sur le côté droit (les boutons et la légende de TikTok, Reels et Shorts les cachent) : le texte important reste vers le centre.
- Pas de texte trop petit : il doit se lire sur un téléphone, sans le son.
- Jamais de son, de musique ou de voix inventés ou fabriqués par du code : seulement les fichiers fournis dans `public/`.
- Jamais d'information inventée (prix, chiffres, noms) : demander si elle manque.

## La méthode

1. **Toujours montrer le plan séquence avant d'animer** : les scènes, ce qu'on voit, ce qu'on entend, la durée de chacune. Attendre l'accord.
2. **Scène par scène**, puis assembler. Pas toute la vidéo d'un coup.
3. **Ouvrir l'aperçu** (Remotion Studio) et en donner le lien, pour qu'on voie le résultat à chaque changement.
4. **La première version n'est jamais la dernière.** Après chaque version : faire 4 images de contrôle aux moments clés, les évaluer comme un directeur artistique exigeant (note sur 10), corriger les 3 plus gros problèmes, recommencer jusqu'à 8 sur 10.
5. Les règles qui font « pro » : une accroche forte dans les 2 premières secondes, du nouveau toutes les 2 à 4 secondes, chaque idée écrite à l'écran, les animations calées sur la voix, un effet sonore par événement, une fin sur un appel à l'action clair.

## Les fichiers

- `public/` : les ingrédients (voix, images, sons, musique). Ranger en sous-dossiers si besoin : `public/voix/`, `public/images/`, `public/sons/`. Des noms clairs, sans accents ni espaces.
- `public/rushs/` : les vidéos filmées à monter.
- `src/` : le code des vidéos (c'est Claude qui l'écrit).
- `mes-videos/` : les vidéos finies (MP4). Toujours y ranger les rendus, avec un nom clair (`pub-boutique-v2.mp4`).
- `outils/` : `transcrire.py` (transcrire une voix ou un rush, mot par mot) et `comparer.py` (vérifier que la voix dit bien le script).
- Quand la personne parle du « dossier voix », « images », « sons », « clips » ou « rushs », il s'agit de `public/voix/`, `public/images/`, `public/sons/`, `public/clips/` et `public/rushs/` : Remotion ne lit que ce qui est dans `public/`. Les créer s'ils n'existent pas. Si elle a déposé un fichier ailleurs dans le projet, le déplacer au bon endroit et le lui dire.

## Les modèles réutilisables

- Quand on transforme une vidéo en modèle (« je veux pouvoir changer seulement le prix, la couleur… »), décrire les réglages avec un schéma zod (`npx remotion add zod @remotion/zod-types`, `zColor()` pour les couleurs) et des `defaultProps` écrits directement dans la `<Composition>` : ils apparaissent alors dans le panneau de droite de Remotion Studio, et Studio enregistre tout seul les changements.
- Ranger les morceaux réutilisables (style de sous-titres, bandeau, appel à l'action, mouvements) dans `src/mes-modeles/`, et expliquer où modifier chaque élément.

## La voix off

- La voix se fait dans Google AI Studio (synthèse vocale) à partir d'un texte préparé par Claude : chiffres écrits en toutes lettres.
- Après chaque voix déposée : `python outils/transcrire.py`, puis `python outils/comparer.py` avec le script. La voix peut ajouter, sauter ou répéter des phrases : le signaler, avec le moment exact.
- Caler les animations sur les temps des mots du fichier `.mots.json`, jamais à l'œil.

## Les sons

- Claude ne peut pas entendre : il **mesure** (durée, silence, volume avec `ffmpeg`), coupe le silence du début et met les sons au même volume. L'écoute finale revient à la personne.
- Une musique plus courte que la vidéo : la boucler avec un fondu à chaque jointure.
- Le volume final du MP4 : `ffmpeg -i video.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 video-finale.mp4`.

## Si je travaille depuis mon téléphone

Une session sur téléphone tourne dans le cloud (la variable `CLAUDE_CODE_REMOTE` vaut `true`). Dans ce cas :

- Remotion Studio n'est pas visible : faire **d'abord un brouillon léger** (petite taille, rendu rapide), puis le rendu final quand il plaît.
- Ranger chaque vidéo dans `mes-videos/`, la garder **sous 100 Mo**, puis l'envoyer sur GitHub (commit et push).
- Toujours donner le **lien direct** de téléchargement de la vidéo : `https://github.com/<compte>/<dépôt>/raw/<branche>/mes-videos/<nom>.mp4`.
- Les rushs lourds arrivent par un lien Google Drive : les télécharger dans `public/rushs/` (ils ne sont pas envoyés sur GitHub).
