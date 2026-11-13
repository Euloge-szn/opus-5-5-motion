#!/usr/bin/env bash
# Installation automatique au début de chaque session sur téléphone (session cloud de Claude Code).
# Sur ordinateur, ce script ne fait rien : l'installation se fait une fois, avec INSTALLATION.md.

if [ "$CLAUDE_CODE_REMOTE" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
echo "Préparation du projet pour la session sur téléphone..."

# Remotion et ses modules
if [ ! -d node_modules ]; then
  npm install --no-audit --no-fund --loglevel=error || echo "ATTENTION : npm install a échoué. Relance-le avant de travailler."
fi

# Le navigateur dont Remotion a besoin pour fabriquer les vidéos
npx --no-install remotion browser ensure >/dev/null 2>&1 || echo "ATTENTION : le navigateur de Remotion n'est pas prêt (npx remotion browser ensure)."

# ffmpeg : mesurer et couper les sons et les vidéos
if ! command -v ffmpeg >/dev/null 2>&1; then
  (sudo -n apt-get update -qq && sudo -n apt-get install -y -qq ffmpeg) >/dev/null 2>&1 \
    || (apt-get update -qq && apt-get install -y -qq ffmpeg) >/dev/null 2>&1 \
    || echo "ATTENTION : ffmpeg n'a pas pu être installé."
fi

# faster-whisper : transcrire les voix (outils/transcrire.py)
if ! python3 -c "import faster_whisper" >/dev/null 2>&1; then
  python3 -m pip install -q faster-whisper >/dev/null 2>&1 \
    || python3 -m pip install -q --break-system-packages faster-whisper >/dev/null 2>&1 \
    || echo "ATTENTION : faster-whisper n'a pas pu être installé."
fi

echo "Préparation terminée (voir les ATTENTION éventuelles ci-dessus). Règles téléphone : voir CLAUDE.md."
exit 0
