from numpy import NaN
import pandas as pd
from tqdm import tqdm

# Todo essa parte é só para funcionar a orientação à objeto
# Ela não é obrigatória para chegar no resultado
# O jeito mais fácil seria usar o Jupyter e sem Orientação à objeto
# Fiz usando isso para poder aprender


class MicrodadosENEM:
    def __init__(self, nome=None, colunas=None, ler_microdados=True, microdados=None):
        if ler_microdados:
            print("Importando...")
            self.microdados = pd.read_csv(nome, sep=';', encoding='latin-1', usecols=colunas)
            print("Importado")
        else:
            self.microdados = microdados
        # Divide em duas partes porque em uma parte do código será preciso criar uma objeto
        # sem fazer a leitura de um arquivo

    def _localiza_valor_nos_microdados(self, num):
        return self.microdados.loc[self.microdados['CO_PROVA_MT'] == num]

    @classmethod
    def filtrar_dados(cls, microdados, lista_de_usados):
        novos_microdados = None
        for i, num in enumerate(lista_de_usados):
            if i == 0:
                # Se for a primeira vez no laço é preciso criar um novo dataframe
                micro_filtrados = microdados._localiza_valor_nos_microdados(num)
                novos_microdados = micro_filtrados
                # Cria o dataframe "novos_microdados"
            else:
                # Senão for a primeira vez é preciso juntar(merge) os dois dataframes
                micro_filtrados = microdados._localiza_valor_nos_microdados(num)
                novos_microdados = pd.merge(novos_microdados, micro_filtrados, how='outer')
                # Juntando os dataframes
        return cls(ler_microdados=False, microdados=novos_microdados)
        # Retorna um objeto com os novos microdados

    def exportar_dados(self, nome):
        print("Exportando...")
        self.microdados.to_csv(nome, index=False, sep=';', encoding='latin-1')
        print("Processo concluído")

    def _cria_nova_noluna(self, nome_da_coluna):
        self.microdados.loc[:, nome_da_coluna] = NaN

    @staticmethod
    def _calc_quest_acertadas(gabarito, respostas):
        cont = 0
        for i in range(0, len(respostas)):
            if respostas[i] == gabarito[i]:
                # Se a resposta e o gabarito for o mesmo soma 1 na contagem
                cont += 1
        return cont

    def calc_quest_acertadas_total(self):
        self._cria_nova_noluna("QuestAcertadas")
        quantidade_de_linhas = self.microdados.loc[:, "CO_PROVA_MT"].count()
        for i in tqdm(range(0, quantidade_de_linhas)):
            self.microdados.loc[i, 'QuestAcertadas'] = self._calc_quest_acertadas(
                self.microdados.iloc[i]["TX_GABARITO_MT"],
                self.microdados.iloc[i]["TX_RESPOSTAS_MT"])
            # Para cada linha calcula a quantidade de questões acertadas usando a função

    @staticmethod
    def _mostrar_resultado_com_info(microdados):
        print(microdados['NU_NOTA_MT'].describe())

    @staticmethod
    def _imprimir_espaco_para_organizar():
        print("\n" + '#' * 30 + "\n")

    @staticmethod
    def _mostrar_min_med_max(microdados):
        minimo = microdados['NU_NOTA_MT'].min()
        media = microdados['NU_NOTA_MT'].mean()
        maximo = microdados['NU_NOTA_MT'].max()

        print(f'O valor mínimo é {minimo:.2f}')
        print(f'O valor médio é {media:.2f}')
        print(f'O valor máximo é {maximo:.2f}')

    def mostrar_resultado(self):
        for i in range(0, 45 + 1):
            # Laço para cada valor possível de acertos
            print(f'QUANTIDADE DE ACERTOS: {i}')
            micro_com_questao = self.microdados.loc[self.microdados['QuestAcertadas'] == i]
            # Localiza os dados com uma quantidade de acertos específica
            self._mostrar_min_med_max(micro_com_questao)

            resp = input("Precione enter para ir para o próximo valor\nou digite \"info\" para mais informações:")
            if resp.strip().lower() == "info":
                self._mostrar_resultado_com_info(micro_com_questao)

            self._imprimir_espaco_para_organizar()
