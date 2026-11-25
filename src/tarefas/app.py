from flask import Flask, redirect, render_template, request, url_for

from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa

app = Flask(__name__)

with app.app_context():
    init_db()

@app.route('/test')
def test():
    return 'Servidor Online!'

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa']
        data_conclusao_form = request.form['dataConclusao']

        data_corrigida = data_conclusao_form or None

        tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_corrigida)

        tarefa.salvarTarefa()

        return redirect(url_for('home'))

    tarefas= Tarefa.listarTarefas()

    return render_template(
        'base.html',
        titulo_da_pagina='Minha lista', 
        tarefas_da_pagina=tarefas,
        button_submit="Adicionar",
        botao_voltar="display: none",
    )

@app.route('/delete/<int:id>')
def apagar_id_especificado(id):
    Tarefa.apagarTarefa(id)
    
    return redirect('/')

@app.route('/edit/<int:id_tarefa>', methods=['GET', 'POST']) 
def editar_id_especificado(id_tarefa):

    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa']
        data_conclusao_form = request.form['dataConclusao']

        data_corrigida = data_conclusao_form or None

        tarefa = Tarefa(
            titulo=titulo_form,
            id=id_tarefa,
            data_conclusao=data_corrigida
        )

        tarefa.editarTarefas()

        return redirect(url_for('home'))
    return render_template(
        "base.html",
        titulo_da_pagina="Minha lista de tarefas",
        tarefas_da_pagina={"titulo_tarefa:": None, "data_conclusao": None},
        button_submit="Atualizar",
        lista="display: none",

    )
if __name__ == '__main__':

    app.run()