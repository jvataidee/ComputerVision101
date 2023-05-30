import cv2
import numpy as np

# Função para remover imperfeições utilizando a função inpaint do OpenCV
def remove_blemish(event, x, y, flags, param):
    global img, mask, radius

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(mask, (x, y), radius, 255, -1)
        img = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
        mask.fill(0)

# Função para exibir instruções
def print_instructions():
    print("Instruções:")
    print("1. Clique com o botão esquerdo do mouse sobre a imperfeição que deseja remover.")
    print("2. Pressione 'r' para redefinir a imagem original.")
    print("3. Pressione 'q' para sair do programa.")
    print("4. Pressione '+' para aumentar o raio do pincel.")
    print("5. Pressione '-' para diminuir o raio do pincel.")

# Parâmetros iniciais
radius = 5
image_path = "blemish.png"

# Carregar a imagem e criar uma máscara
img = cv2.imread(image_path)
mask = np.zeros(img.shape[:2], dtype=np.uint8)

# Exibir instruções
print_instructions()

# Criar janela e configurar a função callback do mouse
cv2.namedWindow("Blemish Removal")
cv2.setMouseCallback("Blemish Removal", remove_blemish)

while True:
    cv2.imshow("Blemish Removal", img)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('r'):
        img = cv2.imread(image_path)
        mask.fill(0)
    elif key == ord('+'):
        radius += 1
        print(f"Raio do pincel aumentado para {radius}")
    elif key == ord('-'):
        radius = max(1, radius - 1)
        print(f"Raio do pincel diminuído para {radius}")

cv2.destroyAllWindows()


#%%
