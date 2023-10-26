#!/bin/bash

# Verifica se o ambiente virtual já existe e exclui se existir
if [ -d "django_venv" ]; then
    echo "Excluindo ambiente virtual existente..."
    rm -rf django_venv
fi

# Cria um ambiente virtual com Python 3 chamado django_venv
echo "Criando ambiente virtual django_venv..."
python3 -m venv django_venv

# Ativa o ambiente virtual
source django_venv/bin/activate

# Instala as dependências do arquivo requirement.txt no ambiente virtual
echo "Instalando as dependências do Django e psycopg2..."
pip install -r requirement.txt

echo "Ambiente virtual django_venv ativado."