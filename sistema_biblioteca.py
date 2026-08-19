class Livro:
    def __init__(self, titulo, autor, isbn, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel
        self.emprestado_para = None  # Nome do usuário que emprestou, se aplicável

    def __str__(self):
        status = "Disponível" if self.disponivel else f"Emprestado para: {self.emprestado_para}"
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Status: {status}"

class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista de livros

    def adicionar_livro(self, titulo, autor, isbn):
        livro = Livro(titulo, autor, isbn)
        self.livros.append(livro)
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        print("\nLista de Livros:")
        for i, livro in enumerate(self.livros, 1):
            print(f"{i}. {livro}")

    def emprestar_livro(self, isbn, nome_usuario):
        for livro in self.livros:
            if livro.isbn == isbn:
                if livro.disponivel:
                    livro.disponivel = False
                    livro.emprestado_para = nome_usuario
                    print(f"Livro '{livro.titulo}' emprestado para {nome_usuario}.")
                    return
                else:
                    print(f"Livro '{livro.titulo}' já está emprestado.")
                    return
        print("Livro não encontrado pelo ISBN.")

    def devolver_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                if not livro.disponivel:
                    livro.disponivel = True
                    usuario = livro.emprestado_para
                    livro.emprestado_para = None
                    print(f"Livro '{livro.titulo}' devolvido por {usuario}.")
                    return
                else:
                    print(f"Livro '{livro.titulo}' já está disponível.")
                    return
        print("Livro não encontrado pelo ISBN.")

def menu():
    biblioteca = Biblioteca()
    while True:
        print(" Sistema de Biblioteca ")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            biblioteca.adicionar_livro(titulo, autor, isbn)
        
        elif opcao == "2":
            biblioteca.listar_livros()
        
        elif opcao == "3":
            isbn = input("ISBN do livro a emprestar: ")
            nome_usuario = input("Nome do usuário: ")
            biblioteca.emprestar_livro(isbn, nome_usuario)
        
        elif opcao == "4":
            isbn = input("ISBN do livro a devolver: ")
            biblioteca.devolver_livro(isbn)
        
        elif opcao == "5":
            print("Obrigado por usar o sistema!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu principal
if __name__ == "__main__":
    menu()
