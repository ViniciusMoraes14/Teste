import json

#Abrindo o arquivo json!
with open("dados.json") as dados_json:
    dados = json.load(dados_json)

#Colocando os valores dentro de uma lista.
faturamento = []
for x in dados:
    valor = x['valor']
    faturamento.append(float(valor))

#Calculo da média de faturamento.
media = sum(faturamento)/30
#Calculando a quantidade de dias que foi superior a média.
dias = 0 
for i in dados:
    if i['valor'] > media:
        dias+=1

print('~'*50)
print("RESULTADOS")
print('~'*50)
print(f"Menor Valor: R$ {min(faturamento)}")
print('~'*50)
print(f"Maior Valor: R$ {max(faturamento)}")
print('~'*50)
print(f"{dias} foi superior!")
print('~'*50)