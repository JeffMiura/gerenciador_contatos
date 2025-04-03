from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Conexão com o banco de dados
def get_db_connection():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Buch_159753',
        database='gerenciador_contatos'
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    nome = request.form['nome']
    email = request.form['email']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contatos (nome, email) VALUES (%s, %s)', (nome, email))
    conn.commit()
    cursor.close()
    conn.close()
    return 'Contato adicionado com sucesso!'

@app.route('/edit_contact', methods=['POST'])
def edit_contact():
    contato_id = request.form['id']
    novo_nome = request.form['novo_nome']
    novo_email = request.form['novo_email']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE contatos SET nome = %s, email = %s WHERE id = %s', (novo_nome, novo_email, contato_id))
    conn.commit()
    cursor.close()
    conn.close()
    return 'Contato editado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
