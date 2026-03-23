'''

Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada

O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída

Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''

N = int(input())
valor = N

print(valor)

# cédulas de 100
nota100 = N // 100
N = N % 100
print(f"{nota100} nota(s) de R$ 100,00")

# cédulas de 50
nota50 = N // 50
N = N % 50
print(f"{nota50} nota(s) de R$ 50,00")

# cédulas de 20
nota20 = N // 20
N = N % 20
print(f"{nota20} nota(s) de R$ 20,00")

# cédulas de 10
nota10 = N // 10
N = N % 10
print(f"{nota10} nota(s) de R$ 10,00")

# cédulas de 5
nota5 = N // 5
N = N % 5
print(f"{nota5} nota(s) de R$ 5,00")

# cédulas de 2
nota2 = N // 2
N = N % 2
print(f"{nota2} nota(s) de R$ 2,00")

# cédulas de 1
nota1 = N // 1
N = N % 1
print(f"{nota1} nota(s) de R$ 1,00")
