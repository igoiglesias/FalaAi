#!/bin/bash

# Verifica se o virtualenv está instalado, se não, instala
if ! command -v virtualenv &> /dev/null
then
    echo "virtualenv não encontrado. Instalando..."
    sudo apt-get install -y python3-virtualenv
fi

# Cria o ambiente virtual se não existir
if [ ! -d ".venv" ]; then
    echo "Criando o ambiente virtual..."
    virtualenv .venv
fi

# Ativa o ambiente virtual
source .venv/bin/activate

# Instala as dependências do requirements.txt
pip install -r requirements.txt
