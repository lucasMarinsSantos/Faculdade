from PIL import Image
import pytesseract
import os

# Se necessário, defina o caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Altere conforme necessário

# Carregue a imagem
imagem_path = r'C:\Users\Manhã\Desktop\Faculdade\Portifólio\Fontes\font1.png'
imagem = Image.open(imagem_path)

# Pré-processamento: converter para escala de cinza
imagem = imagem.convert('L')

# Aplicar binarização (opcional)
imagem = imagem.point(lambda x: 0 if x < 128 else 255, '1')

# Use pytesseract para extrair texto
texto = pytesseract.image_to_string(imagem)

# Exiba o texto extraído
print("Texto extraído:")
print(texto)

# Salvar o texto extraído no mesmo diretório da imagem
diretorio = os.path.dirname(imagem_path)  # Obtém o diretório da imagem
arquivo_texto_path = os.path.join(diretorio, 'texto_extraido.txt')  # Cria o caminho para o arquivo de texto

with open(arquivo_texto_path, 'w', encoding='utf-8') as arquivo:
    arquivo.write(texto)

print(f"Texto salvo em '{arquivo_texto_path}'")
