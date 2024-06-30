def coleta_canais(qtd_canais):
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
    return canais

def calcula_bonificacao(canais, fixo_premium, fixo_nao_premium):
    bonificacao = []
    for canal in canais:
        valor = canal[2]
        if canal[3]:
            valor += (canal[1] // 1000) * fixo_premium
        else:
            valor += (canal[1] // 1000) * fixo_nao_premium
        bonificacao.append([canal[0], valor])
    return bonificacao

def exibe_bonificacao(bonificacao):
    print(5 * '-')
    print('BÔNUS')
    print(5 * '-')
    for bonus in bonificacao:
        nome, valor = bonus
        print(f'{nome}: R$ {valor:.2f}')

def main():
    qtd_canais = int(input())
    canais = coleta_canais(qtd_canais)
    fixo_premium = float(input())
    fixo_nao_premium = float(input())
    bonificacao = calcula_bonificacao(canais, fixo_premium, fixo_nao_premium)
    exibe_bonificacao(bonificacao)

main()
