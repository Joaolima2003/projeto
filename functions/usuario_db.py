
def cadastrar(conexao,nome,email_usuario,senha_usuario,telefone,rua,numero,bairro):

    cursor = conexao.cursor()

    sql = f'INSERT INTO usuarios(usuario_name, usuario_email,usuario_senha,usuario_telefone,usuario_rua,usuario_numero,usuario_bairro) VALUES (?, ? , ?, ?, ?, ? , ?)'
    cursor.execute(sql, [nome, email_usuario,senha_usuario,telefone,rua,numero,bairro])
    conexao.commit()
    
    return True

def login(conexao,email,senha):
    cursor = conexao.cursor()
    sql = 'select * from usuarios WHERE usuario_email=? and usuario_senha=?'
    cursor.execute(sql, [
        email, senha
    ])
    return cursor.fetchall()

def usuario_atualizar(conexao,usuario_novo,id):
    sql = 'UPDATE usuarios SET usuario_name=? WHERE usuario_id=?'
    cursor = conexao.cursor()
    cursor.execute(sql, [usuario_novo, id])
    conexao.commit()



   