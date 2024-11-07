def selection_sort(lst):
    n = len(lst)  # Obtém o tamanho da lista

    # Percorre cada posição da lista
    for i in range(n):
        # Assume que o menor elemento está na posição atual 'i'
        min_index = i

        # Percorre o restante da lista para encontrar o menor elemento
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:  # Compara o valor atual com o menor encontrado
                min_index = j  # Atualiza o índice do menor elemento encontrado

        # Troca o elemento atual (lst[i]) com o menor elemento encontrado (lst[min_index])
        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst  # Retorna a lista ordenada
