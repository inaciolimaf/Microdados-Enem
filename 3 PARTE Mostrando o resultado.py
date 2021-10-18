import pandas as pd

# Terceira parte para mostrar o resultado

print("Importando")
microdados=pd.read_csv("MicrodadosFiltradosComQuest.csv",sep=';', encoding='latin-1')
print("Importado")
# Importa os microdados

for i in range(0,45+1):
    # Laço para cada valor de acertos
    print(f'QUANTIDADE DE ACERTOS: {i}')
    MicroComQuestão=microdados.loc[microdados['QuestAcertadas']==i]
    # Localiza os dados com uma quantidade de acertos específica
    minimo=MicroComQuestão['NU_NOTA_CN'].min()
    media=MicroComQuestão['NU_NOTA_CN'].mean()
    maximo=MicroComQuestão['NU_NOTA_CN'].max()
    # Calcula o mínimo, a media e o máximo
    print(f'O valor mínimo é {minimo}')
    print(f'O valor médio é {media}')
    print(f'O valor máximo é {maximo}')
    resp=input("Precione enter para ir para o próximo valor\nou digite \"info\" para mais informações:")
    if resp=="info":
        print(MicroComQuestão['NU_NOTA_CN'].describe())
        # Mostra os dados mais detalhados se for pedido
    print()
    print('#'*30)
    print()
print("Concluído.")