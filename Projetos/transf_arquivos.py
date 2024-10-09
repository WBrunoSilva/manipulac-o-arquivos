import os 
import tkinter as tk

# Definindo função para processamento de arquivos 
def processar_arquivo(arquivo_origem, arquivo_destino):
    try:
        with open(arquivo_origem, 'r', encoding= 'utf-8') as f_origem:
            conteudo = f_origem.read()
    except FileNotFoundError:
        print(f'Arquivo {arquivo_origem} não encontrado')
        return
    except PermissionError:
        print(f'Você não tem permissão para ler {arquivo_origem}.')
        return
    except Exception as e:
        print(f'Erro inesperado ao ler {arquivo_origem}:{e}.')

    try:
        with open(arquivo_destino, 'w', encoding= 'utf8') as f_destino:
            f.destino.write('Cabeçalho: Conteúdo do Arquivo/n')
            f.destino.write(conteudo)
            print(f'Conteúdo escrito em {arquivo_destino}')
    except PermissionError:
        print(f' Sem permissão para escrever em {arquivo_destino}')
        return
    except Exception as e:
        print(f'Erro inesperado ao escrever em {arquivo_destino}:{e}')

# Definindo função para a transferência do arquivo no WIDGET
def transferencia_arquivo():
    origem = e1.get()
    destino = e2.get()

    if origem and destino:
        resultado = processar_arquivo(origem, destino)
        status_label.config(text = resultado)
    else:
        status_label.config(text= f' Por Favor, insira vaminhos válidos para a origem do destino')


# Criando janela para a aplicação 
janela = tk.Tk()
janela.title(f'Transferência de Arquivos')

# Rótulos e campos de entrada
tk.Label(janela, text= 'Origem').grid(row= 0)
tk.Label(janela, text= ' Destino').grid(row= 1)
e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e1.grid(row= 0, column= 1)
e2.grid(row= 1,column= 1)

# Label para mostrar o status da transferência
status_label = tk.Label(janela, text = '', fg= 'green')
status_label.grid(row= 4, columnspan= 2)

tk.Button(janela, text= 'Sair', command= janela.quit).grid(row= 3, column= 0, sticky= tk.W, pady= 4)
tk.Button(janela, text= 'Transferir Arquivo', command= transferencia_arquivo).grid(row= 3, column= 1, sticky= tk.W, pady= 4)

janela.mainloop()