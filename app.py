from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# definindo o modelo de dados


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tarefa = db.Column(db.String(100), unique=True, nullable=False)


@app.route('/')
def index():
    # leitura dos dados do banco
    tasks = Tasks.query.all()
    return render_template('index.html', tasks=tasks)

# inserção de dados no banco


@app.route('/create', methods=["POST"])
def cria_tarefa():
    tarefa = request.form['nome_tarefa'].strip()

    # verifica se já existe a tarefa
    existind_tarefa = Tasks.query.filter_by(tarefa=tarefa).first()
    if existind_tarefa:
        return redirect('/?mensagem=Tarefa já existe!')

    nova_tarefa = Tasks(tarefa=tarefa)
    db.session.add(nova_tarefa)
    db.session.commit()
    return redirect('/')

# deleta tarefa


@app.route('/delete/<int:tarefa_id>', methods=['POST'])
def deleta_tarefa(tarefa_id):
    tarefa = Tasks.query.get(tarefa_id)

    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
    return redirect('/')

# edição de tarefas


@app.route('/editar/<int:tarefa_id>', methods=['POST'])
def editar_tarefa(tarefa_id):
    tarefa = Tasks.query.get(tarefa_id)

    if tarefa:
        tarefa.tarefa = request.form['nome_tarefa'].strip()
        db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', debug=True, port=5153)
