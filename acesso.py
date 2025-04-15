import pymysql

# Conexão com o banco de dados
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='bancodedadosatualizado',
)

cursor = conexao.cursor()

# Listar todos os funcionários
print('LISTA DE FUNCIONÁRIOS: ')
cursor = conexao.cursor()
comando = 'SELECT * FROM FUNCIONARIOS'
cursor.execute(comando)
resultado = cursor.fetchall()  # Mostra os resultados
print(resultado)

Registro=input('Digite seu registro de funcionário: ')
cargo= input('Digite seu cargo: ')

if resultado:
    print('Acesso liberado!')
else:
    print('Acesso negado!')
    conexao.close()
    exit()

# Perguntar se deseja cadastrar novo funcionário
opcao = input("Deseja cadastrar um novo funcionário? (s/n): ").lower()

if opcao == 's':
    print('\nADICIONAR DADOS DO NOVO FUNCIONÁRIO:')
    registro = int(input('Digite o registro do funcionário: '))
    nome = input('Digite o nome do funcionário: ')
    cargo = input('Digite o cargo do funcionário: ')
    data_admissao = input('Digite a data de admissão (YYYY-MM-DD): ')

    comando = '''
    INSERT INTO FUNCIONARIOS (Registro, Nome, Cargo, Data_admissao)
    VALUES (%s, %s, %s, %s)
    '''
    cursor.execute(comando, (registro, nome, cargo, data_admissao))
    conexao.commit()
    print(f"Funcionário {nome} inserido com sucesso!")
else:
    print("Continuando sem cadastrar novo funcionário...")

# Excluir funcionário
print("\nEXCLUIR FUNCIONÁRIO:")
registro_excluir = int(input('Digite o registro do funcionário a ser excluído: '))
cursor.execute('DELETE FROM FUNCIONARIOS WHERE Registro = %s', (registro_excluir,))
conexao.commit()
print(f"Funcionário com registro {registro_excluir} excluído com sucesso.")

# Listar produtos
print('\nPRODUTOS EM ESTOQUE:')
cursor.execute('SELECT * FROM PRODUTOS')
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)

# Adicionar novo produto
print('\nADICIONAR NOVO PRODUTO:')
id_produto = int(input('ID do produto: '))
nome_prod = input('Nome do produto: ')
marca = input('Marca: ')
modelo = input('Modelo: ')
medida = input('Medida: ')
tipo = input('Tipo: ')
qnt_atual = int(input('Quantidade atual: '))
qnt_min = int(input('Quantidade mínima: '))
qnt_repor = int(input('Quantidade para repor: '))
valor_custo = float(input('Valor de custo: '))
valor_venda = float(input('Valor de venda: '))

comando = '''
INSERT INTO PRODUTOS 
(id_produto, Nome, Marca, Modelo, Medida, Tipo, Qnt_atual, Qnt_min, Qnt_Repor, Valor_Custo, Valor_venda)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''
valores = (id_produto, nome_prod, marca, modelo, medida, tipo, qnt_atual, qnt_min, qnt_repor, valor_custo, valor_venda)
cursor.execute(comando, valores)
conexao.commit()
print(f"Produto {nome_prod} inserido com sucesso!")

# Atualizar valor de venda
print("\nALTERAR VALOR DE VENDA:")
id_atualizar = int(input("Digite o ID do produto: "))
novo_valor = float(input("Novo valor de venda: "))
cursor.execute('UPDATE PRODUTOS SET Valor_venda = %s WHERE id_produto = %s', (novo_valor, id_atualizar))
conexao.commit()
print("Valor atualizado com sucesso.")

# Excluir produto
print("\nEXCLUIR PRODUTO:")
id_excluir = int(input('Digite o ID do produto: '))
cursor.execute('DELETE FROM PRODUTOS WHERE id_produto = %s', (id_excluir,))
conexao.commit()
print(f"Produto com ID {id_excluir} excluído com sucesso.")

# Encerrar conexão
cursor.close()
conexao.close()