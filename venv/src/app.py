from flask import Flask, render_template, request, redirect, url_for
import pytesseract
from PIL import Image
import os

app = Flask(__name__)

# Defina o caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # ajuste o caminho conforme necessário

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ocr')
def ocr_page():
    return render_template('ocr.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'imagem' not in request.files:
        return redirect(url_for('ocr_page'))

    imagem = request.files['imagem']

    if imagem.filename == '':
        return redirect(url_for('ocr_page'))

    if imagem:
        caminho_imagem = os.path.join('uploads', imagem.filename)
        imagem.save(caminho_imagem)

        # Processar a imagem com OCR
        img = Image.open(caminho_imagem)
        texto_extraido = pytesseract.image_to_string(img)

        # Imprimir o texto extraído para verificar a estrutura
        print("Texto extraído:", texto_extraido)

        # Agora, vamos processar o texto extraído
        linhas = texto_extraido.splitlines()  # Dividir o texto por linha
        ocr_data = []

        for linha in linhas:
            if ',' in linha:  # Assumindo que os campos estão separados por vírgula
                try:
                    nome, data, presenca = linha.split(',')  # Separar os valores por vírgula
                    ocr_data.append({
                        'nome': nome.strip(),
                        'data': data.strip(),
                        'presenca': presenca.strip()
                    })
                except ValueError:
                    # Ignorar linhas que não tenham 3 valores separados por vírgula
                    print(f"Linha ignorada: {linha}")
        
        # Renderizar a página com os dados extraídos e formatados
        return render_template('ocr.html', ocr_data=ocr_data)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.secret_key = 'chave_secreta'
    app.run(debug=True)
