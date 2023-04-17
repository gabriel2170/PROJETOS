lista = []

frase = 'objetivo;teste;teste1;teste2;teste3;'

nome = ''

for i in frase:
    
    if i == ';':  
        lista.append(nome)
        nome = ''


    nome += i.replace(';', '')
    


print(lista)