from numpy import NaN
import pandas as pd
from tqdm import tqdm

# Todo essa parte é só para funcionar a orientação à objeto
# Ela não é obrigatória para chegar no resultado
# O jeito mais fácil seria usar o Jupyter e sem Orientação à objeto
# Fiz usando isso para poder aprender


class MicrodadosENEM:
    def __init__(self, microdados, materia: str):
        self.microdados = microdados
        # Divide em duas partes porque em uma parte do código será preciso criar uma objeto
        # sem fazer a leitura de um arquivo
        self.quantAcertos = []
        # Cria uma lista para ser preenchidda em outra função com a quantidade de acertos
        # e depois adicionada nos microdados
        self.materia = materia
        # Matéria que será calculada

    @classmethod
    def ler_microdados(cls, nome: str, colunas: str, materia: str):
        print("Importando...")
        dados = pd.read_csv(nome, sep=';', encoding='latin-1', usecols=colunas)
        # Lê os microdados
        print("Importado")
        return cls(dados, materia)

    def localiza_valor_nos_microdados(self, num):
        return self.microdados.loc[self.microdados[f"CO_PROVA_{self.materia}"] == num]

    @classmethod
    def filtrar_dados(cls, microdados, lista_de_usados, materia):
        novos_microdados = None
        for i, num in enumerate(lista_de_usados):
            if i == 0:
                # Se for a primeira vez no laço é preciso criar um novo dataframe
                micro_filtrados = microdados.localiza_valor_nos_microdados(num)
                novos_microdados = micro_filtrados
                # Cria o dataframe "novos_microdados"
            else:
                # Senão for a primeira vez é preciso juntar(merge) os dois dataframes
                micro_filtrados = microdados.localiza_valor_nos_microdados(num)
                novos_microdados = pd.merge(novos_microdados, micro_filtrados, how='outer')
                # Juntando os dataframes
        return cls(novos_microdados, materia)
        # Retorna um objeto com os novos microdados

    def exportar_dados(self, nome):
        print("Exportando...")
        self.microdados.to_csv(nome, index=False, sep=';', encoding='latin-1')
        print("Processo concluído")

    def _cria_nova_noluna(self, nome_da_coluna):
        self.microdados.loc[:, nome_da_coluna] = NaN

    def _calc_quest_acertadas(self, respostas, gabarito):
        cont = 0
        for i in range(0, len(respostas)):
            if respostas[i] == gabarito[i]:
                # Se a resposta e o gabarito for o mesmo soma 1 na contagem
                cont += 1
        self.quantAcertos.append(cont)

    def calc_quest_acertadas_total(self):
        for i in tqdm(self.microdados.iterrows()):
            # O tqdm é para ver o progresso
            self._calc_quest_acertadas(i[1][2],i[1][3])
            # Para cada linha calcula a quantidade de questões acertadas usando a função
        self.microdados['QuestAcertadas'] = self.quantAcertos
        # Coloca a lista nos microdados

    def _mostrar_resultado_com_info(self, microdados):
        print(microdados[f"NU_NOTA_{self.materia}"].describe())

    @staticmethod
    def _imprimir_espaco_para_organizar():
        print("\n" + '#' * 30 + "\n")

    def _mostrar_min_med_max(self, microdados):
        minimo = microdados[f"NU_NOTA_{self.materia}"].min()
        media = microdados[f"NU_NOTA_{self.materia}"].mean()
        maximo = microdados[f"NU_NOTA_{self.materia}"].max()

        print(f"O valor mínimo é {minimo:.2f}")
        print(f"O valor médio é {media:.2f}")
        print(f"O valor máximo é {maximo:.2f}")

    def mostrar_resultado(self):
        for i in range(0, 45 + 1):
            # Laço para cada valor possível de acertos
            print(f"QUANTIDADE DE ACERTOS: {i}")
            micro_com_questao = self.microdados.loc[self.microdados["QuestAcertadas"] == i]
            # Localiza os dados com uma quantidade de acertos específica
            self._mostrar_min_med_max(micro_com_questao)

            resp = input("Precione enter para ir para o próximo valor\nou digite \"info\" para mais informações:")
            if resp.strip().lower() == "info":
                self._mostrar_resultado_com_info(micro_com_questao)

            self._imprimir_espaco_para_organizar()

    def exportar_resultado(self):
        print("Iniciando a exportação")
        lista_com_todas_questoes = []
        for i in range(0, 45+1):
            micro_com_questao = self.microdados.loc[self.microdados["QuestAcertadas"] == i]
            # Localiza os dados com uma quantidade de acertos específica
            minimo = micro_com_questao[f"NU_NOTA_{self.materia}"].min()
            media = micro_com_questao[f"NU_NOTA_{self.materia}"].mean()
            maximo = micro_com_questao[f"NU_NOTA_{self.materia}"].max()
            minimo = round(minimo, 2)
            media = round(media, 2)
            maximo = round(maximo, 2)
            # Calcula o mínimo, a média e o máximo
            lista_com_uma_questao = [i, minimo, media, maximo]
            lista_com_todas_questoes.append(lista_com_uma_questao)
            # Adiciona o resultado na lista
        resultado_microdados = pd.DataFrame(lista_com_todas_questoes, columns=["QUAN_ACERTOS",
                                                                               "MÍNIMO", "MÉDIA",
                                                                               "MÁXIMO"])
        resultado_microdados.to_excel(f"{self.materia}ResultadoMicrodados.xlsx", index=False)

        return resultado_microdados
        # Cria o DataFrame e salva em xlsx
        print("Exportação concluída")
