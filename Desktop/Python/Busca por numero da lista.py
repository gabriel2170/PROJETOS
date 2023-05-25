import numpy as np


n1 = int(input('Digite o primeiro numero: \n'))
n2 = int(input('Digite o segundo numero: \n'))
n3 = int(input('Digite o terceiro numero: \n'))
n4 = int(input('Digite o quarto numero: \n'))
n5 = int(input('Digite o quinto numero: \n'))
n6 = int(input('Digite o sexto numero: \n'))
n7 = int(input('Digite o setimo numero: \n\n'))


lista = np.array([n1,n2,n3,n4,n5,n6,n7])


num = int(input('Selecione 1 dos 7 numeros digitados: '))

posicao = np.where(lista == num)

busca = np.searchsorted(lista, num)


print('\n\nNumero: ' , busca, 'Posicao: ' , posicao) 