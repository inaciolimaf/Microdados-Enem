"""
Código para calcular uma relação entre a quantidade de acertos e a nota no ENEM
baseado nos Microdados
Inácio Lima de Souza Filho
"""
import FuncoesDados

# Primeira parte para filtragem de dados
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

materias = {"MT": [587, 588, 589, 590], "LC": [577, 578, 579, 580],
            "CH": [567, 568, 569, 570], "CN": [597, 598, 599, 600]}
# Para Micros2020
for materia, ListaDeUsados in materias.items():
    ColunasUsadas = [f"NU_NOTA_{materia}", f"TX_RESPOSTAS_{materia}",
                     f"TX_GABARITO_{materia}", f"CO_PROVA_{materia}"]
    microdados = FuncoesDados.MicrodadosENEM.ler_microdados("MICRODADOS_ENEM_2020.csv",
                                                            ColunasUsadas,
                                                            materia)
    # Inicia a objeto lendo os microdados
    # ListaDeUsados com os valores para serem usados, cada um indica o código referente a
    # uma cor de uma prova da aplicação do ENEM, não será considerado o ENEM PPL
    print("Iniciando a filtragem dos dados")
    microdados = microdados.filtrar_dados(microdados, ListaDeUsados, materia)
    print("Filtragem concluída. O resultado é:")
    print(microdados.microdados)

    print("Iniciando o calculo:")
    microdados.calc_quest_acertadas_total()
    print("Processo concluído. O resultado é:")
    print(microdados.microdados)

    print(microdados.exportar_resultado())
    # microdados.mostrar_resultado()
    # Opicional
    print("Concluído.")