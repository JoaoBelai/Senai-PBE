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
        if self.disponivel == True:
            disponivel = "Sim"
        else:
            disponivel = "Não"

        print(f"\nNome Coleção: {self.titulo}"
              f"\nAno: {self.ano_publicacao}"
              f"\nDisponível: {disponivel}"
              f"\nLivros da coleção:")
        
        for i in range(len(self.lista_livro)):
            print(self.lista_livro[i].titulo)


        



livro1 = ItemBiblioteca("Diário de um Banana", 2008, True)

livro1.emprestar()
livro1.devolver()
livro1.obter_info()

colecao1 = ColecaoLivro("Diário de um Banana", 2025, True)

colecao1.adcionar_livro(livro1)
colecao1.adcionar_livro(ItemBiblioteca("Diário de um Banana: Rodrick é o cara", 2009, False))

colecao1.verificar_disponibilidade_colecao()
colecao1.obter_info()