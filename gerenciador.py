import os
import pandas as pd

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

file_path = 'C:\\Users\\betof\\OneDrive\\Documentos\\Relação bkps\\bkps.xlsx'
extrair_dados = pd.read_excel(file_path)
dados = extrair_dados.to_dict(orient='records')

def calcular_espaco_livre(dados):
    for colaborador in dados:
        espaço_total = colaborador['tamanho do hd']
        espaço_usado = colaborador['tamanho do backup']
        colaborador['espaço livre'] = espaço_total - espaço_usado

def mostrar_hds_com_espaco_livre(dados):
    calcular_espaco_livre(dados)  
    hds_exibidos = set()  
    for colaborador in dados:
        nome_hd = colaborador['nome do hd']
        if nome_hd not in hds_exibidos:
            espaço_total = colaborador['tamanho do hd']
            espaço_usado = colaborador['tamanho do backup']
            espaço_livre = colaborador['espaço livre']
            percentual_usado = (espaço_usado / espaço_total) * 100
            barras_uso = '=' * int(percentual_usado // 10)
            print(f'{nome_hd} [{barras_uso}] {percentual_usado:.0f}% em uso ({espaço_livre:.2f} GB livre)')
            hds_exibidos.add(nome_hd)

def procurar_backup(dados, nome):
    nome = nome.upper()
    hds = []
    colaboradores_encontrados = []
    for colaborador in dados:
        nome_completo = colaborador['nome do colaborador']
        nome_partes = nome_completo.split()

        if nome_completo == nome or (nome_partes and nome_partes[0] == nome):
            hds.append(colaborador['nome do hd'])
            colaboradores_encontrados.append(colaborador['nome do colaborador'])

    if hds:
        return hds, colaboradores_encontrados
    else:
        return None

while True:
    clear_screen()
    print('Gerenciador de Backups')
    try:
        decisao = input('(1) Procurar BKP\n(2) Adicionar BKP\n(3) Buscar HDs com espaço livre\n(4) Sair\nEscolha uma opção: ')
        
        if decisao == '1':
            clear_screen()
            nome = input('Digite o nome do usuário: ')
            hd = procurar_backup(dados, nome)
            if hd:
                print(f'O BKP de {nome} está no HD {hd}!')
            else:
                print('O BKP não foi encontrado!')
            input('Pressione Enter para continuar...')
        
        elif decisao == '2':
            clear_screen()
            novo_nome = input('Digite o nome do colaborador: ').upper()
            escolha_hd = input('Digite o número do HD: ')
            tamanho_bkp = int(input('Digite o tamanho do BKP: '))
            tamanho_do_hd = int(input('Digite o tamanho total do HD em GB: '))
            novo_registro = {'nome do hd': escolha_hd, 'nome do colaborador': novo_nome, 'tamanho do backup': tamanho_bkp, 'tamanho do hd': tamanho_do_hd}
            dados.append(novo_registro)
            
            novo_dataframe = pd.DataFrame(dados)
            novo_dataframe.to_excel(file_path, index=False)
            print('Novo BKP cadastrado com sucesso!')
        
            extrair_dados = pd.read_excel(file_path)
            dados = extrair_dados.to_dict(orient='records')
            input('Pressione Enter para continuar...')
        
        elif decisao == '3':
            clear_screen()
            mostrar_hds_com_espaco_livre(dados)
            input('Pressione Enter para continuar...')
        
        elif decisao == '4':
            clear_screen()
            print('Saindo do programa...')
            break
        
        else:
            clear_screen()
            print('Opção inválida! Por favor, escolha uma opção válida.')
            input('Pressione Enter para continuar...')
    
    except ValueError:
        clear_screen()
        print('Erro: Entrada inválida! Por favor, digite o valor correto.')
        input('Pressione Enter para continuar...')
    except FileNotFoundError:
        clear_screen()
        print(f'Erro: Arquivo não encontrado em {file_path}. Verifique o caminho e tente novamente.')
        input('Pressione Enter para continuar...')
    except Exception as e:
        clear_screen()
        print(f'Ocorreu um erro: {e}')
        input('Pressione Enter para continuar...')
