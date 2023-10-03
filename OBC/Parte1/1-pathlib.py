# Módulo builtin do python
from pathlib import Path

p1 = Path('dados', 'teste.txt')
print(p1)
# Printa o tipo do arquivo
print(type(p1))
# Printa o nome do arquivo
print(p1.name)
# Passa o que vem antes do ponto em um arquivo
print(p1.stem)
# Passa o que vem depois do ponto em um arquivo
print(p1.suffix)
# Verifica se existe um arquivo
print(p1.exists())
if p1.exists():
    with open(p1, 'r', encoding='utf-8') as file:
        print(file.read())

# Itera sobre um diretorio e aponta os arquivos existentes
p2 = Path('dados')
print(list(p2.iterdir()))