povos = ['anões', 'elfos', 'orcs', 'homens', 'dragões']
combatentes = []
for povo in povos:
    print(f'Povo: {povo}')
    for i in range(1): #foi colocado range(1) pois 200 ficaria muito extenso
        idade = int(input(f'Idade do combatente {i+1}: '))
        peso = float(input(f'Peso do combatente {i+1} (em kg): '))
        altura = float(input(f'Altura do combatente {i+1} (em metros): '))
        combatentes.append({'povo': povo, 'idade': idade, 'peso': peso, 'altura': altura})
contador_jovens = 0
for combatente in combatentes:
    if combatente['idade'] < 18:
        contador_jovens += 1
print(f'Quantia de juvenis malditos: {contador_jovens}')
for povo in povos:
    soma_idades = 0
    contador_combatentes = 0
    for combatente in combatentes:
        if combatente['povo'] == povo:
            soma_idades += combatente['idade']
            contador_combatentes += 1
    if contador_combatentes > 0:
        media_idades = soma_idades / contador_combatentes
        print(f'Média invernos dos combatentes {povo}: {media_idades:.2f}')
soma_alturas = 0
for combatente in combatentes:
    soma_alturas += combatente['altura']
media_alturas = soma_alturas / len(combatentes)
print(f'Média da elevações dos pobre coitados infelizes: {media_alturas: .2f} metros de pura bravura!')

pesados = 0
for combatente in combatentes:
    if combatente['peso'] > 80:
        pesados += 1
porcentagem_pesados = pesados / len(combatentes)
print(f'Porcentagem do barrigão dos amaldiçoados da guerra: {porcentagem_pesados: .2f} kg de pura massa destrutiva')


