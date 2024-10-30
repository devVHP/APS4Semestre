def bucket_sort(lst):
    # Inicializa uma lista vazia de baldes
    buckets = []
    n = len(lst)  # Define o número de baldes com base no tamanho da lista

    # Cria 'n' baldes vazios
    for i in range(n):
        buckets.append([])

    # Distribui cada elemento da lista no balde apropriado
    for element in lst:
        index = int(element * 10)  # Calcula o índice do balde
        buckets[index].append(element)  # Adiciona o elemento ao balde correspondente

    # Ordena cada balde individualmente
    for i in range(n):
        buckets[i] = sorted(buckets[i])

    # Junta todos os elementos dos baldes de volta na lista original, agora ordenada
    k = 0  # Índice para atualizar a lista original
    for i in range(n):
        for j in range(len(buckets[i])):
            lst[k] = buckets[i][j]  # Copia o elemento do balde para a lista
            k += 1  # Move para o próximo índice da lista

    return lst  # Retorna a lista ordenada