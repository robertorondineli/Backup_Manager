# Backup_Manager
 Gerenciador de Backups

# Descrição
Este script é um gerenciador de backups que permite aos usuários procurar backups, adicionar novos backups e verificar HDs com espaço livre. Ele usa a biblioteca pandas para manipular dados armazenados em um arquivo Excel. O script também inclui uma interface de linha de comando simples para interação com o usuário.

# Funcionalidades
Procurar Backup (BKP)

Adicionar Backup (BKP)

Buscar HDs com Espaço Livre

Sair

# Requisitos
Python 3.6 ou superior

Bibliotecas Python: pandas, os

Arquivo Excel contendo dados dos backups

Estrutura do Arquivo Excel

# O arquivo Excel deve conter as seguintes colunas:

nome do hd: Nome do HD onde o backup está armazenado

nome do colaborador: Nome do colaborador associado ao backup

tamanho do backup: Tamanho do backup em GB

tamanho do hd: Tamanho total do HD em GB

# Instale as dependências necessárias:

pip install pandas

pip install pyinstaller


# Transformar em Executável (.exe)

No terminal ou prompt de comando, navegue até o diretório onde está salvo o arquivo gerenciador_backups.py e execute o comando:

pyinstaller --onefile gerenciador_backups.py

Isso criará um executável na pasta dist.

# Executar o Arquivo .exe

Navegue até a pasta dist e execute o arquivo gerenciador_backups.exe. A partir daqui, você poderá interagir com o programa conforme descrito nas opções.

# Considerações Finais

Ainda estou desenvolvendo uma GUI.
Esta documentação deve fornecer uma visão clara sobre como usar e transformar o script Python em um executável para gerenciamento de backups.
