import cv2
import numpy as np

def preprocess(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 200)
    return edges

def find_contour(edges):
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=cv2.contourArea)
    return contour

def four_point_transform(image, pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    (tl, tr, br, bl) = rect
    maxWidth = max(int(np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))), int(np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))))
    maxHeight = max(int(np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))), int(np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))))
    dst = np.array([[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]], dtype="float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped

def document_scanner(image_path):
    # Leitura da imagem
    image = cv2.imread(image_path)
    original_image = image.copy()

    # Pré-processamento e detecção de bordas
    edges = preprocess(image)

    # Detecção do contorno
    contour = find_contour(edges)

    # Aproximação do contorno para obter os 4 pontos
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    pts = np.squeeze(approx)

    # Desenhar contorno, vértices numerados e mensagem de salvar na imagem original
    cv2.drawContours(original_image, [contour], -1, (0, 255, 0), 2)
    for i, (x, y) in enumerate(pts):
        cv2.circle(original_image, (x, y), 5, (0, 0, 255), -1)
        cv2.putText(original_image, str(i+1), (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(original_image, "Pressione 'q' para salvar a imagem", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Transformação de perspectiva
    warped = four_point_transform(image, pts)

    # Exibição dos resultados
    cv2.imshow("Original", original_image)
    cv2.imshow("Scanned Document", warped)

    # Salvar a imagem corrigida quando a tecla 'q' for pressionada
    key = cv2.waitKey(0)
    if key == ord('q'):
        cv2.imwrite("scanned-form-corrected.jpg", warped)
        print("Imagem corrigida salva com sucesso.")

    cv2.destroyAllWindows()

# Exemplo de uso
document_scanner("scanned-form.jpg")