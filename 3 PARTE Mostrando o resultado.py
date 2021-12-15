import FuncoesDados

# Terceira parte para exportar o resultado

microdados = FuncoesDados.MicrodadosENEM("MicrodadosFiltradosComQuest.csv", colunas=None)
microdados.exportar_resultado()
# microdados.mostrar_resultado()
# Opicional
print("Concluído.")
