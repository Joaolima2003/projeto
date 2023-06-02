import sqlite3
from functions.usuario_db import cadastrar, login, usuario_atualizar
from menuprincipal import menu_cliente
conn = sqlite3.connect('aula_database') 
c = conn.cursor()
  
opc = 0

# Menu de Cadastro
def main():
    global opc 
    while opc != 3:
        print('1 - Cadastrar\n2 - Logar\n3 - Sair')
        opc = int(input('Qual sua opção:'))

        if opc == 1:
            nome = str(input('Nome:'))
            email_usuario = str(input('Email:'))
            senha_usuario = str(input('Senha:'))
            telefone = (input('Contato:'))
            rua = str(input('Rua:'))
            numero = int (input('Numero:'))
            bairro = str(input('Bairro:'))
            cadastrar(conn,nome,email_usuario,senha_usuario,telefone,rua,numero,bairro)

        elif opc == 2:
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            usuario_autenticado = login(conn, 
                                             email,                         senha)
            if len(usuario_autenticado) > 0:
                print('Entrou no Sistema!!')
                menu_cliente(usuario_autenticado[0][0])
            else:
                print('Usuário ou Senha Inválidos!!')

        elif opc == 3:
            break
        
        else:
            print('Opção inválida')           

# Menu de Exibição de Itens
main()