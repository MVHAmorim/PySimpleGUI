import PySimpleGUI as sg
from consultaAPI import *

sg.theme('Dark')

moedas =['BTC', 'USD', 'EUR']

layout = [[sg.Text(text='Consulta de Cotações 1.0')],
          [sg.InputOptionMenu(moedas, size=(20, 2), key='opcao'), sg.Button('Consultar')],
          [sg.Text('', key='saida')]]

janela = sg.Window('Cotações de Moedas', layout, resizable=True, finalize=True)
while True:
    event, valor = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Consultar':
        moeda = valor['opcao']
        janela['saida'].update(pegar_cotacoes(moeda))

janela.close()
