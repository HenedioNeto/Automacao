"""
Organizador de arquivos

Organizar os arquivos de acordo com seu sufixo

(exe, csv, jpg, pdf, zip)
"""
import os
from pathlib import Path 

# Diretório raiz do SO
caminho_base = os.path.expanduser('~')

# Navegar para o diretório Download
caminho = os.path.join(caminho_base, 'Downloads')
diretorio_trabalho = os.chdir(caminho)

# Listar arquivos do diretório
lista_arquivos = os.listdir(diretorio_trabalho)

# Criar pastas
lista_tipo = ['exe', 'csv', 'jpg', 'pdf', 'zip', 'txt', 'xlsx']
for tipo in lista_tipo:
    if tipo not in os.listdir():
        os.mkdir(tipo)

# Organizando arquivos
for arquivo in lista_arquivos:
    for tipo in lista_tipo:
        if '.' +tipo in arquivo:
            caminho_antigo = os.path.join(caminho, arquivo)
            caminho_novo = os.path.join(caminho, tipo, arquivo)
            os.replace(caminho_antigo, caminho_novo)