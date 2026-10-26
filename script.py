class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario #privado : dois sublinhados

    def apresentar(self):
        print(f"dou {self.nome} e ganho R$ {self.salario}")



ana = Funcionario( "ana",  3000)
ana.salario = 4000
print(ana.salario)
ana.apresentar()