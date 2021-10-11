import pandas as pd

# Primeira parte para filtragem de dados

#Lista com as colunas mais utéis que estão nos microdados
'''Colunas=['NU_INSCRICAO', 'NO_MUNICIPIO_ESC', 'CO_PROVA_CN', 'CO_PROVA_CH', 'CO_PROVA_LC',
'CO_PROVA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'TP_LINGUA', 'TX_GABARITO_CN',
'TX_GABARITO_CH', 'TX_GABARITO_LC', 'TX_GABARITO_MT', 'TP_STATUS_REDACAO', 'NU_NOTA_REDACAO']'''

Colunas=['CO_PROVA_CN', 'NU_NOTA_CN', 'TX_RESPOSTAS_CN']
# Colunas que seram usadas para Ciencias da Natureza
# Informações do significado estão na parte de dicionários dos microdados 

print("Importando...")
microdados=pd.read_csv("MICRODADOS_ENEM_2019.csv", sep=';', encoding='latin-1', usecols=Colunas)
print("Importado")
# Importando os microdados

# Este passo serve para tirar as outras provas, como reaplicação e os valores nulos
print("Iniciando a filtragem dos dados")
ListaDeUsados=[503.0,504.0,505.0,506.0]
# Lista com os valores para serem usados, cada um indica o codido referente a uma cor de uma prova da aplicação regular

for i,num in enumerate(ListaDeUsados):
    if i==0:
        # Se for a primeira vez no laço é preciso criar um novo dataframe
        MicroFiltrados=microdados.loc[microdados['CO_PROVA_CN']==num]
        # Localiza nos microdados o valor de num e atribui à MicroFiltrados
        NovosMicrodados=MicroFiltrados
        # Cria o dataframe "NovosMicrodados"
    else:
        # Senão for a primeira vez é preciso fundir(merge) os dois dataframes
        MicroFiltrados=microdados.loc[microdados['CO_PROVA_CN']==num]
        NovosMicrodados=pd.merge(NovosMicrodados, MicroFiltrados, how='outer')
        # Juntando os dataframes
print("Filtragem concluída. O resultado é:")
print(NovosMicrodados)

print("Exportando...")
NovosMicrodados.to_csv("MicrodadosFiltrados.csv", index=False, sep=';', encoding='latin-1')
print("Processo concluído")
# Exportando os dados filtrados