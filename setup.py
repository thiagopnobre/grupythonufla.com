# -*- coding:utf-8 -*-

import argparse
from os import system

# instala dependências
def install_requirements():
    system("sudo pip install -r requirements.txt")

# atualiza dependências
def upgrade_requirements():
    system("sudo pip install -r requirements.txt --upgrade")

# adição de argumentos para interface do terminal
parser = argparse.ArgumentParser(prog='setup_project.py', description='Automatização do projeto importando configurações e dependências')
parser.add_argument('-r', help='instalar dependências', action="store_true")
parser.add_argument('-upgrade', help='atualizar dependências', action="store_true")

# parse args
args = parser.parse_args()

# Verifica argumentos
if args.r:
    install_requirements()

if args.upgrade:
    upgrade_requirements()
