import os

def processar_arquivo(arquivo_antigo, arquivo_novo):
        try:
            with open(arquivo_antigo, 'r', encoding= 'utf-8') as f_antigo:
                  conteudo = f_antigo.read()
        except FileNotFoundError:
              print(f'Arquivo {arquivo_antigo} não encontrado')
              return
        except PermissionError:
              print(f'Você não tem permissão para ler {arquivo_antigo}.')
              return
        except Exception as e:
              print(f'Erro inesperado ao ler {arquivo_antigo}:{e}')
              return
        try:
              with open(arquivo_novo, 'w', encoding= 'utf-8') as f_novo:
                    f_novo.write('Cabeçalho: Conteúdo do Arquivo\n')
                    f_novo.write(conteudo)
                    print(f'Conteúdo escrito em {arquivo_novo}')
        except PermissionError:
              print(f'Sem permissão para escrever em {arquivo_novo}')
        except Exception as e:
              print(f'Erro inesperado ao escrever em {arquivo_novo}: {e}')
            
def main():
      diretorio_trabalho = 'diretorio_trabalho'
      arquivo_antigo = os.path.join(diretorio_trabalho, 'arquivo_antigo.txt')
      arquivo_novo = os.path.join(diretorio_trabalho, 'arquivo_novo.txt')

      processar_arquivo(arquivo_antigo, arquivo_novo)

if __name__ == '__main__':
      main()