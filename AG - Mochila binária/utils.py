diretorioInstancias = 'instancias'

def leArquivos(instancia):

    if instancia not in ['01', '02', '03', '04', '05', '06', '07', '08']:
        print("Falha na leitura do arquivo de instância, por favor, use uma das instâncias disponíveis.")
        exit()

    capacidadeArq = "p" + instancia + "_c.txt"
    pesosArq = "p" + instancia + "_w.txt" 
    utilidadesArq = "p" + instancia + "_p.txt" 
    solucaoArq = "p" + instancia + "_s.txt" 

    pesos = []
    utilidades = []
    solucao = []

    with open(diretorioInstancias + '/' + capacidadeArq, 'r') as f:
        capacidade = int(f.readline())

    with open(diretorioInstancias + '/' + pesosArq, 'r') as f:
        for line in f:
            pesos.append(int(line))

    with open(diretorioInstancias + '/' + utilidadesArq, 'r') as f:
        for line in f:
            utilidades.append(int(line))

    with open(diretorioInstancias + '/' + solucaoArq, 'r') as f:
        for line in f:
            solucao.append(int(line))

    return (capacidade, pesos, utilidades, solucao)


def quantidadeObjetos(array):
    return len(array)
