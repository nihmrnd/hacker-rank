arr = list(map(int, input().rstrip().split()))

resultados = []
for i in arr:
  multiplicacoes = []
  for x in range(1,11):
    multiplicacao = x*i
    multiplicacoes.append(multiplicacao)
  resultados.append(multiplicacoes)

resultados_valores_comuns = []
sublista_um = resultados_valores_comuns[0]

for sublista in resultados:
  valores_comuns = []
  for i in sublista[0]:
    for j in sublista[1]:
      if sublista[i] == sublista[j]:
        valores_comuns.append(sublista[i])
  resultados_valores_comuns.append(valores_comuns)
print(resultados_valores_comuns)        
