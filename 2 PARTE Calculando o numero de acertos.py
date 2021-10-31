from FuncoesDados import importar_dados, exportar_dados, calc_quest_acertadas_total

# Segunda parte para calcular a quantidade de acertos


microdados = importar_dados("MicrodadosFiltrados.csv")

print("Iniciando o calculo:")
microdados = calc_quest_acertadas_total(microdados)
print("Processo concluído. O resultado é:")
print(microdados)

exportar_dados(microdados, "MicrodadosFiltradosComQuest.csv")
