def func_obj(solucao, mochila):

    utilidade = peso = 0

    for i in range(mochila.qtd_obj):
        if (solucao[i]):
            utilidade += mochila.utilidade[i]
            peso += mochila.peso[i]

    if peso <= mochila.capacidade:
        fitness = utilidade
        viavel = True
    else:
        fitness = utilidade * (1 - 5 * ((peso - mochila.capacidade)/mochila.capacidade))
        viavel = False
 
    return (fitness, viavel)