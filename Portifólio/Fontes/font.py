from PIL import Image
import os

# Caminho das imagens e pastas de saída
image_paths = [
    r'C:\Users\Manhã\Desktop\Faculdade\Portifólio\Fontes\font1.png',  # Altere para suas imagens reais
    r'C:\Users\Manhã\Desktop\Faculdade\Portifólio\Fontes\font2.png'   # Segunda imagem
]
output_dirs = [
    r'C:\Users\Manhã\Desktop\Faculdade\Portifólio\Fontes_caracteres_1',
    r'C:\Users\Manhã\Desktop\Faculdade\Portifólio\Fontes_caracteres_2'
]

# Dimensões ajustadas para uma imagem de 2048x2048 com 16 colunas e 13 linhas
caracter_largura = 2048 // 15  # largura de cada caractere
caracter_altura = 2048 // 13   # altura de cada caractere

# Adicionar um deslocamento para centralizar melhor os caracteres
deslocamento_horizontal = 0  # Ajuste conforme necessário

# Função para processar cada imagem
def process_image(image_path, output_dir):
    # Criar a pasta de saída, se não existir
    os.makedirs(output_dir, exist_ok=True)

    # Carregar a imagem
    image = Image.open(image_path)

    # Definir o número de linhas e colunas com base na imagem (16 colunas e 13 linhas)
    num_colunas = 16
    num_linhas = 13

    # Contador para nomear os arquivos
    contador = 0

    # Percorrer cada caractere e salvar como arquivo separado
    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            # Definir a área de corte para o caractere
            x_inicio = (coluna * caracter_largura) + deslocamento_horizontal
            y_inicio = linha * caracter_altura
            x_fim = x_inicio + caracter_largura - (2 * deslocamento_horizontal)  # Ajuste de margem na direita também
            box = (x_inicio, y_inicio, x_fim, y_inicio + caracter_altura)

            # Recortar o caractere da imagem
            caractere = image.crop(box)

            # Salvar o caractere em um arquivo PNG
            caractere.save(f"{output_dir}/caractere_{contador}.png")
            contador += 1

    print(f"Caracteres foram salvos na pasta: {output_dir}")

# Processar cada imagem com suas respectivas pastas de saída
for image_path, output_dir in zip(image_paths, output_dirs):
    process_image(image_path, output_dir)
