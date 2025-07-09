from base_dados import ligar_bd
from cliente import listar_clientes

def criar_tabela_equipamentos():
    conn = ligar_bd()
    if not conn:
        print("Não foi possível conectar à base de dados.")
        return

    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipamentos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            cliente_id INT NOT NULL,
            tipo VARCHAR(100),
            marca VARCHAR(100),
            modelo VARCHAR(100),
            descricao_problema TEXT,
            estado VARCHAR(20) DEFAULT 'Recebido',
            data_entrada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    """)
    conn.commit()
    conn.close()

def adicionar_equipamento():
    print("\n🔹 Adicionar Equipamento")
    listar_clientes()
    try:
        cliente_id = int(input("ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return

    tipo = input("Tipo de equipamento: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    descricao = input("Descrição do problema: ")

    conn = ligar_bd()
    if not conn:
        print("Não foi possível adicionar o equipamento.")
        return

    cursor = conn.cursor()
    sql = """
        INSERT INTO equipamentos 
        (cliente_id, tipo, marca, modelo, descricao_problema) 
        VALUES (%s, %s, %s, %s, %s)
    """
    valores = (cliente_id, tipo, marca, modelo, descricao)
    cursor.execute(sql, valores)
    conn.commit()
    conn.close()
    print("Equipamento registado com sucesso.")

def listar_equipamentos():
    conn = ligar_bd()
    if not conn:
        print("Erro ao conectar à base de dados.")
        return

    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.id, c.nome, e.tipo, e.marca, e.modelo, e.estado, e.data_entrada
        FROM equipamentos e
        JOIN clientes c ON e.cliente_id = c.id
        ORDER BY e.data_entrada DESC
    """)
    resultados = cursor.fetchall()
    if resultados:
        print("\nLista de Equipamentos:")
        for (eid, cliente, tipo, marca, modelo, estado, data) in resultados:
            print(f"[{eid}] {tipo} {marca} {modelo} | Cliente: {cliente} | Estado: {estado} | Entrada: {data}")
    else:
        print("Nenhum equipamento encontrado.")
    conn.close()
