# Microdados Enem 2019
 Usa os microdados do ENEM e o Pandas para tentar prever a nota baseado na quantidade de acertos

## Divisão
O programa é dividido em 3 partes:
A primeira faz a filtragem dos dados selecionando apenas o que interessa
A segunda calcula a quantidade de acertos para cada candidato
A terceira mostra o resultado obtido, média, valores minimos e máximos

## Descrição
Os microdados são arquivos no formato .csv que contém varias informações sobre os canditados que fizeram a prova. O link de acesso:
https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados

Na parte de dicionários no arquivo dos microdados é possível ver todas as colunas do arquivo, seu significado e várias outras informações essenciais para entender o código. Por exemplo, os codígos para cada cor de prova estão descritos nos dicionários
## Informações para executar
Para executar é preciso ter o python e a bibliotaca do pandas instalados. Além de ter os microdados no mesmo local que o arquivo do python

O arquivo que mais demora para concluir é o segundo que precisa executar a função para calcular a quantidade de acertos 3707811 vezes. Para testar se estava funcionando deixei um notebook antigo ligado por mais de 6 dias.

Uma dica para quem converter o arquivo .py para .exe é que quando o programa executar vai salvar o resultado num arquivo e modifica-lo, nesse processo alguns anti-vírus costumam bloquear a ação e isso gera um erro no código.