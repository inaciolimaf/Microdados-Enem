from FuncoesDados import importar_dados, mostrar_resultado 

# Terceira parte para mostrar o resultado

microdados = importar_dados("MicrodadosFiltradosComQuest.csv", colunas=None)

mostrar_resultado(microdados)
print("Concluído.")
