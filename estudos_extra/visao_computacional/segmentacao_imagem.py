import cv2

# carregamento imagem RGB e segmentando canais
imagem = cv2.imread("frutas.jpeg")
azul, verde, vermelho = cv2.split(imagem)

#Exibindo imagens dos canais separados
cv2.imshow("Canal R", vermelho)
cv2.imshow("Canal G", verde)
cv2.imshow("Canal B", azul)

# Salvando imagens dos canais separados 
cv2.imwrite("frutas-canal-vermelho.jpeg", vermelho)
cv2.imwrite("frutas-canal-verde.jpeg", verde)
cv2.imwrite("frutas-canal-azul.jpeg", azul)

cv2.waitKey(0)
cv2.destroyAllWindows()

################################################################################
# Combinando canais em um imagem RGB
# carregamento imagem RGB e segmentando canais
imagem = cv2.imread("frutas.jpeg")
azul, verde, vermelho = cv2.split(imagem)

# Combinando os três canais em uma única imagem
imagem = cv2.merge((azul, verde, vermelho))
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()

################################################################################
# Converter imagens em RGB para tons de cinza
# carregamento imagem em RGB
imagem = cv2.imread("frutas.jpeg")

# CONVERTENDO e exibindo a imagem em tons de cinza
imagem = cv2.cvtColor(imagem, cv2.COLOR_BAYER_BG2GRAY)
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()

################################################################################
# Segmentando canais em uma imagem HSV

imagem = cv2.imread("frutas.jpeg")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

matriz, saturacao, valor = cv2.split(imagem)

cv2.imshow("Canal H", matriz)
cv2.imshow("Canal S", saturacao)
cv2.imshow("Canal V", valor)

imagem = cv2.merge((matriz, saturacao, valor))
imagem = cv2.cvtColor(imagem, cv2.COLOR_HLS2BGR)

cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()