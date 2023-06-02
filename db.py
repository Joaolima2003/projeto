import sqlite3

conn = sqlite3.connect('aula_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS usuarios(
            usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_name VARCHAR(100) NOT NULL UNIQUE,
            usuario_email VARCHAR(50) NOT NULL UNIQUE,
            usuario_senha VARCHAR(25),
            usuario_telefone VARCHAR(12),
            usuario_rua VARCHAR(100),
            usuario_numero INT,
            usuario_bairro VARCHAR(100)
          )
          ''')


c.execute('''
        CREATE TABLE produtos(
          produto_id INTEGER PRIMARY KEY AUTOINCREMENT,
          produto_nome VARCHAR(100) NOT NULL UNIQUE,
          produto_valor FLOAT,
          usuario_id INTEGER REFERENCES usuarios (usuario_id)


        )



''')


conn.commit()