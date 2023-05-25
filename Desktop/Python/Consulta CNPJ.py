import requests
import json



cnpj = input('Seu CNPJ: ')

url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"ST"}
response = requests.request("GET", url, params=querystring)


if 'CNPJ inválido' in response.text:
    print('CNPJ Invalido')

else:
    resp = json.loads(response.text)


    print(resp)

        
    #print(resp['nome'])
    #print(resp['fantasia'])
    #print(resp['cnpj'])
    #print(resp['cep'])
    #print(resp['logradouro'])
    #print(resp['bairro'])
    #print(resp['municipio'])
    #print(resp['uf'])
    #print(resp['numero'])
    #print(resp['complemento'])



    
    



