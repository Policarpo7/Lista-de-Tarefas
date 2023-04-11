**Lista de Tarefas com Tkinter e Pickle**

Este código é um aplicativo simples de lista de tarefas desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica e a biblioteca Pickle para salvar e carregar as tarefas em um arquivo.

**Funcionalidades**

**O aplicativo permite ao usuário:**

    Adicionar tarefas com nome e categoria.
    Filtrar tarefas por categoria.
    Remover tarefas.
    Marcar tarefas como concluídas.
    Salvar e carregar tarefas em um arquivo.

**Explicação do código**
**Importação de módulos**

Os módulos pickle e tkinter são importados para manipular a serialização de dados e a criação da interface gráfica, respectivamente.

**Funções**

    salvar_tarefas(): Salva a lista de tarefas em um arquivo chamado tarefas.pkl usando a biblioteca pickle.
    carregar_tarefas(): Carrega a lista de tarefas do arquivo tarefas.pkl se existir, senão retorna uma lista vazia.
    fechar_janela(): Salva as tarefas, fecha a janela e encerra o aplicativo.
    exibir_lista_tarefas(): Exibe as tarefas na interface gráfica, com a possibilidade de filtrá-las por categoria.
    adicionar_nova_tarefa(): Adiciona uma nova tarefa à lista de tarefas e atualiza a visualização na interface gráfica.
    filtrar_por_categoria(event): Filtra as tarefas por categoria e atualiza a visualização na interface gráfica.
    remover_tarefa(): Remove uma tarefa selecionada da lista de tarefas e atualiza a visualização na interface gráfica.
    marcar_como_concluida(): Marca uma tarefa selecionada como concluída e atualiza a visualização na interface gráfica.

**Interface gráfica (Tkinter)**

A interface gráfica é construída usando a biblioteca Tkinter e é composta pelos seguintes elementos:

    Título da aplicação.
    Campos de entrada para nome e categoria de uma nova tarefa.
    Botão para incluir uma nova tarefa.
    Campos de entrada para filtrar as tarefas por categoria.
    Lista de tarefas exibida na tela.
    Botões para remover tarefa, marcar como concluída e sair do aplicativo.
    Créditos do desenvolvedor.

**Fluxo do aplicativo**

    A lista de tarefas é carregada do arquivo tarefas.pkl (ou uma lista vazia, se o arquivo não existir).
    A interface gráfica é construída e exibida na tela.
    O usuário pode interagir com a aplicação através das funcionalidades oferecidas.
    Quando o usuário fecha a janela ou clica no botão "Sair", as tarefas são salvas no arquivo e o aplicativo é encerrado.
