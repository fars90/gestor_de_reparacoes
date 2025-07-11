import sys
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
    autenticar_tecnico,
    apagar_tecnico
)

def iniciar_sessao():
    criar_tabela_tecnicos()
    while True:
        print("\n🔐 AUTENTICAÇÃO")
        print("1 - Login")
        print("2 - Registar Primeiro Técnico")
        print("0 - Sair")
        escolha = input("Escolha: ")
        if escolha == "1":
            user, is_admin = autenticar_tecnico()
            if user:
                return user, is_admin
        elif escolha == "2":
            registrar_tecnico(current_is_admin=False)
        elif escolha == "0":
            sys.exit("👋 Programa terminado.")
        else:
            print("❌ Opção inválida.")

def menu_principal(current_user, is_admin):
    criar_tabela_clientes()
    criar_tabela_equipamentos()

    while True:
        print(f"\n📋 MENU PRINCIPAL (User: {current_user}{' - Admin' if is_admin else ''})")
        print("1 - Adicionar cliente")
        print("2 - Listar clientes")
        print("3 - Adicionar equipamento")
        print("4 - Listar equipamentos")
        print("5 - Atualizar estado de equipamento")
        print("6 - Gerar relatório")
        if is_admin:
            print("7 - Registar novo técnico")
            print("8 - Apagar técnico")
        print("9 - Logout")
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
        elif opcao == "7" and is_admin:
            registrar_tecnico(current_is_admin=True)
        elif opcao == "8" and is_admin:
            apagar_tecnico(current_user, current_is_admin=is_admin)
        elif opcao == "9":
            print("🔄 Logout efetuado.")
            return  # volta ao menu de autenticação
        elif opcao == "0":
            sys.exit("👋 Programa terminado.")
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    while True:
        user, admin = iniciar_sessao()
        menu_principal(user, admin)
