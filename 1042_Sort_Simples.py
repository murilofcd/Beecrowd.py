'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada

A entrada contem três números inteiros.

Saída

Imprima a saída conforme foi especificado.
'''

valores = input().split()

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

original = [a, b, c]

ordenados = sorted(original)

for num in ordenados:
    print(num)

print()

for num in original:
    print(num)
