class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá meu nome é {self.nome} e tenho {self.idade} anos.")

    def __str__(self):
        return f"{self.nome}"

    def __eq__(self, other):
        if isinstance(other, Pessoa):
            if self.nome == other.nome and self.idade == other.idade:
                return True
        return False

    def __len__(self):
        return  self.idade

    def to_dict(self):
        return {
            "Nome": self.nome,
            "Idade" : self.idade
                }

pessoa1 = Pessoa("João Belai", 19)
pessoa1.apresentar()
print(pessoa1)

pessoa2 = Pessoa("Fernanda Scanacapra", 35)

if pessoa1 == pessoa2:
    print("São iguais")
else:
    print("Não são iguais")

dicionario = pessoa1.to_dict()
print(dicionario)

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def apresentar(self):
        super().apresentar()
        print(f"Olá, eu sou {self.nome}, tenho {self.idade} anos e sou {self.cargo}")

funcionario = Funcionario("ABC", 25, "Aprendiz")
funcionario.apresentar()

lista_pessoas = [pessoa1, pessoa2, funcionario]
for pessoa in lista_pessoas:
    pessoa.apresentar()


class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError('Saldo não pode ser negativo')
        self.__saldo = valor

    # def get_saldo(self):
    #     return self.__saldo
    #
    # def set_saldo(self, valor):
    #     if valor < 0:
    #         raise ValueError('Saldo não pode ser negativo')
    #     self.__saldo = valor


minha_conta = ContaBancaria("João Belai", 50000)

minha_conta.saldo = 500
print(minha_conta.saldo)

from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def autorizar(self, valor):
        pass

    @abstractmethod
    def estornar(self, valor):
        pass


class Pix(Pagamento):
    def autorizar(self, valor):
        print(f"Transferindo R$ {valor} via PIX...")

    def estornar(self, valor):
        print(f"Devolvendo R$ {valor} via PIX...")


Pix().autorizar(122)
Pix().estornar(122)


