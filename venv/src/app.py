from flask import Flask, request, render_template, redirect, url_for, flash
from controller.presenca_controller import listar_presencas, upload_presenca
import os

app = Flask(__name__)

# Defina uma chave secreta
app.secret_key = 'AA2bd1c4d3!!!'  # Altere para uma chave única e segura

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return upload_presenca()  # Chame a função para processar o upload

    # Para o método GET, exibe a lista de presenças
    presencas = listar_presencas()  # Função que busca as presenças no banco
    return render_template('index.html', presencas=presencas)

if __name__ == '__main__':
    app.run(debug=True)