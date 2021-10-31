import pandas as pd
from tqdm import tqdm


# Função para importar os microdados
def importar_dados(nome, colunas=None):
    print("Importando...")
    microdados = pd.read_csv(nome, sep=';', encoding='latin-1', usecols=colunas)
    print("Importado")
    return microdados


def localiza_valor_nos_microdados(microdados, num):
    return microdados.loc[microdados['CO_PROVA_MT'] == num]


def filtrar_dados(lista_de_usados, microdados):
    novos_microdados = None
    for i, num in enumerate(lista_de_usados):
        if i == 0:
            # Se for a primeira vez no laço é preciso criar um novo dataframe
            micro_filtrados = localiza_valor_nos_microdados(microdados, num)
            novos_microdados = micro_filtrados
            # Cria o dataframe "novos_microdados"
        else:
            # Senão for a primeira vez é preciso juntar(merge) os dois dataframes
            micro_filtrados = localiza_valor_nos_microdados(microdados, num)
            novos_microdados = pd.merge(novos_microdados, micro_filtrados, how='outer')
            # Juntando os dataframes
    return novos_microdados


def exportar_dados(microdados, nome):
    print("Exportando...")
    microdados.to_csv(nome, index=False, sep=';', encoding='latin-1')
    print("Processo concluído")
    return microdados


def cria_nova_noluna(microdados, nome_da_coluna):
    microdados.loc[:, nome_da_coluna] = 0
    return microdados


def calc_quest_acertadas(gabarito, respostas):
    cont = 0
    for i in range(0, len(respostas)):
        if respostas[i] == gabarito[i]:
            # Se a resposta e o gabarito for o mesmo soma 1 na contagem
            cont += 1
    return cont


def calc_quest_acertadas_total(microdados):
    microdados = cria_nova_noluna(microdados, "QuestAcertadas")
    quantidade_de_linhas = microdados.loc[:, "CO_PROVA_MT"].count()
    for i in tqdm(range(0, 100000)):
        microdados.loc[i, 'QuestAcertadas'] = calc_quest_acertadas(microdados.iloc[i]["TX_GABARITO_MT"],
                                                                   microdados.iloc[i]["TX_RESPOSTAS_MT"])
        # Para cada linha calcula a quantidade de questões acertadas usando a função
    return microdados


def mostrar_resultado_com_info(microdados):
    print(microdados['NU_NOTA_MT'].describe())


def imprimir_espaco_para_organizar():
    print("\n" + '#' * 30 + "\n")


def mostrar_min_med_max(microdados):
    minimo = microdados['NU_NOTA_MT'].min()
    media = microdados['NU_NOTA_MT'].mean()
    maximo = microdados['NU_NOTA_MT'].max()

    print(f'O valor mínimo é {minimo:.2f}')
    print(f'O valor médio é {media:.2f}')
    print(f'O valor máximo é {maximo:.2f}')


def mostrar_resultado(microdados):
    for i in range(0, 45 + 1):
        # Laço para cada valor possível de acertos
        print(f'QUANTIDADE DE ACERTOS: {i}')
        micro_com_questao = microdados.loc[microdados['QuestAcertadas'] == i]
        # Localiza os dados com uma quantidade de acertos específica

        mostrar_min_med_max(micro_com_questao)

        resp = input("Precione enter para ir para o próximo valor\nou digite \"info\" para mais informações:")
        if resp.strip().lower() == "info":
            mostrar_resultado_com_info(micro_com_questao)

        imprimir_espaco_para_organizar()
