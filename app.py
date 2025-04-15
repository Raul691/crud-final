from flask import Flask, request, render_template, redirect
import pymysql

app = Flask(__name__)

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
        return f"Acesso liberado para {resultado[1]}!"
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
