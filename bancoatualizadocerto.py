import pymysql
# Conexão com o banco de dados
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='bancodedadosatualizado',  # Verifique o nome correto do seu banco de dados
)
cursor= conexao.cursor()

print('PRODUTOS EM ESTOQUE: ')
cursor = conexao.cursor()
comando = 'SELECT * FROM PRODUTOS'
cursor.execute(comando)
resultado = cursor.fetchall()  # Mostra os resultados
print(resultado)

# Adicionar novo produto
print('Adicionar novo produto em estoque: ')
id_produto = int(input('Digite o id do produto: '))
Nome = input('Digite o nome do produto: ')
Marca = input('Digite a marca do produto: ')
Modelo = input('Digite o modelo do produto: ')
Medida = input('Digite a medida do produto: ')
Tipo = input('Digite o tipo do produto: ')
Qnt_atual = int(input('Digite a quantidade atual do produto: '))
Qnt_min = int(input('Digite a quantidade mínima do produto: '))
Qnt_Repor = int(input('Digite a quantidade a se comprar desse produto: '))
Valor_Custo = float(input('Digite o valor de compra do produto: '))
Valor_venda = float(input('Digite o valor de venda do produto: '))

# Comando para inserir o novo produto
comando = '''
INSERT INTO PRODUTOS 
(id_produto, Nome, Marca, Modelo, Medida, Tipo, Qnt_atual, Qnt_min, Qnt_Repor, Valor_Custo, Valor_venda)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''
valores = (id_produto, Nome, Marca, Modelo, Medida, Tipo, Qnt_atual, Qnt_min, Qnt_Repor, Valor_Custo, Valor_venda)
cursor.execute(comando, valores)
conexao.commit()  # Confirma a inserção
print(f"Produto {id_produto} inserido com sucesso!")

# Alterar o valor de um produto
print("Alterar o valor de um produto")
id_produto = int(input("Digite o id do produto: "))
valor_de_venda = float(input("Digite o novo valor desse produto: "))
comando = 'UPDATE PRODUTOS SET Valor_venda = %s WHERE id_produto = %s'
cursor.execute(comando, (valor_de_venda, id_produto))
conexao.commit()
print("Valor do produto alterado com sucesso.")

# Excluir um produto do estoque
print("Excluir um produto do estoque")
id_produto = int(input('Digite o id do produto: '))
comando = 'DELETE FROM PRODUTOS WHERE id_produto = %s'
cursor.execute(comando, (id_produto,))
conexao.commit()
print(f"Produto com id {id_produto} excluído com sucesso.")

# Fechar a conexão
cursor.close()
conexao.close()