#!/bin/bash
source .venv/bin/activate
export UVICORN_HTTP2=true
export UVICORN_RELOAD=true

# celery -A app.celery.celery worker --loglevel=info &
# CELERY_PID=$!

# wait_for_celery() {
#     echo "Aguardando o Celery iniciar..."
#     while ! ps -p $CELERY_PID > /dev/null; do
#         sleep 1
#     done
#     echo "Celery está em execução. Continuando com o Gunicorn."
# }

# wait_for_celery

gunicorn app.main:app \
    -w $(($(nproc) - 1)) \
    -k uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --reload \
    --keep-alive 120 \
    --timeout 120 \
    --preload \
    --log-level info \
    --forwarded-allow-ips '*' \
    --graceful-timeout 30 \
    --error-logfile error.log &
GUNICORN_PID=$!

cleanup() {
    echo "Terminando processos..."
    # kill $CELERY_PID 
    kill $GUNICORN_PID
    exit 0
}

trap cleanup SIGINT
# wait $CELERY_PID 
wait $GUNICORN_PID
echo "Tudo limpo"