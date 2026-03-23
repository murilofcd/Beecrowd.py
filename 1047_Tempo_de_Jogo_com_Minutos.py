'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada

Quatro números inteiros representando a hora de início e fim do jogo.

Saída

Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''

valores = input().split()

hi = int(valores[0])
mi = int(valores[1])
hf = int(valores[2])
mf = int(valores[3])

inicio = hi * 60 + mi
fim = hf * 60 + mf

if fim > inicio:
    duracao_min = fim - inicio
else:
    duracao_min = 24*60 - inicio + fim

duracao_h = duracao_min // 60
duracao_m = duracao_min % 60

print(f"O JOGO DUROU {duracao_h} HORA(S) E {duracao_m} MINUTO(S)")

