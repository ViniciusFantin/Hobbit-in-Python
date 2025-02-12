salario_inicial = 1000
ano_atual = 70 #supomos que estamos no ano 70

ano_contratacao = 55
ano_aumento_56 = 56
percentual_aumento = 1.5

salario = salario_inicial
ano = ano_contratacao

while ano < ano_atual:
    if ano == ano_aumento_56:
        salario *= 1 + percentual_aumento / 100
    else:
        percentual_aumento = min(percentual_aumento * 2, 100)
        salario *= 1 + percentual_aumento / 100
    ano += 1

print(f"Salário de Thorin em {ano_atual} será de {salario:.2f} moedas de ouro")