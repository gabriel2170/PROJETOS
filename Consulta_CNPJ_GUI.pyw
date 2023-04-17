import PySimpleGUI as pg
import requests
import json

layout= (
    [pg.Push(), pg.Input(key='CNPJ', size=(18,20)), pg.Button('Buscar_CNPJ')],
    [pg.Input(key='cnpj', size=(18,20), readonly=True)],
    [pg.Input(key='nome'),pg.Text('Razao Social')],
    [pg.Input(key='fantasia'),pg.Text('Nome Fantasia')],
    [pg.Input(key='cep'),pg.Text('CEP')],
    [pg.Input(key='municipio'),pg.Text('Cidade')],
    [pg.Input(key='endereco'),pg.Text('Endereço')],
    [pg.Input(key='complemento'),pg.Text('Complemento')],
    [pg.Input(key='bairro'),pg.Text('Bairro')],
    [pg.Input(key='numero'),pg.Text('Numero')],
    [pg.Input(key='uf'),pg.Text('UF')],  
    [pg.Button('Fechar')] 
    )

janela = pg.Window("CONSULTA CNPJ", layout, size=(450,350))


while True:

    event, values = janela.read()

    if event == 'Buscar_CNPJ':
        cnpj = values['CNPJ']

        url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
        querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
        response = requests.request("GET", url, params=querystring)


        if 'ERROR' in response.text or 'CNPJ inválido' in response.text or len(cnpj) > 14 or len(cnpj) < 14 :
            pg.Popup('CNPJ Invalido')
            
        else:
            resp = json.loads(response.text)

    
            janela['nome'].update(resp['nome'])
            janela['fantasia'].update(resp['fantasia'])
            janela['cnpj'].update(resp['cnpj'])
            janela['cep'].update(resp['cep'])
            janela['endereco'].update(resp['logradouro'])
            janela['bairro'].update(resp['bairro'])
            janela['municipio'].update(resp['municipio'])
            janela['uf'].update(resp['uf'])
            janela['numero'].update(resp['numero'])
            janela['complemento'].update(resp['complemento'])
            
    if event == 'Fechar' or event == pg.WIN_CLOSED:
        break


janela.close()
