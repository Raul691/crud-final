from flask import Flask, request, render_template, redirect, session, url_for
import pymysql

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'


def conectar_bd():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='bancodedadosatualizado',
    )

@app.route('/')
def index():
    return render_template('login.html')  # Página de login

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')  # Página de cadastro

@app.route('/login', methods=['POST'])
def login():
    registro = request.form['registro']
    cargo = request.form['cargo']

    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM FUNCIONARIOS WHERE Registro=%s AND Cargo=%s", (registro, cargo))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        session['nome'] = resultado[1]  # Armazena o nome do funcionário na sessão
        return redirect('/index')  # Redireciona para a página inicial
    else:
        return redirect(url_for('acesso_negado'))

@app.route('/acesso-negado')
def acesso_negado():
    return render_template('acesso_negado.html')  # Página de acesso negado

@app.route('/cadastrar-funcionario', methods=['POST'])
def cadastrar_funcionario():
    registro = request.form['registro']
    nome = request.form['nome']
    cargo = request.form['cargo']
    data = request.form['data']

    conexao = conectar_bd()
    cursor = conexao.cursor()
    comando = '''
    INSERT INTO FUNCIONARIOS (Registro, Nome, Cargo, Data_admissao)
    VALUES (%s, %s, %s, %s)
    '''
    cursor.execute(comando, (registro, nome, cargo, data))
    conexao.commit()
    cursor.close()
    conexao.close()
    session['nome'] = nome
    return redirect('/index')  

@app.route('/index')
def index_page():
    if 'nome' not in session:  # Verifica se o usuário está logado
        return redirect('/')  # Redireciona para a página de login
    nome = session['nome']  # Obtém o nome do usuário da sessão
    return render_template('index.html', nome=nome)


@app.route('/estoque')
def estoque():
    if 'nome' not in session:
           return redirect('/')
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM PRODUTOS")
    produtos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('estoque.html', produtos=produtos)

@app.route('/editar_produto/<int:id_produto>')
def editar_produto(id_produto):
    if 'nome' not in session:
        return redirect('/')
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM PRODUTOS WHERE id_produto=%s", (id_produto,))
    produto = cursor.fetchone()
    cursor.close()
    conexao.close()
    if produto:
        return render_template('editar_produto.html', produto=produto)
    else:
        return "Produto não encontrado." # Ou uma página de erro

@app.route('/atualizar_produto/<int:id_produto>', methods=['POST'])
def atualizar_produto(id_produto):
    if 'nome' not in session:
        return redirect('/')
    nome = request.form['nome']
    marca = request.form['marca']
    modelo = request.form['modelo']
    medida = request.form['medida']
    tipo = request.form['tipo']
    qnt_atual = request.form['qnt_atual']
    qnt_min = request.form['qnt_min']
    qnt_repor = request.form['qnt_repor']
    valor_custo = request.form['valor_custo']
    valor_venda = request.form['valor_venda']

    conexao = conectar_bd()
    cursor = conexao.cursor()
    comando = '''
    UPDATE PRODUTOS
    SET Nome=%s, Marca=%s, Modelo=%s, Medida=%s, Tipo=%s,
        Qnt_atual=%s, Qnt_min=%s, Qnt_Repor=%s, Valor_Custo=%s, Valor_Venda=%s
    WHERE id_produto=%s
    '''
    cursor.execute(comando, (nome, marca, modelo, medida, tipo, qnt_atual, qnt_min, qnt_repor, valor_custo, valor_venda, id_produto))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/estoque')

@app.route('/excluir_produto/<int:id_produto>')
def excluir_produto(id_produto):
    if 'nome' not in session:
        return redirect('/')
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM PRODUTOS WHERE id_produto=%s", (id_produto,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/estoque')

@app.route('/adicionar_produto')
def adicionar_produto():
    if 'nome' not in session:
        return redirect('/')
    return render_template('adicionar_produto.html')

@app.route('/salvar_produto', methods=['POST'])
def salvar_produto():
    if 'nome' not in session:
        return redirect('/')
    id_produto = request.form['id_produto']
    nome = request.form['nome']
    marca = request.form['marca']
    modelo = request.form['modelo']
    medida = request.form['medida']
    tipo = request.form['tipo']
    qnt_atual = request.form['qnt_atual']
    qnt_min = request.form['qnt_min']
    qnt_repor = request.form['qnt_repor']
    valor_custo = request.form['valor_custo']
    valor_venda = request.form['valor_venda']

    conexao = conectar_bd()
    cursor = conexao.cursor()

    # Verifica se já existe um produto com o mesmo ID
    cursor.execute("SELECT id_produto FROM PRODUTOS WHERE id_produto = %s", (id_produto,))
    resultado = cursor.fetchone()

    if resultado:
        mensagem_erro = "Erro: Já existe um produto com este ID."
        cursor.close()
        conexao.close()
        return render_template('adicionar_produto.html', mensagem_erro=mensagem_erro,
                               nome=nome, marca=marca, modelo=modelo, medida=medida, tipo=tipo,
                               qnt_atual=qnt_atual, qnt_min=qnt_min, qnt_repor=qnt_repor,
                               valor_custo=valor_custo, valor_venda=valor_venda)
    else:
        comando = '''
        INSERT INTO PRODUTOS (id_produto, Nome, Marca, Modelo, Medida, Tipo, Qnt_atual, Qnt_min, Qnt_Repor, Valor_Custo, Valor_Venda)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(comando, (id_produto, nome, marca, modelo, medida, tipo, qnt_atual, qnt_min, qnt_repor, valor_custo, valor_venda))
        conexao.commit()
        cursor.close()
        conexao.close()
        session['mensagem'] = 'Produto adicionado com sucesso!'
        return redirect('/estoque')
    
@app.route('/pesquisar_estoque', methods=['GET'])
def pesquisar_estoque():
    if 'nome' not in session:
        return redirect('/')
    termo_pesquisa = request.args.get('termo_pesquisa')
    conexao = conectar_bd()
    cursor = conexao.cursor()
    comando = """
    SELECT * FROM PRODUTOS
    WHERE Nome LIKE %s OR Marca LIKE %s OR Modelo LIKE %s
    """
    termo_like = f"%{termo_pesquisa}%"
    cursor.execute(comando, (termo_like, termo_like, termo_like))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('estoque.html', produtos=resultados)
    
if __name__ == '__main__':
    app.run(debug=True)
