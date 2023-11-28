from database import Database
from user import User
from pokemon import Pokemon

def CLI():
    db = Database("bolt://44.200.53.49:7687", "neo4j", "jails-plugs-compartments")
    user_model = User(db)
    Pokemon_model = Pokemon(db)

    while True:
        print("------ Menu ------")
        print("1. Criar Cadastro de Treinador Pokemon")
        print("2. Procurar Treinador")
        print("3. Atualizar dados de treinador")
        print("4. Remover dados de treinador e todos seus Pokemons")
        print("5. Entrar como Treinador")
        print("6. Sair")

        choice = input("Escolha uma das opcoes (1-6): ")

        if choice == "1":
            name = input("Insira o nome: ")
            email = input("Insira o email: ")
            password = input("Crie uma senha: ")
            id = input("Entrar com ID: ")
            user_model.create(name, email, password, id)
            print("Usuario de treinador criado com sucesso.")

        elif choice == "2":
            id = input("Entre com id do treinador: ")
            user = user_model.get(id)
            if user:
                print(f"Name: {user[0]['u']['name']}, Email: {user[0]['u']['email']}")
            else:
                print("User not found.")

        elif choice == "3":
            id = input("Treinador id: ")
            name = input("Entre com novo nome (aperte enter para pular): ")
            email = input("Entre com novo email (aperte enter para pular): ")
            password = input("Entre com nova senha (aperte enter para pular): ")
            user = user_model.update(id, name, email, password)
            if user:
                print("Usuario atulizado com sucesso.")
            else:
                print("Usuario não encontrado.")

        elif choice == "4":
            id = input("Treinador id: ")
            user = user_model.delete(id)
            if user:
                print("Usuario removido com sucesso.")
            else:
                print("Usuario não encontrado.")

        elif choice == "5":
            email = input("Entre com email do treinador: ")
            password = input("Inserir senha: ")
            user = user_model.get_user_by_email(email)
            if user and user["password"] == password:
                logged_in_user_id = user["id"]
                print("Login completo.")
            else:
                print("Email ou senha invalida.")

            if logged_in_user_id:
                while True:
                    print("\n------ Pokemon CRUD Menu ------")
                    print("1. Registrar Pokemon")
                    print("2. Procurar Pokemon")
                    print("3. Atualizar dados do Pokemon")
                    print("4. Remover dados do Pokemon")
                    print("5. Listar meus Pokemons")
                    print("6. Sair")

                    User_choice = input("Enter your choice (1-7): ")

                    if User_choice == "1":
                        name = input("Entre com o nome do Pokemon: ")
                        pokedexid = input("Entre com o id do Pokemon: ")
                        Pokemon_model.create(logged_in_user_id, name, pokedexid)
                        print("Pokemon registrado com sucesso.")

                    elif User_choice == "2":
                        pokedexid = input("Insira o id do Pokemon: ")
                        pokemon = Pokemon_model.get(pokedexid)
                        if pokemon:
                            print(f"Name: {pokemon[0]['d']['name']}, pokedexid: {pokemon[0]['d']['pokedexid']}")
                        else:
                            print("Pokemon nao encontrado.")

                    elif User_choice == "3":
                        pokedexid = input("Insira o id do pokemon: ")
                        name = input("Entre com um novo nome do Pokemon(aperte Enter para pular): ")
                        pokemon = Pokemon_model.update(pokedexid, name)
                        if pokemon:
                            print("Pokemon atualizado com sucesso.")
                        else:
                            print("Pokemon nao encontrado.")

                    elif User_choice == "4":
                        pokedexid = input("Entre com id do Pokemon: ")
                        pokemon = Pokemon_model.delete(pokedexid)
                        if pokemon:
                            print("Pokemon removido com sucesso.")
                        else:
                            print("Pokemon não encontrado.")

                    elif User_choice == "5":
                        pokemons = Pokemon_model.get_pokemons_from_user(logged_in_user_id)
                        print("Pokemons do treinador:")
                        if pokemons:
                            for pokemon in pokemons:
                                print(f"Pokemon: {pokemon['d']['name']}, pokedexid: {pokemon['d']['pokedexid']}")
                        else:
                            print("Nenhum pokemon encontrado.")

                    elif User_choice == "6":
                        break

                    else:
                        print("Opcao invalida, tente novamente.")

            else:
                print("Treinador nao encontrado.")

        elif choice == "6":
            break

        else:
            print("Escolha invalida, tente novamente.")

CLI()