# Importando as bibliotecas
import cv2
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('dark_background')
matplotlib.rcParams['figure.figsize'] = (8.0, 8.0)
matplotlib.rcParams['image.cmap'] = 'gray'
# %matplotlib inline

# Definir o caminho dos dados e modelos
DATA_PATH = r"D:\Estudos\OpenCV\Computer Vision - Introduction\w9 - Video Analysis\data"
MODEL_PATH = r"D:\Estudos\OpenCV\Computer Vision - Introduction\w10 - Deep Learning\models"
modelFile = MODEL_PATH + "/ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.pb"
configFile = MODEL_PATH + "/ssd_mobilenet_v2_coco_2018_03_29.pbtxt"
classFile = MODEL_PATH + "/coco_class_labels.txt"

# Carregar o modelo SSD
net = cv2.dnn.readNetFromTensorflow(modelFile, configFile)

# Ler o arquivo de classes
with open(classFile) as fp:
    labels = fp.read().split("\n")

# Obter o índice da classe "sports ball"
class_index = labels.index('sports ball')

# Definir o rastreador CSRT
tracker = cv2.TrackerCSRT_create()

# Função para detecção de objetos com SSD
def object_detection(net, img):
    dim = 300
    mean = (127.5, 127.5, 127.5)

    blob = cv2.dnn.blobFromImage(img, 1.0/127.5, (dim, dim), mean, True)

    # Passar o blob para a rede neural
    net.setInput(blob)

    # Realizar a predição
    objects = net.forward()
    return objects

# Função para exibir os objetos detectados na imagem
def display_objects(im, objects, threshold=0.25):

    rows = im.shape[0]
    cols = im.shape[1]

    # Para cada objeto detectado
    for i in range(objects.shape[2]):
        # Obter a classe e a confiança
        classId = int(objects[0, 0, i, 1])
        score = float(objects[0, 0, i, 2])

        # Verificar se a detecção é da classe "sports ball"
        if classId == class_index and score > threshold:
            # Recuperar as coordenadas originais a partir das coordenadas normalizadas
            x = int(objects[0, 0, i, 3] * cols)
            y = int(objects[0, 0, i, 4] * rows)
            w = int(objects[0, 0, i, 5] * cols - x)
            h = int(objects[0, 0, i, 6] * rows - y)

            # Exibir a caixa delimitadora
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Inicializar o rastreador com a caixa delimitadora
            bbox = (x, y, w, h)
            tracker.init(im, bbox)

    return im

# Ler o vídeo
video = cv2.VideoCapture(r"D:\Estudos\OpenCV\Computer Vision - Introduction\w11 - Projects\Project4\soccer-ball.mp4")

# Verificar se o vídeo foi aberto corretamente
if not video.isOpened():
    print("Não foi possível abrir o vídeo.")

# Ler o primeiro frame
ok, frame = video.read()
if not ok:
    print('Não foi possível ler o arquivo de vídeo.')

# Definir as configurações do vídeo de saída
output_file = 'output_video.mp4'
output_fps = video.get(cv2.CAP_PROP_FPS)
output_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
output_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter(output_file, fourcc, output_fps, (output_width, output_height))

# Loop para processar cada frame do vídeo
while True:
    # Ler um novo frame
    ok, frame = video.read()
    if not ok:
        break

    # Detectar objetos com SSD e realizar o rastreamento
    objects = object_detection(net, frame)
    frame = display_objects(frame, objects)

    # Atualizar o rastreador
    ok, bbox = tracker.update(frame)

    # Verificar se o rastreamento foi bem-sucedido
    if ok:
        # Rastreamento bem-sucedido
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2)
        #cv2.putText(frame, "Tracking", (p1[0], p1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
    else:
        # Rastreamento falhou
        cv2.putText(frame, "Rastreamento falhou", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Exibir o frame resultante
    cv2.imshow("Detecção e rastreamento de objetos", frame)

    # Salvar o frame no vídeo de saída
    output_video.write(frame)

    # Verificar se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
video.release()
output_video.release()
cv2.destroyAllWindows()
