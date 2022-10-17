import pandas as pd

tabela = pd.read_excel('/content/beneficio.xlsx')

opc = int(input('Digite uma opcao (0-Junho/1-Janeiro/2-Maio/3-Abril/4-Fevereiro/5-Marco/6-Julho): '))

if opc >= 7 or opc < 0:
    print('Nao foi encontrado') 
else:
    display(tabela.iloc[opc])
