from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Conexão com o banco
def obter_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sofia1211",
        database="tcc_almoxarifado",
        port=3306
    )

@app.route('/inicio')
def home():
    conexao = obter_conexao()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM produtos")
    produtos_do_banco = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template('home.html', produtos=produtos_do_banco)

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')
#   Cadastro nao oficial
@app.route('/cadastrar_produto', methods=['POST'])
def cadastrar_produto():
    nome = request.form.get('nome')
    quantidade = request.form.get('quantidade')
    descricao = request.form.get('descricao')

    conexao = obter_conexao()
    cursor = conexao.cursor()

    comando = """
        INSERT INTO produtos (nome, quantidade, descricao)
        VALUES (%s, %s, %s)
    """
    cursor.execute(comando, (nome, quantidade, descricao))

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect(url_for('estoque'))

if __name__ == '__main__':
    app.run(debug=True)