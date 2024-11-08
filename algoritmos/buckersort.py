def bucket_sort(lst):
    n = len(lst)  
    buckets = [[] for _ in range(n)]

    max_value = max(lst)

    for element in lst:
        index = int(element / max_value * (n - 1))
        buckets[index].append(element)

    for i in range(n):
        buckets[i] = sorted(buckets[i])

    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            lst[k] = buckets[i][j]
            k += 1

    return lst





def bucket_sort(lst):
    # Define o número de baldes com base no tamanho da lista
    n = len(lst)  
    # Inicializa uma lista vazia de baldes
    buckets = [[] for _ in range(n)]  # Cria 'n' baldes vazios

    # Encontra o valor máximo na lista para normalizar as distribuições nos baldes
    max_value = max(lst)

    # Distribui cada elemento da lista no balde apropriado
    for element in lst:
        index = int(element / max_value * (n - 1))  # Calcula o índice do balde
        buckets[index].append(element)  # Adiciona o elemento ao balde correspondente

    # Ordena cada balde individualmente (aqui usando sorted)
    for i in range(n):
        buckets[i] = sorted(buckets[i])  # Ordena os elementos de cada balde

    # Junta todos os elementos dos baldes de volta na lista original, agora ordenada
    k = 0  # Índice para atualizar a lista original
    for i in range(n):
        for j in range(len(buckets[i])):
            lst[k] = buckets[i][j]  # Copia o elemento do balde para a lista
            k += 1  # Move para o próximo índice da lista

    return lst  # Retorna a lista ordenada