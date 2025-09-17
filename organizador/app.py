from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="2580",
        database="organizador"
    )

@app.route('/')
def index():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    return render_template('index.html', tarefas=tarefas)

@app.route('/adicionarTarefa', methods=['POST'])
def adicionar_tarefa():
    disciplina = request.form['disciplina']
    tarefa = request.form['tarefa']
    data = request.form['data']

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (disciplina, tarefa, data_entrega) VALUES (%s, %s, %s)",
                   (disciplina, tarefa, data))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
