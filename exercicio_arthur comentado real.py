# Criando o layout
import PySimpleGUI as sg

# Lista para armazenar as tarefas
tarefas = []  # Cria uma lista vazia chamada "tarefas" para armazenar as tarefas do aplicativo

# Função para adicionar uma tarefa à lista


def adicionar_tarefa(texto):
    tarefas.append({'concluida': False, 'texto': texto})
    # Adiciona uma tarefa à lista "tarefas" como um dicionário com duas chaves: 'concluida' (inicializada como False) e 'texto'.

def listar_tarefas():
    return [f"{'[x]' if tarefa['concluida'] else '[ ]'} {tarefa['texto']}" for tarefa in tarefas]
    # Retorna uma lista de strings representando as tarefas, com '[x]' se a tarefa estiver concluída e '[ ]' se não estiver.

def remover_tarefa(tarefa):
    tarefa = tarefa[4:]  # Remove o "[x] " ou "[ ] " do início da string
    for t in tarefas:
        if t['texto'] == tarefa:
            tarefas.remove(t)
            break
    # Remove uma tarefa da lista "tarefas" com base no texto fornecido, após remover os primeiros 4 caracteres que representam o status.

def marcar_como_concluida(tarefa):
    tarefa = tarefa[4:]  # Remove o "[x] " ou "[ ] " do início da string
    for t in tarefas:
        if t['texto'] == tarefa:
            t['concluida'] = not t['concluida']
            break
    # Marca uma tarefa como concluída ou não, com base no texto fornecido, após remover os primeiros 4 caracteres que representam o status.

    # Função para remover uma tarefa da lista

def criar_janela_inicial():
    sg.theme('LightBlue')

   # Define a estrutura da interface gráfica da janela
    layout = [
        [sg.Frame('Tarefas', layout=[], key='container')],
        [sg.InputText("", key="tarefa"), sg.Button('Adicionar Tarefa')],
        [sg.Listbox(values=[], size=(40, 10), key='tarefas'), sg.Button(
            'Remover Tarefa'), sg.Button('Marcar como Concluída')],
        [sg.Button('Resetar')]
    ]

    return sg.Window('EXERCICIO ARTHUR', layout=layout, finalize=True)


# Criando a janela
janela = criar_janela_inicial()

# Função para marcar uma tarefa como concluída







# Criando as regras dessa janela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'Adicionar Tarefa':  # Se o evento for adicionar uma tarefa
        # Obtém o texto da tarefa do campo de entrada
        tarefa = values["tarefa"]
        if tarefa: # if diferente de 0 null none ele executa
            # Chama a função para adicionar a tarefa à lista
            adicionar_tarefa(tarefa)
            # Atualiza a lista de tarefas na janela
            janela['tarefas'].update(list(listar_tarefas()))
            janela['tarefa'].update('')  # Limpa o campo de entrada
        
    elif event == 'Remover Tarefa':  # Se o evento for remover uma tarefa
        # Obtém a tarefa selecionada na lista
        selected_tarefa = values['tarefas']
        if selected_tarefa:  # Se uma tarefa estiver selecionada
            # Chama a função para remover a tarefa da lista
            remover_tarefa(selected_tarefa[0])
            # Atualiza a lista de tarefas na janela
            janela['tarefas'].update(list(listar_tarefas()))

    elif event == 'Marcar como Concluída':  # Se o evento for marcar uma tarefa como concluída
        # Obtém a tarefa selecionada na lista
        selected_tarefa = values['tarefas']
        if selected_tarefa:  # Se uma tarefa estiver selecionada
            # Chama a função para marcar a tarefa como concluída ou não
            marcar_como_concluida(selected_tarefa[0])
            # Atualiza a lista de tarefas na janela
            janela['tarefas'].update(list(listar_tarefas()))
            
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()
