import mysql.connector
import hashlib
import getpass
from mysql.connector import Error
from base_dados import ligar_bd

def criar_tabela_tecnicos():
    conn = ligar_bd()
    if not conn:
        print("❌ Erro ao conectar à base de dados.")
        return
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS utilizadores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(64) NOT NULL,
            is_admin TINYINT(1) NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password: str) -> str:
    """Gera hash SHA-256 da password."""
    return hashlib.sha256(password.encode()).hexdigest()

def registrar_tecnico(current_is_admin=False):
    conn = ligar_bd()
    if not conn:
        print("❌ Não foi possível conectar à base de dados.")
        return

    cursor = conn.cursor()
    # Verifica quantos utilizadores já existem
    cursor.execute("SELECT COUNT(*) FROM utilizadores")
    (count,) = cursor.fetchone()

    # Se já existe alguém e quem tenta não é admin, nega
    if count > 0 and not current_is_admin:
        print("❌ Sem permissão para registar novos técnicos.")
        conn.close()
        return

    # Quem regista o primeiro utilizador fica admin
    is_admin = 1 if count == 0 else 0

    print("\n🔹 Registar Novo Técnico")
    username = input("Username: ").strip()
    senha = getpass.getpass("Password: ")
    senha_conf = getpass.getpass("Confirmar Password: ")
    if senha != senha_conf:
        print("❌ As passwords não coincidem.")
        conn.close()
        return

    password_hash = hash_password(senha)
    try:
        cursor.execute(
            "INSERT INTO utilizadores (username, password_hash, is_admin) VALUES (%s, %s, %s)",
            (username, password_hash, is_admin)
        )
        conn.commit()
        role = "Admin" if is_admin else "Técnico"
        print(f"✅ {role} registado com sucesso.")
    except Error as err:
        print(f"❌ Erro ao registar técnico: {err}")
    finally:
        conn.close()

def autenticar_tecnico():
    conn = ligar_bd()
    if not conn:
        print("❌ Não foi possível conectar à base de dados.")
        return None, False

    print("\n🔹 Login de Técnico")
    username = input("Username: ").strip()
    senha = getpass.getpass("Password: ")
    password_hash = hash_password(senha)

    cursor = conn.cursor()
    cursor.execute(
        "SELECT password_hash, is_admin FROM utilizadores WHERE username = %s",
        (username,)
    )
    row = cursor.fetchone()
    conn.close()

    if row and row[0] == password_hash:
        is_admin = bool(row[1])
        print(f"✅ Bem-vindo, {username}! {'(Admin)' if is_admin else ''}")
        return username, is_admin
    else:
        print("❌ Username ou password incorretos.")
        return None, False

def apagar_tecnico(current_username, current_is_admin):
    if not current_is_admin:
        print("❌ Sem permissão para apagar técnicos.")
        return

    print("\n🔹 Apagar Técnico")
    alvo = input("Username do técnico a apagar: ").strip()
    if alvo == current_username:
        print("❌ Não podes apagar o teu próprio utilizador.")
        return

    conn = ligar_bd()
    if not conn:
        print("❌ Erro ao conectar à base de dados.")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM utilizadores WHERE username = %s", (alvo,))
    (count,) = cursor.fetchone()
    if count == 0:
        print(f"❌ Técnico '{alvo}' não encontrado.")
        conn.close()
        return

    cursor.execute("DELETE FROM utilizadores WHERE username = %s", (alvo,))
    conn.commit()
    conn.close()
    print(f"✅ Técnico '{alvo}' apagado com sucesso.")
