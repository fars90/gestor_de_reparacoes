from base_dados import ligar_bd

def criar_tabela_clientes():
    conn = ligar_bd()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            telefone VARCHAR(20),
            email VARCHAR(100)
        )
    """)
    conn.commit()
    conn.close()

def adicionar_cliente(nome, telefone, email):
    conn = ligar_bd()
    cursor = conn.cursor()
    sql = "INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s)"
    valores = (nome, telefone, email)
    cursor.execute(sql, valores)
    conn.commit()
    conn.close()
    print("Cliente adicionado com sucesso.")

def listar_clientes():
    conn = ligar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    resultados = cursor.fetchall()
    if resultados:
        for (id, nome, telefone, email) in resultados:
            print(f"[{id}] {nome} | Tel: {telefone} | Email: {email}")
    else:
        print("Nenhum cliente encontrado.")
    conn.close()
