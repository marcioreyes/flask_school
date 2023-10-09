from flask import Flask, render_template, request, flash
import random

app = Flask(__name__)
app.secretkey = "mrproductions"

@app.route('/')
def index():
    #TESTE DE ENVIO DE VALORES PARA O HTML
    s_abc = [random.random() for _ in range(40)]
    return render_template('index.html', s_abc=s_abc)

@app.route('/perfil')
def perfil():
    ...

@app.route('/completar')
def completar():
    return render_template('index.html', methods=['POST', 'GET'])

@app.route('/traduzir')
def traduzir():
    return render_template('traduzir.html', methods=['POST', 'GET'])

@app.route('/ouvir')
def ouvir():
    ...

@app.route('/contato', methods=['POST', 'GET'])
def contato():
    return render_template("contato.html")

@app.route('/testes', methods=['POST','GET'])
def testes():
    return render_template("testes.html")