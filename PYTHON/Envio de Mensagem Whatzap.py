import pywhatkit
import PySimpleGUI as pg
import pandas as pd
import time
import pyautogui as pa

tabela = pd.read_excel('mensagem.xlsx')

layout = (
    [pg.Push(), pg.Button("Enviar"),pg.Button("Enviar pela Planilha"),pg.Button("Fechar"), pg.Push()],
    [pg.Multiline(size=(60,20), key='msg')]
    )


janela = pg.Window('WHATZAP MESSAGENS', layout, size=(400,400))


def horario(x, y, v):
    vetor = []
    for z in v:
        if z != ',' or type(z) == int:
            vetor.append(z)

    x = vetor[0] + vetor[1]
    y = vetor[2] + vetor[3]

    return int(x),int(y)
    
    


while True:
    event, values = janela.read()

    if event == 'Enviar':
   
        pywhatkit.sendwhatmsg_instantly('+5516992200625', values['msg'])        
        pa.click(button='left')
        pa.press('enter')

    if event == 'Fechar' or event == pg.WIN_CLOSED:
        break


janela.close()
