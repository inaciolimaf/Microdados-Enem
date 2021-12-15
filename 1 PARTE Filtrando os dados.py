"""
Código para calcular uma relação entre a quantidade de acertos e a nota no ENEM
baseado nos Microdados
Inácio Lima de Souza Filho
"""
import FuncoesDados

# Primeira parte para filtragem de dados
materia = "MT"
ColunasMatematica = [f"NU_NOTA_{materia}", f"TX_RESPOSTAS_{materia}", f"TX_GABARITO_{materia}", f"CO_PROVA_{materia}"]
# Colunas que serão usadas para os calculos em Matemática
"""
Significado da cada coluna:

"NU_NOTA_{}": Se refere a nota do candidato, é usada na parte 3 para comparar com 
a quantidade de acertos
"TX_RESPOSTAS_{}": Se refere as respostas do candidato, é usada para calcular 
a quantidade de acertos
"TX_GABARITO_{}": Se refere ao gabarito da prova (cada prova tem um gabarito
diferente), também é usada para calcular a quantidade de acertos
"CO_PROVA_{}": Se refere ao código da prova, é usado para filtrar os dados
"""
# Mais informações estão no Dicionário disponível junto com os microdados

microdados = FuncoesDados.MicrodadosENEM("MICRODADOS_ENEM_2019.csv", ColunasMatematica)
# Inicia a objeto lendo os microdados

ListaDeUsados = [515, 516, 517, 518]
# Lista com os valores para serem usados, cada um indica o código referente a
# uma cor de uma prova da aplicação do ENEM, não será considerado o ENEM PPL

print("Iniciando a filtragem dos dados para matemática")
NovosMicrodados = microdados.filtrar_dados(microdados, ListaDeUsados)
print("Filtragem concluída. O resultado é:")
print(NovosMicrodados.microdados)

NovosMicrodados.exportar_dados("MicrodadosFiltrados.csv")
