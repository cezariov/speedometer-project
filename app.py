velocidade = int(input("Digite sua velocidade"))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print("Não Levou Muta")
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print("Levou multa")
elif velocidade > velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print("Levou multa grave")
