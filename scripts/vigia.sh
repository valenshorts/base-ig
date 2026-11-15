#!/usr/bin/env bash
# Vigía: se queda despierto y publica cada pieza a su hora, sin depender del cron de GitHub
# (que a veces se saltea corridas durante horas). Antes del límite de 6 h de GitHub,
# lanza una corrida nueva que sigue la cadena. El cron queda solo de respaldo.
set -u
inicio=$(date +%s)
limite=$((inicio + 330 * 60))
fallo=0

guardar() {
  git add queue/*/estado.json 2>/dev/null || true
  git diff --cached --quiet && return
  git commit -qm "Estado de publicación"
  git push -q || { git pull -q --rebase origin main && git push -q; }
}

while true; do
  git pull -q --rebase origin main || true
  espera=$(python scripts/proxima.py)
  [ -z "$espera" ] && espera=7200          # nada pendiente: el contenido de mañana llega a la tarde
  [ "$fallo" = 1 ] && [ "$espera" -lt 1800 ] && espera=1800   # si Instagram falló, reintentar en 30 min
  resto=$((limite - $(date +%s)))
  if [ "$espera" -ge "$resto" ]; then
    [ "$resto" -gt 0 ] && sleep "$resto"
    gh api -X POST "repos/$GITHUB_REPOSITORY/actions/workflows/publicar.yml/dispatches" \
      -f ref=main -F 'inputs[dry_run]=false' && echo "Sigue una corrida nueva."
    exit 0
  fi
  echo "$(TZ=America/Argentina/Buenos_Aires date +%H:%M) próxima revisión en $((espera / 60)) min."
  sleep "$espera"
  git pull -q --rebase origin main || true
  if python scripts/publicar.py; then fallo=0; else fallo=1; fi
  guardar
done
