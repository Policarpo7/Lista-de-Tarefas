import pickle
from tkinter import *

def salvar_tarefas():
    with open('tarefas.pkl', 'wb') as f:
        pickle.dump(tarefas, f)

def carregar_tarefas():
    try:
        with open('tarefas.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def fechar_janela():
    salvar_tarefas()
    janela.quit()
    janela.destroy()

# Criar janela
janela = Tk()
janela.title('Lista de Tarefas')

tarefas = carregar_tarefas()

# Criar widgets
titulo = Label(janela, text='Lista de Tarefas')
titulo.pack()

nova_tarefa_frame = Frame(janela)
nova_tarefa_frame.pack()

nova_tarefa_nome_label = Label(nova_tarefa_frame, text='Nova Tarefa: ')
nova_tarefa_nome_label.pack(side=LEFT)

nova_tarefa_nome = Entry(nova_tarefa_frame)
nova_tarefa_nome.pack(side=LEFT)

nova_tarefa_categoria_label = Label(nova_tarefa_frame, text='Categoria: ')
nova_tarefa_categoria_label.pack(side=LEFT)

nova_tarefa_categoria = Entry(nova_tarefa_frame)
nova_tarefa_categoria.pack(side=LEFT)

incluir_nova_tarefa = Button(janela, text='Incluir Tarefa')

filtro_frame = Frame(janela)
filtro_frame.pack()

filtro_de_categoria_label = Label(filtro_frame, text='Filtrar por Categoria: ')
filtro_de_categoria_label.pack(side=LEFT)

filtro_de_categoria = Entry(filtro_frame)
filtro_de_categoria.pack(side=LEFT)

lista_tarefas = Listbox(janela)
lista_tarefas.pack()

# Função para exibir a lista de tarefas
def exibir_lista_tarefas():
    lista_tarefas.delete(0, END)

    # Filtrar tarefas por categoria, se houver um filtro selecionado
    categoria_filtro = filtro_de_categoria.get()
    tarefas_filtradas = []
    for tarefa in tarefas:
        if categoria_filtro == '' or tarefa['categoria'] == categoria_filtro:
            tarefas_filtradas.append(tarefa)

    # Exibir cada tarefa na lista
    for tarefa in tarefas_filtradas:
        marcado = ''
        if tarefa['concluida']:
            marcado = ' (concluído)'
        lista_tarefas.insert(END, tarefa['nome'] + ' - ' + tarefa['categoria'] + marcado)

# Adicionar nova tarefa
def adicionar_nova_tarefa():
    nome = nova_tarefa_nome.get().strip()
    categoria = nova_tarefa_categoria.get()
    if nome != '':
        tarefas.append({
            'nome': nome,
            'categoria': categoria,
            'concluida': False
        })
        nova_tarefa_nome.delete(0, END)
        nova_tarefa_categoria.delete(0, END)
        exibir_lista_tarefas()

incluir_nova_tarefa.config(command=adicionar_nova_tarefa)
incluir_nova_tarefa.pack()

# Filtrar por categoria
def filtrar_por_categoria(event):
    exibir_lista_tarefas()

filtro_de_categoria.bind('<KeyRelease>', filtrar_por_categoria)

# Remover tarefa
def remover_tarefa():
    tarefa_selecionada = lista_tarefas.curselection()
    if len(tarefa_selecionada) > 0:
        indice = tarefa_selecionada[0]
        del tarefas[indice]
        exibir_lista_tarefas()

remover_tarefa_botao = Button(janela, text='Remover Tarefa', command=remover_tarefa)
remover_tarefa_botao.pack()

def marcar_como_concluida():
    # Obter o índice da tarefa selecionada na lista de tarefas
    indice_selecionado = lista_tarefas.curselection()

    # Marcar a tarefa como concluída na lista de tarefas, se houver uma tarefa selecionada
    if indice_selecionado:
        tarefas[indice_selecionado[0]]['concluida'] = True
        exibir_lista_tarefas()

marcar_como_concluida_botao = Button(janela, text='Marcar como Concluída', command=marcar_como_concluida)
marcar_como_concluida_botao.pack()

sair_botao = Button(janela, text="Sair", command=fechar_janela)
sair_botao.pack()

# Exibir lista de tarefas após carregar do arquivo
exibir_lista_tarefas()

janela.protocol('WM_DELETE_WINDOW', fechar_janela)
# Adicionar créditos do desenvolvedor
desenvolvido_por = Label(janela, text="Desenvolvido por Policarpo", font=("Arial", 8))
desenvolvido_por.place(relx=1.0, rely=1.0, x=-5, y=-5, anchor="se")
janela.mainloop()