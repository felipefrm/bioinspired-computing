def func_obj(solucao, mochila):

    utilidade = peso = penalidade = 0

    for i in range(mochila.qtd_obj):
        if (solucao[i]):
            utilidade += mochila.utilidade[i]
            peso += mochila.peso[i]
        penalidade += mochila.peso[i]

    if peso <= mochila.capacidade:
        fitness = utilidade
        viavel = True
    else:
        fitness = utilidade * (1 - 5 * ((peso - mochila.capacidade)/mochila.capacidade))
        viavel = False
    # fitness = utilidade - penalidade * max(0, peso - mochila.capacidade);

    # print(f'fitness = {fitness} / solucao = {solucao}')
    return (fitness, viavel)