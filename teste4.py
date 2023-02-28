
#Faturamentos
SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

#Total do Faturamento
Faturamento = SP+RJ+MG+ES+Outros

#Calculo
Porcentagem_SP = ((SP/Faturamento)*100)
Porcentagem_RJ = ((RJ/Faturamento)*100)
Porcentagem_MG = ((MG/Faturamento)*100)
Porcentagem_ES = ((ES/Faturamento)*100)
Porcentagem_Outros = ((Outros/Faturamento)*100)

#Resultado
print(f'Porcentagem de Cada Estado em Relação ao Faturamento da Distribuidora:\nSP-{Porcentagem_SP}%\nRJ-{Porcentagem_RJ}%\nMG-{Porcentagem_MG}%\nES-{Porcentagem_ES}%\nOutros Estados-{Porcentagem_Outros}%')

#Verificando se deu certo a conta!
total = Porcentagem_SP + Porcentagem_RJ + Porcentagem_MG + Porcentagem_ES + Porcentagem_Outros
print(f'{total}%')