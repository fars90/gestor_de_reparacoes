from cliente import criar_tabela_clientes, adicionar_cliente, listar_clientes

def menu():
    criar_tabela_clientes()
    while True:
        print("\nMENU CLIENTES")
        print("1 - Adicionar cliente")
        print("2 - Listar clientes")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            adicionar_cliente(nome, telefone, email)
        elif opcao == "2":
            listar_clientes()
        elif opcao == "0":
            print("A sair do programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()