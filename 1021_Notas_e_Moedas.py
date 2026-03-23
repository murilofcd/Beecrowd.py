'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada

O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída

Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
'''

N = float(input())

valor = int(round(N * 100))

print("NOTAS:")

# notas
nota100 = valor // 10000
valor = valor % 10000
print(f"{nota100} nota(s) de R$ 100.00")

nota50 = valor // 5000
valor = valor % 5000
print(f"{nota50} nota(s) de R$ 50.00")

nota20 = valor // 2000
valor = valor % 2000
print(f"{nota20} nota(s) de R$ 20.00")

nota10 = valor // 1000
valor = valor % 1000
print(f"{nota10} nota(s) de R$ 10.00")

nota5 = valor // 500
valor = valor % 500
print(f"{nota5} nota(s) de R$ 5.00")

nota2 = valor // 200
valor = valor % 200
print(f"{nota2} nota(s) de R$ 2.00")

print("MOEDAS:")

# moedas
moeda1 = valor // 100
valor = valor % 100
print(f"{moeda1} moeda(s) de R$ 1.00")

moeda050 = valor // 50
valor = valor % 50
print(f"{moeda050} moeda(s) de R$ 0.50")

moeda025 = valor // 25
valor = valor % 25
print(f"{moeda025} moeda(s) de R$ 0.25")

moeda010 = valor // 10
valor = valor % 10
print(f"{moeda010} moeda(s) de R$ 0.10")

moeda005 = valor // 5
valor = valor % 5
print(f"{moeda005} moeda(s) de R$ 0.05")

moeda001 = valor // 1
valor = valor % 1
print(f"{moeda001} moeda(s) de R$ 0.01")
