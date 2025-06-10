# IMPORTS
import cv2

#CARREGANDO IMAGENS A PARTIR DE ARQUIVOS
imagem = cv2.imread("imagem.jpg")
cv2.imshow("Imagem",imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

# CARREGANDO IMAGENS A PARTIR DE vídeos
captura = cv2.VideoCapture("Video.mp4")

while True:
    ret, frame = captura.read()
    cv2.imshow("Imagem", frame)
    
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
captura.release()
cv2.destroyAllWindows()

# CARREGANDO IMAGENS A PARTIR DE UMA WEBCAM
captura = cv2.VideoCapture(0)

while True:
    ret, frame = captura.read()
    cv2.imshow("Imagem", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
captura.release()
cv2.destroyAllWindows()
