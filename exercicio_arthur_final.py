# Criando o layout
import PySimpleGUI as sg

lista_de_tarefas = []


def adicionar_tarefa(texto):
    lista_de_tarefas.append({'concluida': False, 'texto': texto})


def listar_tarefas():
    return [f"{'[x]' if nome_da_tarefa['concluida'] else '[ ]'} {nome_da_tarefa['texto']}" for nome_da_tarefa in lista_de_tarefas]


def remover_tarefa(nome_da_tarefa):
    nome_da_tarefa = nome_da_tarefa[4:]
    for texto_tarefa in lista_de_tarefas:
        if texto_tarefa['texto'] == nome_da_tarefa:
            lista_de_tarefas.remove(texto_tarefa)
            break


def marcar_concluida(nome_da_tarefa):
    nome_da_tarefa = nome_da_tarefa[4:]
    for texto_tarefa in lista_de_tarefas:
        if texto_tarefa['texto'] == nome_da_tarefa:
            texto_tarefa['concluida'] = True
            break


def desmarcar_concluida(nome_da_tarefa):
    nome_da_tarefa = nome_da_tarefa[4:]
    for texto_tarefa in lista_de_tarefas:
        if texto_tarefa['texto'] == nome_da_tarefa:
            texto_tarefa['concluida'] = False
            break


def resetar(janela):
    janela.close()
    lista_de_tarefas.clear()
    return criar_janela_inicial()


def criar_janela_inicial():
    sg.theme('DarkBlue')
    layout = [
        [sg.Frame('Tarefas', layout=[]),
         sg.InputText("", key="valor_digitado"),
         sg.Button('Adicionar Tarefa')],
        [sg.Listbox(values=[], size=(80, 20), key='lista_tarefas_digitadas')],
        [sg.Button('Remover Tarefa'),
         sg.Button('Marcar como Concluída'),
         sg.Button('Desmarcar como Concluída'),
         sg.Button('Resetar')]
    ]
    return sg.Window('AP2 DE PRÁTICAS DE PROGRAMAÇÃO - Arthur Farias', layout=layout, finalize=True, element_justification='center')


janela = criar_janela_inicial()

while True:
    evento, values = janela.read()
    if evento == sg.WIN_CLOSED:
        break

    elif evento == 'Adicionar Tarefa':
        nome_da_tarefa = values["valor_digitado"]
        if nome_da_tarefa:
            adicionar_tarefa(nome_da_tarefa)
            janela['lista_tarefas_digitadas'].update(list(listar_tarefas()))
            janela['valor_digitado'].update('')

    elif evento == 'Remover Tarefa':
        selected_tarefa = values['lista_tarefas_digitadas']
        if selected_tarefa:
            remover_tarefa(selected_tarefa[0])
            janela['lista_tarefas_digitadas'].update(list(listar_tarefas()))

    elif evento == 'Marcar como Concluída':
        selected_tarefa = values['lista_tarefas_digitadas']
        if selected_tarefa:
            marcar_concluida(selected_tarefa[0])
            janela['lista_tarefas_digitadas'].update(list(listar_tarefas()))

    elif evento == 'Desmarcar como Concluída':
        selected_tarefa = values['lista_tarefas_digitadas']
        if selected_tarefa:
            desmarcar_concluida(selected_tarefa[0])
            janela['lista_tarefas_digitadas'].update(list(listar_tarefas()))

    elif evento == 'Resetar':
        janela = resetar(janela)
