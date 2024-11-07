def insertion_sort(arr):
    # Percorre cada elemento da lista a partir do segundo
    for i in range(1, len(arr)):
        # Seleciona o elemento atual para ser inserido na parte ordenada
        key = arr[i]
        
        # Inicializa j como o índice anterior a i
        j = i - 1
        
        # Move elementos maiores que key uma posição para a direita
        # para abrir espaço para o key na posição correta
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insere o key na posição correta da parte ordenada
        arr[j + 1] = key

    return arr
