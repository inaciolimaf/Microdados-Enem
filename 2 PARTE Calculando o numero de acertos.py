import FuncoesDados

# Segunda parte para calcular a quantidade de acertos

microdados = FuncoesDados.MicrodadosENEM("MicrodadosFiltrados.csv")

print("Iniciando o calculo:")
microdados.calc_quest_acertadas_total()
print("Processo concluído. O resultado é:")
print(microdados.microdados)

microdados.exportar_dados("MicrodadosFiltradosComQuest.csv")
