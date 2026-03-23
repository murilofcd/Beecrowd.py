'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

Distancia =

Entrada

O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída

Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.
'''

X = input().split()
Y = input().split()

x1 = float(X[0])
y1 = float(X[1])

x2 = float(Y[0])
y2 = float(Y[1])

DISTANCIA = ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5

print(f"{DISTANCIA:.4f}")

