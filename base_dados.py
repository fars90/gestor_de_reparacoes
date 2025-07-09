import mysql.connector
from mysql.connector import Error

DB_NAME = "assistencia"

def criar_base_dados(cursor):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

def ligar_bd():
    try:
        # Conexão inicial (sem base de dados)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        cursor = conn.cursor()
        criar_base_dados(cursor)
        cursor.close()
        conn.close()

        # Conexão com a base de dados
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database=DB_NAME
        )

        if conn.is_connected():
            print(f"Conexão à base de dados '{DB_NAME}' estabelecida com sucesso.")
        return conn

    except Error as erro:
        print(f"Erro ao conectar à base de dados: {erro}")
        return None
