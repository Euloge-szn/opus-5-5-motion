# Opus 5.5 Motion : le projet de départ

Ce dépôt accompagne la formation **Opus 5.5 Motion : motion design et montage avec Claude** (Euloge ia Store).
Il contient tout ce qu'il faut pour fabriquer des vidéos animées avec Claude et Remotion.

> **Claude, si on t'a envoyé ce lien pour tout installer : lis et suis [INSTALLATION.md](INSTALLATION.md).**

## Sur ordinateur

1. Dans l'application Claude, ouvre l'onglet **Code** et choisis ton dossier `Mes vidéos`.
2. Copie le lien de cette page et envoie-le à Claude avec cette phrase :

   > Installe tout ce qu'il faut sur mon ordinateur à partir de ce dépôt : [lien]. Fais tout à ma place, et explique-moi simplement ce que tu fais.

3. Accepte les demandes d'autorisation de Claude. Quand il te dit que c'est terminé, tout est prêt.

## Sur téléphone

1. Touche le bouton vert **Use this template** (« utiliser ce modèle »), puis **Create a new repository**.
2. Nom : `mes-videos`, puis choisis **Private**, et crée le dépôt.
3. Dans l'application Claude, onglet **Code**, choisis ton dépôt `mes-videos`, avec l'accès internet complet (**Full**).

À chaque nouvelle session, le projet s'installe tout seul.

## Ce qu'il y a dedans

| Dossier ou fichier | À quoi il sert |
|---|---|
| `.claude/skills/` | Les skills Remotion : le manuel de savoir-faire de Claude pour les animations |
| `CLAUDE.md` | Ton fichier de règles de départ, à compléter avec ton projet |
| `public/` | Tes ingrédients : voix, images, sons, musique |
| `public/rushs/` | Tes vidéos filmées à monter |
| `mes-videos/` | Les vidéos finies |
| `src/` | Le code des vidéos (c'est Claude qui l'écrit) |
| `outils/` | Transcrire une voix et la comparer au script |

## À savoir

- Remotion est gratuit pour les particuliers et les entreprises de 3 personnes ou moins. Au-delà, une licence entreprise est demandée (voir remotion.pro).
- Les skills de `.claude/skills/` sont ceux publiés par l'équipe Remotion (`remotion-dev/skills`).
