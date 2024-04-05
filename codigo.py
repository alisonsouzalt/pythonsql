

#Antes de conectar ao banco digite no terminal: pip install mysql-connector-python

import mysql.connector

conexao = mysql.connector.connect(
    host= 'localhost', #coloque o nome do host
    user='root', #usuário do banco de dados
    password='1234', #senha do banco de dados
    database='projetoalfa' #nome do banco de dados

)

cursor = conexao.cursor()

#(Nessa parte se inicia o projeto onde tem o objetivo de adiconar, ler, editar ou deletar dados de um banco de dados atravez do python).

# cursor.execute(comando)
# conexao.commit() - quando edita o banco de dados
# resultado = cursor.fetchall() - lendo o banco de dados


#------------------------------------------
    

banco = 1

while banco ==1:
    
#------------------------------------------
    
#CREATE
    print("1. Cadastro de produtos")
    print("2. Consulta de Cadastro") 
    print("3. Update de Cadastros") 
    print("4. Deletar Cadastros") 
    escolha = int(input("Escolha uma opcao acima: "))
    if escolha == 1:
        nome_produto = input("Digite o nome do Produto: ")
        valor = int(input("Digite o valor do produto: "))
        comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
        cursor.execute(comando)
        conexao.commit()
        
        print('Produto Adicionado!')

#------------------------------------------

#READ
    if escolha == 2:
        comando = f'SELECT * FROM vendas'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(resultado)
        print('Busca concluida!')

#------------------------------------------

#UPDATE
    if escolha == 3:
        nome_produto = input("Digite o nome do produto: ")
        valor = int(input("Digite o novo valor: "))
        comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
        cursor.execute(comando)
        conexao.commit()
        print('Update Concluido!')
        
#DELETE
    if escolha == 4:
        nome_produto = input("Digite o nome do produto: ")
        comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
        cursor.execute(comando)
        conexao.commit()
        print('Produto deletado!')
    
    else:
        print("Voce nao escolheu nenhuma das opcoes!")

cursor.close()
conexao.close()
