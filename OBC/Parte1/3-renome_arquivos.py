from pathlib import Path

# Pega a raiz dos arquivos
raiz_dir = Path('arquivos')
# Engloba na variavel todas as iterações a partir da pasta raiz
caminhos_arquivo = raiz_dir.glob('**/*')

for caminho in caminhos_arquivo:
    # Se for um arquivo...
    if caminho.is_file():
        # Converte os itens em forma de tupla (pasta, subpasta e arquivo)
        print(caminho.parts)
        # Pega apenas as subpastas
        print(caminho.parts[-2])
        # seleciona a subpasta no indice[-2]
        pasta_pai = caminho.parts[-2]
        novo_arquivo = f'{pasta_pai}-{caminho.name}'
        novo_caminho_arquivo = caminho.with_name(novo_arquivo)
        caminho.rename(novo_caminho_arquivo)