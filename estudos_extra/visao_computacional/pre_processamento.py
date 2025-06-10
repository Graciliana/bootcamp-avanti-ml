# Operações basicas

# imports
import cv2
import numpy as np
from matplotlib import pyplot as grafico

## Acessando e modificando valores de pixels
imagem = cv2.imread("frutas.jpeg")
valorPixel = imagem[150, 150]
print(valorPixel)
##resultado: [25 33 187]


##modificando para tons de cinza a imagem 
imagem = cv2.imread("frutas.jpeg")
imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
valorPixel = imagem[150, 150]
print(valorPixel)
##resultado: 48

## AGORA VALOR DE INTENSIDADE DA COR EM UM UNICO CANAL
imagem = cv2.imread("frutas.jpeg")
valorPixel = imagem[150, 150, 0]
print(valorPixel)
##resultado: 25

#######################################################################################
# HISTOGRAMA EM UMA IMAGEM BINÁRIA

imagem = cv2.imread("folha-binaria.bmp", 0)
totalPixelPreto = 0
totalPixelBranco = 0

for x in range(0, 499):
    for y in range(0,499):
        if imagem[x,y] == 255:
            totalPixelBranco += 1
        else:
            totalPixelPreto += 1
print("Total pixels Branco: ", totalPixelBranco)
print("Total pixels Preto: ", totalPixelPreto)
# resultado: Total pixels Branco: 190903
#            Total pixels Preto: 58098

# grafico do histograma da imagem
imagem = cv2.imread("folha-binaria.bmp", 0)
grafico.hist(imagem.ravel(), 256, [0,256])
grafico.show()