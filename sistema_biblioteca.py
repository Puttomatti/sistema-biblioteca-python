class Livro:
    def __init__(self, titulo, autor, isbn, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel
        self.emprestado_para = None

    def __str__(self):
        status = (
            "Disponível"
            if self.disponivel
            else f"Emprestado para: {self.emprestado_para}"
        )

        return (
            f"Título: {self.titulo}, "
            f"Autor: {self.autor}, "
            f"ISBN: {self.isbn}, "
            f"Status: {status}"
        )


class Biblioteca:
    def __init__(self):
        self.livros = []

    def buscar_livro_por_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro

        return None

    def adicionar_livro(self, titulo, autor, isbn):
        if self.buscar_livro_por_isbn(isbn):
            print("Já existe um livro cadastrado com esse ISBN.")
            return

        livro = Livro(titulo, autor, isbn)
        self.livros.append(livro)

        print(f"Livro '{titulo}' adicionado com sucesso!")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return

        print("\nLista de livros:")

        for i, livro in enumerate(self.livros, 1):
            print(f"{i}. {livro}")

    def emprestar_livro(self, isbn, nome_usuario):
        livro = self.buscar_livro_por_isbn(isbn)

        if not livro:
            print("Livro não encontrado pelo ISBN.")
            return

        if not livro.disponivel:
            print(f"Livro '{livro.titulo}' já está emprestado.")
            return

        livro.disponivel = False
        livro.emprestado_para = nome_usuario

        print(f"Livro '{livro.titulo}' emprestado para {nome_usuario}.")

    def devolver_livro(self, isbn):
        livro = self.buscar_livro_por_isbn(isbn)

        if not livro:
            print("Livro não encontrado pelo ISBN.")
            return

        if livro.disponivel:
            print(f"Livro '{livro.titulo}' já está disponível.")
            return

        usuario = livro.emprestado_para

        livro.disponivel = True
        livro.emprestado_para = None

        print(f"Livro '{livro.titulo}' devolvido por {usuario}.")


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n=== Sistema de Biblioteca ===")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Título do livro: ").strip()
            autor = input("Autor: ").strip()
            isbn = input("ISBN: ").strip()

            biblioteca.adicionar_livro(titulo, autor, isbn)

        elif opcao == "2":
            biblioteca.listar_livros()

        elif opcao == "3":
            isbn = input("ISBN do livro a emprestar: ").strip()
            nome_usuario = input("Nome do usuário: ").strip()

            biblioteca.emprestar_livro(isbn, nome_usuario)

        elif opcao == "4":
            isbn = input("ISBN do livro a devolver: ").strip()

            biblioteca.devolver_livro(isbn)

        elif opcao == "5":
            print("Obrigado por usar o sistema!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
