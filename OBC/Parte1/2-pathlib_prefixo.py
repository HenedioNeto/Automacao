from pathlib import Path

raiz_dir = Path('dados')
caminho_do_arquivo = raiz_dir.iterdir()
#print(list(caminho_do_arquivo))

for caminho in caminho_do_arquivo:
    # Renome que sera dado ao arquivo
    novo_arquivo = f'novo-{caminho.stem}{caminho.suffix}'
    #print(novo_arquivo)
    # Pega o nome do arquivo e a pasta pai
    novo_caminho_arquivo = caminho.with_name(novo_arquivo)
    # Renomeia o arquivo com o nome do novo_arquivo
    caminho.rename(novo_caminho_arquivo)