import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash


# configuração
DATABASE = "blog.db" # ARQUIVO ONDE VAI SER GUARDADO O BANCO DE DADOS
SECRET_KEY = 'pudim' # incripta e desemcripta a comunicação

app = Flask(__name__)
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request # antes do request quero que faça
def antes_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def depois_request(exc):
    g.bd.close()


@app.route('/') # pagina principal
@app.route('/entradas')
def exibir_entradas():
    return render_template('exibir_entradas.html')

@app.route('/hello')
def pagina_inicial():
    return "Hello Word"



