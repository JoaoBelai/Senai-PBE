class Produto:
    def __init__(self, nome: str, qtd_disponivel: int, preco_unit: float):
        self.nome = nome
        self.qtd_disponivel = qtd_disponivel
        self.preco_unit = preco_unit

    def adcionar_quantidade(self, quantidade):
        print("\nAumento na quantidade de itens realizada com sucesso!")
        self.qtd_disponivel += quantidade
        print(f"Quantidade atual de {self.nome}: {self.qtd_disponivel}")


    def remover_quantidade(self, quantidade):
        if self.qtd_disponivel <=0:
            print("\nRemoção não pode ser realizada, você não tem mais itens desse tipo no estoque")
        else:
            self.qtd_disponivel -= quantidade
            if self.qtd_disponivel < 0:
                self.qtd_disponivel = 0
                print("\nVocê tentou remover mais itens do que há no estoque")
                print(f"Quantidade atual de {self.nome}: {self.qtd_disponivel}")
            else:
                print("\nRemoção de itens realizada com sucesso!")
                print(f"Quantidade atual de {self.nome}: {self.qtd_disponivel}")
    
    def calcular_valor_total(self):
        valor_total = self.qtd_disponivel * self.preco_unit
        print(f"\nValor total do estoque de {self.nome}: R${valor_total:.2f}")


class KitProduto(Produto):
    def __init__(self, nome, qtd_disponivel, preco_unit):
        super().__init__(nome, qtd_disponivel, preco_unit)
        self.lista_produto = []

    def adcionar_produto(self, produto: Produto):
        self.lista_produto.append(produto)
        print("\nProduto adicionado com sucesso!")
    
    def remover_produto(self, produto: Produto):
        if produto in self.lista_produto:
            self.lista_produto.remove(produto)
            print("\nProduto removido com sucesso!")
        else:
            print("\nProduto não presente nesse kit")
    
    def calcular_valor_total(self):
        self.preco_unit = 0
        for produto in self.lista_produto:
            valor = produto.preco_unit * produto.qtd_disponivel
            self.preco_unit += valor
        
        print(f"\nValor total do kit: R${self.preco_unit:.2f}")


produto1 = Produto("Bomba de Combustível", 10, 55.9)
produto2 = Produto("Vela", 15, 15.6)
produto3 = Produto("Cabo de Vela", 15, 20.4)

produto1.adcionar_quantidade(5)

produto2.remover_quantidade(5)
produto3.remover_quantidade(5)
produto1.remover_quantidade(20)

produto2.calcular_valor_total()
produto3.calcular_valor_total()


kit1 = KitProduto("Jogo de cabo e Vela", 1, 0)

kit1.adcionar_produto(Produto("Vela", 1, 15.6))
kit1.adcionar_produto(Produto("Cabo de Vela", 1, 20.4))
kit1.adcionar_produto(produto1)
kit1.remover_produto(produto1)
kit1.calcular_valor_total()


