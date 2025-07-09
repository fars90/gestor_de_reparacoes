from cliente import criar_tabela_clientes, adicionar_cliente, listar_clientes
from equipamento import criar_tabela_equipamentos, adicionar_equipamento, listar_equipamentos, atualizar_estado_equipamento

def menu():
    criar_tabela_clientes()
    criar_tabela_equipamentos()
    while True:
        print("\nMENU CLIENTES")
        print("1 - Adicionar cliente")
        print("2 - Listar clientes")
        print("3 - Adicionar Equipamento")
        print("4 - Listar Equipamentos")
        print("5 - Atualizar Estado Equipamento")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            adicionar_equipamento()
        elif opcao == "4":
            listar_equipamentos()
        elif opcao == "5":
            atualizar_estado_equipamento()
        elif opcao == "0":
            print("A sair do programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()