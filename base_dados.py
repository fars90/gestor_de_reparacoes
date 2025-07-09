import mysql.connector
from mysql.connector import Error

DB_NAME = "assistencia"

def criar_base_dados(cursor):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

def ligar_bd():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        cursor = conn.cursor()
        criar_base_dados(cursor)
        cursor.close()
        conn.close()

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
