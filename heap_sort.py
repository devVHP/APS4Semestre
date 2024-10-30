def heap_sort(arr):
    n = len(arr)

    # Função para transformar o array em um heap máximo
    for i in range(n // 2 - 1, -1, -1):
        # heapify para construir o heap
        k = i
        while True:
            largest = k
            left = 2 * k + 1
            right = 2 * k + 2

            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != k:
                arr[k], arr[largest] = arr[largest], arr[k]
                k = largest
            else:
                break

    # Extrai elementos um por um do heap
    for i in range(n - 1, 0, -1):
        # Move o maior elemento (na raiz) para o final do array
        arr[0], arr[i] = arr[i], arr[0]

        # Reduz o tamanho do heap e reorganiza o heap máximo
        k = 0
        while True:
            largest = k
            left = 2 * k + 1
            right = 2 * k + 2

            if left < i and arr[left] > arr[largest]:
                largest = left
            if right < i and arr[right] > arr[largest]:
                largest = right

            if largest != k:
                arr[k], arr[largest] = arr[largest], arr[k]
                k = largest
            else:
                break