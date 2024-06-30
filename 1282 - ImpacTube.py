qtd_canais = int(input())
canais = []

for _ in range(qtd_canais):
    nome, inscritos, monetizacao, premium = input().split(';')
    inscritos = int(inscritos)
    monetizacao = float(monetizacao)
    if premium == 'sim':
        premium = True
    else:
        premium = False
    canais.append([nome, inscritos, monetizacao, premium])

fixo_premium = float(input())
fixo_nao_premium = float(input())

bonificacao = []

for canal in canais:
    valor = canal[2]
    if canal[3]:
        valor += (canal[1] // 1000) * fixo_premium
    else:
        valor += (canal[1] // 1000) * fixo_nao_premium
    bonificacao.append([canal[0], valor])

print(5 * '-')
print('BÔNUS')
print(5 * '-')
for bonus in bonificacao:
    nome, valor = bonus
    print(f'{nome}: R$ {valor:.2f}')
