import pywhatkit as pw
import PySimpleGUI as pg
import pandas as pa
import os



layout = [
    [pg.Push(),pg.Button('Enviar') , pg.Button('Atualizar Contatos'), pg.Button('Sair'), pg.Push()],
    [pg.Input(key='campanha'), pg.FileBrowse('Arquivo')]
          ]

janela = pg.Window('Teste de Interface',layout, size=(420,100))



while True:
    
    event, values = janela.read()

    if event == 'Enviar':
       try:
           if os.path.exists('Contatos.xlsx'):

               cont = pa.read_excel('Contatos.xlsx')

               numero = cont['CONTATOS']
               grupo = cont['GRUPOS']
               
               pw.start_server()

               if numero != '' or numero != None: 
                    pw.sendwhats_image(numero, values['campanha'])

               elif numero == '' and grupo != '' or numero == None and grupo != None:
                    pw.sendwhats_image(grupo, values['campanha'])

               elif numero == '' and grupo == '' or numero == None and grupo == None:
                   pg.Popup('Ambos os campos do numero e grupo estao preenchidos, preencha apenas um dos 2 campos por linha antes de prosseguir!!')
               else:
                   pg.Popup('Campanha Enviada com Sucesso!!')
                   
       except OSError:
           pg.Popup('Arquivo Contatos esta Aberto, feche o arquivo antes de prosseguir!!')
    
    if event == 'Atualizar Contatos':
        if os.path.exists('Contatos.xlsx'):
            os.startfile('Contatos.xlsx')
            
        
    if event == pg.WIN_CLOSED or event == 'Sair':
        break
    
            
janela.close()




        

        
