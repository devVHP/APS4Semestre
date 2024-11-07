def binary_insertion_sort(arr):
    # Função auxiliar para encontrar o índice de inserção usando busca binária
    def binary_search(sub_arr, key_dist, start, end):
        # Enquanto houver uma faixa válida para busca
        while start < end:
            mid = (start + end) // 2
            # Compara o valor do meio com a chave de busca
            if sub_arr[mid] < key_dist:
                start = mid + 1
            else:
                end = mid
        return start
    
    # Percorre a lista a partir do segundo elemento
    for i in range(1, len(arr)):
        # Elemento atual a ser inserido
        key = arr[i]
        
        # Encontra a posição correta de inserção usando busca binária na parte ordenada
        pos = binary_search(arr, key, 0, i)
        
        # Move todos os elementos para a direita para abrir espaço para o key
        j = i
        while j > pos:
            arr[j] = arr[j - 1]
            j -= 1
        
        # Insere o key na posição encontrada
        arr[pos] = key

    return arr
