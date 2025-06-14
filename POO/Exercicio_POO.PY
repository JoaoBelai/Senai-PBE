class ItemBiblioteca:
    def __init__(self, titulo: str , ano_publicacao: int, disponivel: bool = True):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel == True:
            print("\nO item foi emprestado com sucesso!")
            self.disponivel = False
        else:
            print("\nO item já está emprestado, não pode ser emprestado para outra pessoa!")
    
    def devolver(self):
        if self.disponivel == False:
            print("\nO item foi devolvido com sucesso!")
            self.disponivel = True
        else:
            print("\nO item já está disponível, não pode ser devolvido!")
        
    def obter_info(self):
        if self.disponivel == True:
            disponivel = "Sim"
        else:
            disponivel = "Não"

        print(f"\nTítulo: {self.titulo}"
              f"\nAno: {self.ano_publicacao}"
              f"\nDisponível:{disponivel}")
        
class ColecaoLivro(ItemBiblioteca):
    def __init__(self, titulo: str, ano_publicacao: int, disponivel: bool = True,):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.lista_livro = []

    def adcionar_livro(self, livro: ItemBiblioteca):
        self.lista_livro.append(livro)
    
    def verificar_disponibilidade_colecao(self):
        disponibilidade = True

        for livro in self.lista_livro:
            if livro.disponivel == False:
                disponibilidade = False
            else:
               pass

        if disponibilidade == True:
            print("\nColeção disponível")
            self.disponivel = True
        else:
            print("\nColeção indisponível")
            self.disponivel = False
    
    def obter_info(self):
        super().obter_info()
        
        print(f"Livros da coleção:")    
        for i in range(len(self.lista_livro)):
            print(self.lista_livro[i].titulo)

class Revista(ItemBiblioteca):
    def __init__(self, numero_edicao: int, titulo: str, ano_publicacao: int, disponivel = True):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.numero_edicao = numero_edicao
    
    def atualizar_edicao(self, nova_edicao):
        if nova_edicao > 0:
            self.numero_edicao = nova_edicao
            print("\nNúmero de edição atualizado com sucesso!")
        else:
            print("\nNúmero de edição inválido")
    
    def restringir_emprestimo(self, dias_max):
        if self.ano_publicacao >= 2000:
            print(f"\nLimite de dias de empréstimo restringido para {dias_max} dias")
            return True
        else:
            print("\nRevistas anteriores ao ano 2000 já estão restringidas para 7 dias.")
            return False
    
    def obter_info(self):
        super().obter_info()
        print(f"Edição: {self.numero_edicao}")

class Biblioteca:
    def __init__(self):
        self.dicionario_itens = {}
    
    def adicionar_item(self, item: ItemBiblioteca):
        if item.titulo in self.dicionario_itens:
            print("\nItem já presente na biblioteca!")
        else:
            self.dicionario_itens[item.titulo] = item
            print("\nItem adicionado a biblioteca com sucesso!")
    
    def remover_item(self, titulo):
        if titulo in self.dicionario_itens:   
            del self.dicionario_itens[titulo]
            print("\nItem deletado com sucesso")
        else:
            print("\nItem não encontrado na biblioteca!")
    
    def listar_itens_disponiveis(self):
        lista_titulos = []
        for titulo, item in self.dicionario_itens.items():
            if item.disponivel:
                lista_titulos.append(titulo)
            
        return lista_titulos
    
    def contar_itens_emprestados(self):
        contador = 0
        for item in self.dicionario_itens.values():
            if not item.disponivel:
                contador += 1

        return contador

class RelatiorioBiblioteca:
    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca

    def gerar_relatorio_completo(self):
        print("\nRelatório completo:")
        for item in self.biblioteca.dicionario_itens.values():
            item.obter_info()
    
    def gerar_relatorio_disponibilidade(self):
        print("\nRelatório de Itens Disponíveis:")
        disponiveis = []
        contador = 0
        for titulo, item in self.biblioteca.dicionario_itens.items():
            if item.disponivel:
                disponiveis.append(titulo)
                contador += 1
        print(f"Itens: {contador}")
        str_disponiveis = " ".join(disponiveis)
        print(str_disponiveis)
    
    def gerar_relatorio_emprestimo(self):
        print("\nRelatório de Itens Emprestados:")
        contador = 0
        for item in self.biblioteca.dicionario_itens.values():
            if not item.disponivel:
                contador += 1

        porcentagem = (contador*100)/len(self.biblioteca.dicionario_itens)
        porcentagem = str(porcentagem)
        contador = str(contador)
        str_indisponivel = "Itens Indisponíveis: " + contador + ", " + porcentagem + "% dos itens totais"
        print(str_indisponivel)



livro1 = ItemBiblioteca("Diário de um Banana", 2008, True)
livro1.emprestar()
livro1.devolver()
livro1.obter_info()


colecao1 = ColecaoLivro("Diário de um Banana", 2025, True)
colecao1.adcionar_livro(livro1)
colecao1.adcionar_livro(ItemBiblioteca("Diário de um Banana: Rodrick é o cara", 2009, False))
colecao1.verificar_disponibilidade_colecao()
colecao1.obter_info()


revista1 = Revista(10, "Revista Veja 1", 2010, False)
revista1.atualizar_edicao(20)
revista1.restringir_emprestimo(10)
revista1.obter_info()


biblioteca1 = Biblioteca()
biblioteca1.adicionar_item(livro1)
biblioteca1.adicionar_item(revista1)
biblioteca1.adicionar_item(livro1)
print(biblioteca1.contar_itens_emprestados())
print(biblioteca1.listar_itens_disponiveis())
biblioteca1.remover_item("Diário de um Banana")
biblioteca1.remover_item("Diário de um Banana")
biblioteca1.adicionar_item(livro1)


relatorio = RelatiorioBiblioteca(biblioteca1)
relatorio.gerar_relatorio_completo()
relatorio.gerar_relatorio_disponibilidade()
relatorio.gerar_relatorio_emprestimo()
