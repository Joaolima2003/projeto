import sqlite3
opc = 0
def menu_cliente(usuario_id):
    conn = sqlite3.connect('aula_database')
    c = conn.cursor()

    global opc
    while opc != 7:
        opc = int(input('QUAL OPÇÃO VOCÊ QUER. \n[1] - Atualizar produto\n[2] - Deletar itens\n[3] - Listar produtos cadastrados\n[4] - Inserir produto\n[5] - Atualizar usuário\n[6]-  Deletar usuário\n[7] - Sair\nEscolha a opção: '))
        if opc == 1:
            id = int(input('Digite o id:'))
            novo_nome_produto = str(input('Digite o nome do novo produto:'))
            valor_produto = float(input('Digite o novo valor do produto:'))
            atualizar_produto(conn,novo_nome_produto,valor_produto,id)
        elif opc == 2:
            id = int(input('Digite o id para deletar o produto:'))
            deletar(conn,id)
        elif opc == 3:
            produtos = listar_produto(conn)
            for produto in produtos:
                print(produto)
        elif opc == 4:
            produto_nome = str(input('Qual o nome do produto que vai ser inserido:'))
            produto_valor = float(input('Qual o valor do produto:'))
            inserir_produto(conn,produto_nome,produto_valor, usuario_id)
        elif opc == 5:
            id = int(input('Digite o id do usuário:'))
            usuario_novo = str(input('Digite o nome do novo usuário:'))
            usuario_atualizar(conn,usuario_novo,id) 
        elif opc == 6:
            id = int(input('Qual o id do usuário para deletar:'))
            usuario_deletar(conn,id)
        elif opc == 7:
            break
        else:
            print('Opção Inválida.')    









def deletar(conexao,id):
    sql = 'delete from produtos where produto_id=?'
    cursor = conexao.cursor()
    cursor.execute(sql, [id])
    conexao.commit()

def atualizar_produto(conexao, novo_nome_produto, valor_produto, id):
    sql = 'UPDATE produtos SET produto_nome=? , produto_valor=? WHERE produto_id=?'
    cursor = conexao.cursor()
    cursor.execute(sql, [novo_nome_produto, valor_produto, id])
    conexao.commit()

def listar_produto(conexao):
    cursor = conexao.cursor()
    sql = 'select * from produtos'
    cursor.execute(sql)
    return cursor.fetchall()    

def inserir_produto(conexao,produto_nome,produto_valor, usuario_id):
    cursor = conexao.cursor()
    sql = f'INSERT INTO produtos(produto_nome, produto_valor, usuario_id) VALUES (?, ?, ?)'
    cursor.execute(sql, [produto_nome, produto_valor, usuario_id])
    conexao.commit()
    
def usuario_atualizar(conexao,usuario_novo,id):
    sql = 'UPDATE usuarios SET usuario_name=? WHERE usuario_id=?'
    cursor = conexao.cursor()
    cursor.execute(sql, [usuario_novo, id])
    conexao.commit()

def usuario_deletar(conexao,id):
    sql = 'delete from usuarios where usuario_id=?'
    cursor = conexao.cursor()
    cursor.execute(sql, [id])
    conexao.commit()    