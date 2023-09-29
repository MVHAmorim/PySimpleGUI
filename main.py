import PySimpleGUI as sg

sg.theme('Black')
names = ['No Pain', 'No Gain']

layout = [
    [sg.Text('Escola da Automação Fiscal', size=(30, 1), key='Status')],
    [sg.InputOptionMenu (names, size=(30, 20)), sg.Button('Executar')],
    [sg.Multiline('', s=(40, 5))],
    [sg.Multiline('', s=(40, 5)), sg.Column([[sg.Button('Aplicar')], [sg.Button('Cancelar')]])]
]

janela = sg.Window('Minha Janela', layout, resizable=True, finalize=True)
janela.bind('<Configure>', "Configure")
status = janela['Status']

while True:
    event, valor = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Configure':
        if janela.TKroot.state() == 'Zoom':
            status.update(value='Janela maximizada!')
        else:
            status.update(value='Janela normal')

janela.close()
