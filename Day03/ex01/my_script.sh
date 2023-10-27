#!/bin/bash

pip --version

if [ -d "local_lib" ]; then
  rm -rf local_lib
fi

mkdir local_lib
chmod +x local_lib

pip install git+https://github.com/jaraco/path.git --target=./local_lib > path_install.log

if [ -d "local_lib/path" ]; then
  python3 my_program.py
else
  echo "Falha na instalação do path.py. Verifique o arquivo path_install.log para detalhes."
fi
