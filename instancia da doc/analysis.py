from createFilesFolder import *
from runToAllCombination import *
from createGraphs import *

print('Iniciando algoritmo...')
createFilesFolder()
print('Executando AG 20x para cada uma das 81 combinações possíveis de variação de parâmetros... ')
runToAllCombination()
print('Gerando gráficos de cada combinação...')
createGraphs()
print('PRONTO!')