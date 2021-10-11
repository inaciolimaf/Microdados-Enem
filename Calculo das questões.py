import pandas as pd

#Segunda parte para calcular a quantidade de acertos

# Função que calcula os acertos
def QuestAcertadas(codigo, respostas):
    # Prenche o gabarito baseado na cor da prova
    if codigo==503:
        gabarito= "AAECACDEADCBCDDDBCBDADAEABCEBABEEBCBEECEBDADC"
    elif codigo==504:
        gabarito= "BEEAAEBEEBADEADDADAEABCEDDDBCBCBCCACBCDADCCEB"
    elif codigo==505:
        gabarito= "DADCCEBBCCACBEEBEEBACBCDDDDADBCBBCEAEADEADAAE"
    elif codigo==506:
        gabarito= "DEADBAAAEBEECEBCBCBCBDADAEABCEDDDDADCBEECACBC"
    else:
        print(f"Deu muito errado. {codigo}")

    cont=0
    for i in range(0,len(respostas)):
        if respostas[i]==gabarito[i]:
            # Se a resposta e o gabarito for o mesmo soma 1 na contagem
            cont+=1

    return cont


print("Importando")
microdados=pd.read_csv("MicrodadosFiltrados.csv",sep=';', encoding='latin-1')
print("Importado")
# Importa os microdados

microdados['QuestAcertadas']='NaN'
# Cria a nova coluna

print("Iniciando o calculo:")
for i in range(0, 3707811):
    microdados.loc[i,'QuestAcertadas']=QuestAcertadas(microdados.iloc[i]['CO_PROVA_CN'], microdados.iloc[i]["TX_RESPOSTAS_CN"])
    # Para cada linha calcula a quantidade de questões acertadas usando a função
    print(i)
    # Imprime os valores para saber o progresso

print("Processo concluído. O resultado é:")
print(microdados)

print("Passando para o arquivo")
microdados.to_csv("MicrodadosFiltradosComQuest.csv", index=False, sep=';', encoding='latin-1')
print("Processo concluído")