from pycep_correios import get_address_from_cep, WebService, exceptions


#cep = input("Seu CEP: ")


try:
    endereco = get_address_from_cep('14400740', webservice=WebService.APICEP)

    print(endereco)
    print(endereco['bairro'])
    print(endereco['cep'])
    print(endereco['cidade'])
    print(endereco['logradouro'])
    print(endereco['uf'])
    print(endereco['complemento'])
    
except exceptions.InvalidCEP:
    print('CEP Invalido')

except exceptions.CEPNotFound:
    print('CEP Nao Foi Encontrado')

except exceptions.ConnectionError:
    print('Erro de Conexao com Servidor de Consulta(Correios)')

except exceptions.Timeout:
    print('Timeout na Busca')

except exceptions.HTTPError:
    print('URL do Servidor de Pesquisa esta Offiline')

except exceptions.BaseException:
    print('Erro nos Dados Inseridos')









