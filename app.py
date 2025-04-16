from flask import Flask, request, render_template, redirect, session
import pymysql


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Adicione uma chave secreta para a sessão

def conectar_bd():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='bancodedadosatualizado',
    )

@app.route('/')
def index():
    return render_template('index.html')  # Página de login

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')  # Página de cadastro

@app.route('/inicio')
def inicio():
    nome = session.get('nome')  # Obtém o nome da sessão
    return render_template('inicio.html', nome=nome)  # Passa o nome para o template

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
        return redirect('/inicio')  # Redireciona para a página inicial
    else:
        return "Acesso negado!"

@app.route('/cadastrar-funcionario', methods=['POST'])
def cadastrar_funcionario():
    reg = request.form['reg']
    nome = request.form['nome']
    cargo = request.form['cargo']
    data = request.form['data']

    conexao = conectar_bd()
    cursor = conexao.cursor()
    comando = '''
    INSERT INTO FUNCIONARIOS (Registro, Nome, Cargo, Data_admissao)
    VALUES (%s, %s, %s, %s)
    '''
    cursor.execute(comando, (reg, nome, cargo, data))
    conexao.commit()
    cursor.close()
    conexao.close()

    return f"Funcionário {nome} cadastrado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
