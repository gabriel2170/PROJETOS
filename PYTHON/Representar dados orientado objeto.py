class entradaDados:

  def __init__(self, nome, idade, cidade):
    self.nome = nome
    self.idade = idade
    self.cidade = cidade


  def setNome(self, nome):
    self.nome = nome

  def getNome(self):
    return self.nome

  def setIdade(self, idade):
    self.idade = idade

  def getIdade(self):
    return self.idade

  def setCidade(self, cidade):
    self.cidade = cidade

  def getCidade(self):
    return self.cidade

  def toString(self):
    print("Nome: " , self.nome , " Idade: " , self.idade , " Cidade: " , self.cidade)
     


obj = entradaDados('gabriel', 24, 'Franca')


obj.toString()