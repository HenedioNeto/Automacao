from pathlib import Path
from datetime import datetime

raiz_dir = Path('arquivos')

# Renomeando arquivo de acordo com a data
for caminho in raiz_dir.glob('**/*'):
    if caminho.is_file():
        status = caminho.stat()
        segundo_criado = status.st_ctime
        data_criacao = datetime.fromtimestamp(segundo_criado)
        data_criacao = data_criacao.strftime('%d-%m-%Y_%H_%M_%S')
        novo_nome_arquivo = f'{data_criacao}-{caminho.name}'
        novo_caminho_arquivo = caminho.with_name(novo_nome_arquivo)
        caminho.rename(novo_caminho_arquivo)