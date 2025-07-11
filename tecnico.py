import mysql.connector
import hashlib
import getpass
from base_dados import ligar_bd

def criar_tabela_tecnicos():
    conn = ligar_bd()
    if not conn:
        print("Erro ao conectar à base de dados.")
        return
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS utilizadores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(64) NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password: str) -> str:
    """Gera hash SHA-256 da password."""
    return hashlib.sha256(password.encode()).hexdigest()

def registrar_tecnico():
    print("\nRegistar Novo Técnico")
    username = input("Username: ").strip()
    senha = getpass.getpass("Password: ")
    senha_conf = getpass.getpass("Confirmar Password: ")
    if senha != senha_conf:
        print("As passwords não coincidem.")
        return

    password_hash = hash_password(senha)
    conn = ligar_bd()
    if not conn:
        print("Não foi possível conectar à base de dados.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO utilizadores (username, password_hash) VALUES (%s, %s)",
            (username, password_hash)
        )
        conn.commit()
        print("Técnico registado com sucesso.")
    except mysql.connector.Error as err:
        print(f"Erro ao registar técnico: {err}")
    finally:
        conn.close()

def autenticar_tecnico() -> bool:
    print("\nLogin de Técnico")
    username = input("Username: ").strip()
    senha = getpass.getpass("Password: ")
    password_hash = hash_password(senha)

    conn = ligar_bd()
    if not conn:
        print("Não foi possível conectar à base de dados.")
        return False

    cursor = conn.cursor()
    cursor.execute(
        "SELECT password_hash FROM utilizadores WHERE username = %s",
        (username,)
    )
    row = cursor.fetchone()
    conn.close()

    if row and row[0] == password_hash:
        print(f"Bem-vindo, {username}!")
        return True
    else:
        print("Username ou password incorretos.")
        return False
