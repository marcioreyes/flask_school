from flask import Flask, template_render, flash

app = Flask.app()

@app.route('/index')
def index():
    return template_render('index.html')