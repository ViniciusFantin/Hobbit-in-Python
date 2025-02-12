anoes = []
for i in range (13):
    nome= input(f"digite o nome do {i+1}º anão: ")
    peso = float(input(f"digite o peso do {i+1}º anão: "))
    anoes.append ((nome, peso))
for nome, peso in anoes:
    print (f"{nome} - peso: {peso: .1f} kg")
    if peso > 70:
        print ("baita panção, logo precisará de um barril mais reforçado, anõe malditos!")
media = sum(peso for nome, peso in anoes) / len(anoes)
print(f"média de gordura do barrigão dos anões: {media: .1f} de pura satisfação")