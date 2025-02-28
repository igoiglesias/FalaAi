#!/bin/bash

# Define variáveis
PROJETO_DIR="/home/ubuntu/FalaAi"
VENV_DIR="$PROJETO_DIR/.venv"
USER="www-data"

# Navega até o diretório do projeto
cd "$PROJETO_DIR" || exit

# Atualiza o repositório com o último código
sudo -u "$USER" git checkout .
sudo -u "$USER" git restore --staged --worktree .
sudo -u "$USER" git pull origin main

# Ativa o ambiente virtual e reinstala dependências
sudo -u "$USER" bash -c "source $VENV_DIR/bin/activate && pip install --no-cache-dir -r requirements.txt"

# Reinicia o serviço falaai.service
sudo systemctl restart falaai.service

echo "Atualização concluída, dependências reinstaladas e serviço reiniciado."



