from flask import Flask, template_render, request, flash

app = Flask(__name__)
app.secretkey = "mrproductions"

@app.route('/index')
def index():
    return template_render('index.html')

@app.route('/perfil')
def perfil():
    ...

@app.route('/completar')
def completar():
    ...

@app.route('/traduzir')
def traduzir():
    ...

@app.route('/ouvir')
def ouvir():
    ...