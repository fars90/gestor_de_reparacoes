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
    print("\nAdicionar Equipamento")
    listar_clientes()
    try:
        cliente_id = int(input("ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return

    conn = ligar_bd()
    if not conn:
        print("Não foi possível conectar à base de dados.")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM clientes WHERE id = %s", (cliente_id,))
    (count,) = cursor.fetchone()
    if count == 0:
        print(f"Cliente com ID {cliente_id} não encontrado.")
        conn.close()
        return

    tipo = input("Tipo de equipamento: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    descricao = input("Descrição do problema: ")

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

def atualizar_estado_equipamento():
    listar_equipamentos()
    print("\nAtualizar Estado de Equipamento")
    try:
        equipamento_id = int(input("ID do equipamento: "))
    except ValueError:
        print("ID inválido.")
        return

    conn = ligar_bd()
    if not conn:
        print("Não foi possível conectar à base de dados.")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT estado FROM equipamentos WHERE id = %s", (equipamento_id,))
    resultado = cursor.fetchone()
    if not resultado:
        print(f"Equipamento com ID {equipamento_id} não encontrado.")
        conn.close()
        return

    estado_atual = resultado[0]
    print(f"Estado atual: {estado_atual}")
    novo_estado = input("Novo estado (Recebido / Em reparação / Pronto / Entregue): ").strip()

    sql = "UPDATE equipamentos SET estado = %s WHERE id = %s"
    cursor.execute(sql, (novo_estado, equipamento_id))
    conn.commit()
    conn.close()
    print(f"Estado do equipamento {equipamento_id} atualizado para '{novo_estado}'.")