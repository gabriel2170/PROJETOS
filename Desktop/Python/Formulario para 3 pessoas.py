nome1 = input('Digite o primeiro nome: ')
idade1 = input('Didite a idade: ')
nome2 = input('Digite o segundo nome: ')
idade2 = input('Didite a idade: ')
nome3 = input('Digite o terceiro nome: ')
idade3 = input('Didite a idade: ')



tupla_nomes = (nome1, nome2, nome3)

tupla_idades = (idade1, idade2, idade3)

metIter = iter(tupla_nomes)
metIter2 = iter(tupla_idades)

print(next(metIter), next(metIter2))

print(next(metIter), next(metIter2))

print(next(metIter), next(metIter2))



print('---------------------------------------')


