from base_dados import ligar_bd
import csv
from datetime import datetime

def gerar_relatorio():
    print("\nGeração de Relatórios")
    print("1 - Por cliente")
    print("2 - Por estado")
    print("3 - Por período")
    opcao = input("Escolha: ")

    if opcao == "1":
        cliente_id = input("ID do cliente: ")
        query = """
            SELECT e.id, c.nome, e.tipo, e.marca, e.modelo, e.estado, e.data_entrada
            FROM equipamentos e
            JOIN clientes c ON e.cliente_id = c.id
            WHERE c.id = %s
            ORDER BY e.data_entrada DESC
        """
        params = (cliente_id,)
        ficheiro = f"relatorio_cliente_{cliente_id}_{datetime.now():%Y%m%d%H%M%S}.csv"

    elif opcao == "2":
        estado = input("Estado (Recebido / Em reparação / Pronto / Entregue): ")
        query = """
            SELECT e.id, c.nome, e.tipo, e.marca, e.modelo, e.estado, e.data_entrada
            FROM equipamentos e
            JOIN clientes c ON e.cliente_id = c.id
            WHERE e.estado = %s
            ORDER BY e.data_entrada DESC
        """
        params = (estado,)
        ficheiro = f"relatorio_estado_{estado.replace(' ', '_')}_{datetime.now():%Y%m%d%H%M%S}.csv"

    elif opcao == "3":
        data_inicio = input("Data início (YYYY-MM-DD): ")
        data_fim    = input("Data fim (YYYY-MM-DD): ")
        query = """
            SELECT e.id, c.nome, e.tipo, e.marca, e.modelo, e.estado, e.data_entrada
            FROM equipamentos e
            JOIN clientes c ON e.cliente_id = c.id
            WHERE DATE(e.data_entrada) BETWEEN %s AND %s
            ORDER BY e.data_entrada DESC
        """
        params = (data_inicio, data_fim)
        ficheiro = f"relatorio_periodo_{data_inicio}_a_{data_fim}_{datetime.now():%Y%m%d%H%M%S}.csv"

    else:
        print("Opção inválida.")
        return

    conn = ligar_bd()
    if not conn:
        print("Não foi possível conectar à base de dados.")
        return

    cursor = conn.cursor()
    cursor.execute(query, params)
    resultados = cursor.fetchall()
    conn.close()

    if not resultados:
        print("Nenhum registo encontrado para os critérios fornecidos.")
        return

    colunas = ["ID", "Cliente", "Tipo", "Marca", "Modelo", "Estado", "Data Entrada"]
    print("\n" + " | ".join(colunas))
    print("-" * 80)
    for row in resultados:
        print(" | ".join(str(item) for item in row))

    exportar = input("\nDeseja exportar este relatório para CSV? (s/n): ").strip().lower()
    if exportar == 's':
        with open(ficheiro, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(colunas)
            writer.writerows(resultados)
        print(f"Relatório gravado em: {ficheiro}")
    else:
        print("Exportação cancelada. Nenhum ficheiro foi guardado.")