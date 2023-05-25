import PySimpleGUI as pg
from pycep_correios import get_address_from_cep, WebService, exceptions

layout= (
    [pg.Push(), pg.Input(key='CEP', size=(12,20)), pg.Button('Buscar_CEP')],
    [pg.Input(key='cep', size=(12,20), readonly=True)],
    [pg.Input(key='endereco'),pg.Text('Endereço')],   
    [pg.Input(key='bairro'),pg.Text('Bairro'), ],
    [pg.Input(key='cidade'),pg.Text('Cidade'), ],
    [pg.Input(key='uf'),pg.Text('UF'), ],
    [pg.Input(key='complemento'),pg.Text('Complemento'),],
    [pg.Button('Fechar')] 
    )

janela = pg.Window("CONSULTA CEP", layout, size=(450,250))


while True:

    event, values = janela.read()

    if event == 'Buscar_CEP':
        try:
            endereco = get_address_from_cep(values['CEP'], webservice=WebService.APICEP)
            janela['cep'].update(endereco['cep'])
            janela['endereco'].update(endereco['logradouro'])
            janela['bairro'].update(endereco['bairro'])
            janela['cidade'].update(endereco['cidade'])
            janela['uf'].update(endereco['uf'])
            janela['complemento'].update(endereco['complemento'])
            
        except exceptions.InvalidCEP:
            pg.Popup('CEP Invalido')

        except exceptions.CEPNotFound:
            pg.Popup('CEP Nao Foi Encontrado')

        except exceptions.ConnectionError:
            pg.Popup('Erro de Conexao com Servidor de Consulta(Correios)')

        except exceptions.Timeout:
            pg.Popup('Timeout na Busca')

        except exceptions.HTTPError:
            pg.Popup('URL do Servidor de Pesquisa esta Offiline')

        except exceptions.BaseException:
            pg.Popup('Erro nos Dados Inseridos')

            
    if event == 'Fechar' or event == pg.WIN_CLOSED:
        break


janela.close()
