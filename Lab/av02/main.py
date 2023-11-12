from database import Database
from teacher_crud import TeacherCRUD

class CLI:
    def __init__(self):
        db = Database("bolt://54.175.13.242:7687", "neo4j", "driller-clocks-barriers")
        self.teacher_crud = TeacherCRUD(db)

    def run(self):
        while True:
            print("Menu")
            print("1 - Criar professor")
            print("2 - Pesquisar professor por name")
            print("3 - Atualizar CPF de um professor")
            print("4 - Deletar professor")
            print("0 - Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.create_teacher()

            elif choice == "2":
                self.search_teacher()

            elif choice == "3":
                self.update_teacher()

            elif choice == "4":
                self.delete_teacher()

            elif choice == "0":
                break

            else:
                print("Opção invalida!")

    def create_teacher(self):
        print("Criar professor")
        name = input("Nome: ")
        ano_nasc = int(input("Ano de nascimento: "))
        cpf = input("CPF: ")

        self.teacher_crud.create(name, ano_nasc, cpf)
        print("Professor criado com sucesso!")

    def search_teacher(self):
        print("Pesquisar professor por name")
        name = input("Nome: ")

        teacher = self.teacher_crud.read(name)
        if teacher:
            print("Professor encontrado:")
            print(teacher)
        else:
            print("Professor não encontrado.")

    def update_teacher(self):
        print("Atualizar CPF de um professor")
        name = input("Nome: ")
        new_cpf = input("Novo CPF: ")

        self.teacher_crud.update(name, new_cpf)
        print("CPF atualizado com sucesso!")

    def delete_teacher(self):
        print("Deletar professor")
        name = input("Nome: ")

        self.teacher_crud.delete(name)
        print("Professor deletado com sucesso!")

cli = CLI()
cli.run()