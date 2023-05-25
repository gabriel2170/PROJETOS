from mysql import connector


class Banco:
    def iniciarBanco(self):
        db = connector.connect(
            host="127.0.0.1", 
            user="root", 
            password="klmolk127")

        cursor = db.cursor()

        try:
            cursor.execute("CREATE DATABASE Banco")
            print("Banco foi Criado!")

        except:
            print("Banco ja Existe!")

    def criarTabela(self):
        db = connector.connect(
            host="127.0.0.1", 
            user="root", 
            password="klmolk127", 
            database="Banco"
        )

        cursor = db.cursor()

        try:
            cursor.execute(f"CREATE TABLE funcionario (nome VARCHAR(100), idade INT, profissao VARCHAR(50))")
            print("Tabela foi Criado!")

        except:
            print("Tabela ja Existe!!")

    def inserirDados(self, nome, idade, profissao):
        db = connector.connect(
            host="127.0.0.1", 
            user="root", 
            password="klmolk127", 
            database="Banco"
        )

        cursor = db.cursor()

        self.nome = nome
        self.idade = idade
        self.profissao = profissao

        sql = "INSERT INTO funcionario (nome, idade, profissao) VALUES (%s, %s , %s)"
        val = (self.nome, self.idade, self.profissao)
        try:
            cursor.execute(sql, val)      
            db.commit()
            print(f"Funciorio {nome} foi cadastrado!")

        except:
            print("Tabela não existe!!")


    def consultarTabela(self):
        db = connector.connect(
            host="127.0.0.1", 
            user="root", 
            password="klmolk127", 
            database="Banco"
        )

        cursor = db.cursor()

       
        try:
            cursor.execute("SELECT * FROM funcionario")
            resultado = cursor.fetchall()

            if cursor.rowcount == 0:
                print("Tabela Vazia!!")
            
            else:
                for x in resultado:
                    print(x)

        except:
            print('Tabela não existe!!')
             


    def consultarBanco(self):
        db = connector.connect(
            host="127.0.0.1", 
            user="root", 
            password="klmolk127", 
            database="Banco"
        )

        cursor = db.cursor()

        cursor.execute("SHOW DATABASES")

        for x in cursor:      
            print(x)
    
    def deletarPNome(self, nome):
        db = connector.connect(
            host="127.0.0.1", 
            user="root", 
            password="klmolk127", 
            database="Banco"
        )

        cursor = db.cursor()

        self.nome = nome 

        try:
            if cursor.rowcount == 0:
                cursor.execute(f"DELETE FROM funcionario WHERE nome = '{self.nome}'")
                db.commit()
                print(f'Dados do funcionario {self.nome} foram deletados!')
            else:
                print(f'O nome {self.nome} nao esta cadastrado!!')
        except:
            print('Tabela não existe!!')
        

    def deletarPIdade(self, idade):
        db = connector.connect(
            host="127.0.0.1", 
            user="root", 
            password="klmolk127", 
            database="Banco"
        )

        cursor = db.cursor()

        self.idade = idade 

        try:
            if cursor.rowcount == 0:
                cursor.execute(f"DELETE FROM funcionario WHERE idade = {self.idade}")
                db.commit()
                print(f'Dados do funcionario {self.idade} foram deletados!')
            else:
                 print(f'A idade {self.idade} nao esta cadastrada!!')
        except:
           print('Tabela não existe!!')


    def deletarPProfissao(self, profissao):
        db = connector.connect(
            host="127.0.0.1", 
            user="root", 
            password="klmolk127", 
            database="Banco"
        )

        cursor = db.cursor()

        self.profissao = profissao 

        try:
            if cursor.rowcount == 0:
                cursor.execute(f"DELETE FROM funcionario WHERE profissao = '{self.profissao}'")
                db.commit()
                print(f'Dados do funcionario {self.profissao} foram deletados!')
            else:
                print(f'A profissão {self.profissao} nao esta cadastrada!!')
        except:
            print('Tabela não existe!!')


    def deletarTabela(self):
        db = connector.connect(
            host="127.0.0.1", 
            user="root", 
            password="klmolk127", 
            database="Banco"
        )

        cursor = db.cursor()

        try:
            cursor.execute("DROP TABLE funcionario")
          
            print('Tabela Deletada!!')
        except:
            print('Tabela não Existe!!')

    def deletarBanco(self):
        try:
            db = connector.connect(
                host="127.0.0.1", 
                user="root", 
                password="klmolk127", 
                database="Banco"
            )

            cursor = db.cursor()
            cursor.execute("DROP DATABASE Banco")
          
            print('Banco Deletado!!')
        except:
            print('Banco não Existe!!')


query = Banco()

while(1):

    n = int(input('Digite a opção desejada (1-Criar Banco / 2-Criar Tabela / 3-Inserir Dados na Tabela/ 4-Deletar Tabela/ 5-Deletar dados/ 6-Consultar Bancos/ 7-Consultar Tabelas/ 8-Deletar Banco / 0-Sair): '))

    if n < 0 or n > 8:
        print('Opção Invalida!!')
    
    if n == 0:
        break

    if n == 1:
        query.iniciarBanco()
    
    if n == 2:
        query.criarTabela()
    
    if n == 3:
        nome = input("Insira o nome do funcionario: ")
        idade = input("Insira a idade do funcionario: ")
        profissao = input("Insira a profissao do funcionario: ")

        query.inserirDados(nome, idade, profissao)

    if n == 4: 
        query.deletarTabela()
    if n == 5:
        x = 1
        while(x != 0):
            x = int(input('(Selecione um criterio para deletar os dados: 1-Nome, 2-idade, 3-profissao, 0-Sair): '))
    
            if x < 0 or x > 3 :
                print('Opção Invalida!!')

            if x == 1:
                nome = input("Insira o nome do funcionario: ")
                query.deletarPNome(nome)
           
            if x == 2:
                idade = input("Insira a idade do funcionario: ")
                query.deletarPIdade(idade)        
        
            if x == 3:
                profissao = input("Insira a profissao do funcionario: ")
                query.deletarPProfissao(profissao)
          
    if n == 6:
        query.consultarBanco()
    
    if n == 7:
        query.consultarTabela()
    
    if n == 8:
        query.deletarBanco()
