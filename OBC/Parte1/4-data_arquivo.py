from pathlib import Path
from datetime import datetime 

caminho = Path('arquivos', 'dados', 'dados-novo-teste.txt')
#print(caminho.stat())

# Stat gera um metadado informando o momento de criação do arquivo
status = caminho.stat()
# Do metadado gerado acima, pega as informações do horario e dia criado
segundo_criacao = status.st_ctime
# Formata o metadado acima pegando apenas a data e horario da criação
data_criacao = datetime.fromtimestamp(segundo_criacao)
data_criacao = data_criacao.strftime('%d-%m-%Y_%H_%M_%S')
print(data_criacao) 