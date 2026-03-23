'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada

O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída

A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
'''

X = input().split()

x1 = int(X[0])
x2 = int(X[1])
x3 = float(X[2])

ValorX = x2 * x3

Y = input().split()

y1 = int(Y[0])
y2 = int(Y[1])
y3 = float(Y[2])

ValorY = y2 * y3

SOMA = ValorX + ValorY

print("VALOR A PAGAR: R$ %.2f" % SOMA)

