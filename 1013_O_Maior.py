'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:



Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada

O arquivo de entrada contém três valores inteiros.

Saída

Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''

X = input().split()

a = int(X[0])
b = int(X[1])
c = int(X[2])

MaiorAB = (a + b + abs(a - b)) // 2
Maior = (MaiorAB + c + abs(MaiorAB - c)) // 2

print(Maior, "eh o maior")


