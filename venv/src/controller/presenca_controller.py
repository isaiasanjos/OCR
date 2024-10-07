from flask import request, redirect, render_template, flash
from model.presenca_model import Presenca
from database.config import SessionLocal
import pytesseract
from PIL import Image
import re

# Defina o caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # ajuste o caminho conforme necessário

def upload_presenca():
    if request.method == 'POST':
        image = request.files['imagem']
        img = Image.open(image)
        
        # Processar OCR na imagem
        texto = pytesseract.image_to_string(img)
        
        # Imprimir texto extraído para verificação
        print("Texto extraído:", texto)
        
        # Suponha que o OCR devolva algo como: "João, Presente\nMaria, Ausente"
        linhas = texto.splitlines()

        # A seguir, você precisa garantir que a sessão do banco de dados está sendo criada corretamente
        db = SessionLocal()  # Inicie a sessão do banco de dados
        
        for linha in linhas:
            # Adicione um tratamento para ignorar linhas vazias ou mal formatadas
            if ',' in linha:
                nome, data, presenca = linha.split(',')
                nova_presenca = Presenca(nome_aluno=nome.strip(), data_presenca=data,presenca=presenca.strip())
                db.add(nova_presenca)  # Adiciona a nova presença à sessão
        
        print(f"Número de presenças a serem adicionadas: {len(linhas)}")
        db.commit()  # Salva as alterações no banco
        db.close()  # Fecha a sessão do banco de dados
        
        print("Presenças salvas no banco de dados.")  # Confirma que as presenças foram salvas
        return redirect('/')  # Redireciona para a página principal

    return render_template('index.html')

def listar_presencas():
    db = SessionLocal()
    presencas = db.query(Presenca).all()
    print("Presenças recuperadas do banco de dados:", presencas)  # Adicione esta linha
    db.close()
    
    return presencas
    
    return presencas  # Retorne a lista de presenças, não o template

# Função index para gerenciar a rota principal
def index():
    # Obter a lista de presenças para exibir na página
    presencas = listar_presencas()
    return presencas
