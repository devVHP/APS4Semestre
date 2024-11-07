def heap_sort(arr):
    n = len(arr)  # Tamanho do array

    # Constrói um heap máximo a partir da metade da lista até o início
    for i in range(n // 2 - 1, -1, -1):
        # Ajusta o heap máximo começando pelo índice i
        k = i
        while True:
            largest = k
            left = 2 * k + 1  # Índice do filho à esquerda
            right = 2 * k + 2  # Índice do filho à direita

            # Se o filho à esquerda é maior que o nó atual, atualiza o maior
            if left < n and arr[left] > arr[largest]:
                largest = left
            # Se o filho à direita é maior que o maior atual, atualiza o maior
            if right < n and arr[right] > arr[largest]:
                largest = right

            # Se o maior elemento não é o nó atual, troca e continua ajustando o heap
            if largest != k:
                arr[k], arr[largest] = arr[largest], arr[k]
                k = largest  # Move para o próximo nó
            else:
                break  # Sai do loop se o heap já estiver organizado

    # Extrai os elementos um a um do heap e ajusta o heap após cada remoção
    for i in range(n - 1, 0, -1):
        # Move o maior elemento (na raiz do heap) para o final do array
        arr[0], arr[i] = arr[i], arr[0]

        # Reduz o tamanho do heap e reorganiza o heap máximo para o restante do array
        k = 0
        while True:
            largest = k
            left = 2 * k + 1
            right = 2 * k + 2

            # Reajusta o heap considerando apenas a porção ainda não ordenada
            if left < i and arr[left] > arr[largest]:
                largest = left
            if right < i and arr[right] > arr[largest]:
                largest = right

            if largest != k:
                arr[k], arr[largest] = arr[largest], arr[k]
                k = largest
            else:
                break

    return arr
