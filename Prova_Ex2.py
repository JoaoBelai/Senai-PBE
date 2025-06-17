# Classe Produto sendo instanciada
class Produto:
    # metedo de inicialização pedindo os atributos nome, quantidade disponível e preço unitário como obrigatórios
    def __init__(self, nome: str, qtd_disponivel: int, preco_unit: float):
        self.nome = nome
        self.qtd_disponivel = qtd_disponivel
        self.preco_unit = preco_unit

    # método adicionar quantidade aumentando o self.qtd_disponivel
    def adcionar_quantidade(self, quantidade):
        print("\nAumento na quantidade de itens realizada com sucesso!")
        self.qtd_disponivel += quantidade
        print(f"Quantidade atual de {self.nome}: {self.qtd_disponivel}")

    # método remover quantidade diminuindo o self.qtd_disponivel, desde que já não esteja zerada
    # e caso diminua mais do que tem no estoque o valor do estoque é setado em 0
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
    
    # método calcular valor total do estoque que faz a quantidade de produtos vezs o preço unitario e da o valor total
    def calcular_valor_total(self):
        valor_total = self.qtd_disponivel * self.preco_unit
        print(f"\nValor total do estoque de {self.nome}: R${valor_total:.2f}")


class KitProduto(Produto):
    # método de inicialização puxando os valores da classe pai e criando a lista de produtos
    def __init__(self, nome, qtd_disponivel, preco_unit):
        super().__init__(nome, qtd_disponivel, preco_unit)
        self.lista_produto = []

    # método adicionar produto que recebe um objeto Produto como parametro e adiciona ele na lista
    def adcionar_produto(self, produto: Produto):
        self.lista_produto.append(produto)
        print("\nProduto adicionado com sucesso!")
    
    # método remover produto que recebe um objeto Produto como parametro e remove ele da lista caso ele esteja presente nela
    def remover_produto(self, produto: Produto):
        if produto in self.lista_produto:
            self.lista_produto.remove(produto)
            print("\nProduto removido com sucesso!")
        else:
            print("\nProduto não presente nesse kit")
    
    # método calcular valor total do kit, para cada produto na lista ele multiplica a quantidade pelo preço e soma no valor do kit e passa o resultado
    def calcular_valor_total(self):
        self.preco_unit = 0
        for produto in self.lista_produto:
            valor = produto.preco_unit * produto.qtd_disponivel
            self.preco_unit += valor
        
        print(f"\nValor total do kit: R${self.preco_unit:.2f}")


#testes
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


