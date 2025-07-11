from cliente import criar_tabela_clientes, adicionar_cliente, listar_clientes
from equipamento import (
    criar_tabela_equipamentos,
    adicionar_equipamento,
    listar_equipamentos,
    atualizar_estado_equipamento
)
from relatorios import gerar_relatorio
from tecnico import (
    criar_tabela_tecnicos,
    registrar_tecnico,
    autenticar_tecnico
)

def iniciar_sessao() -> bool:
    criar_tabela_tecnicos()
    while True:
        print("\n🔐 AUTENTICAÇÃO")
        print("1 - Login")
        print("2 - Registar Técnico")
        print("0 - Sair")
        escolha = input("Escolha: ")
        if escolha == "1":
            if autenticar_tecnico():
                return True
        elif escolha == "2":
            registrar_tecnico()
        elif escolha == "0":
            return False
        else:
            print("❌ Opção inválida.")

def menu_principal():
    criar_tabela_clientes()
    criar_tabela_equipamentos()

    while True:
        print("\n📋 MENU PRINCIPAL")
        print("1 - Adicionar cliente")
        print("2 - Listar clientes")
        print("3 - Adicionar equipamento")
        print("4 - Listar equipamentos")
        print("5 - Atualizar estado de equipamento")
        print("6 - Gerar relatório")
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
        elif opcao == "6":
            gerar_relatorio()
        elif opcao == "0":
            print("A sair do programa.")
            break
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    if iniciar_sessao():
        menu_principal()
    else:
        print("👋 Sessão terminada.") 
