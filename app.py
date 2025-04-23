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

if __name__ == '__main__':
    app.run(debug=True)
