#FUNÇÕES
import platform
import psutil
def get_system_info():
    os_name = platform.system()
    os_version = platform.release()
    total_memory = psutil.virtual_memory().total / (1024.0 ** 3)
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq().current
    return {
        "SO": f"{os_name} {os_version}",
        "RAM": f"{total_memory:.2f} GB",
        "Cores": cpu_count,
        "Frequência": f"{cpu_freq} MHz"
}
system_info = get_system_info()
for key, value in system_info.items():
    print(f"{key}: {value}")

#BubbleSort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista      
    
#QuickSort


#InsertionSort
#BinaryInsertionSort
#SelectionSort
def selection_sort(lst):
    n = len(lst)  # Obtém o tamanho da lista

    # Percorre cada elemento da lista
    for i in range(n):
        # Assume que o menor elemento está na posição atual 'i'
        min_index = i

        # Percorre o restante da lista para encontrar o menor elemento
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:  # Compara os elementos
                min_index = j  # Atualiza o índice do menor elemento

        # Troca o elemento atual com o menor elemento encontrado
        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst  # Retorna a lista ordenada

#HeapSort
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

#MergeSort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Divide o array no meio
        left_half = arr[:mid]  # Primeira metade
        right_half = arr[mid:]  # Segunda metade

        # Chama recursivamente merge_sort para cada metade
        merge_sort(left_half)
        merge_sort(right_half)

        # Variáveis para iterar pelos arrays
        i = j = k = 0

        # Intercala os arrays divididos
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copia os elementos restantes de left_half, se houver
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copia os elementos restantes de right_half, se houver
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

#BucketSort
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


#MENU


#Coordenadas

#Calcular a distância de uma coordenada a outra
import math

def haversine(lat1, lon1, lat2, lon2):
    # Converte as coordenadas de graus para radianos
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Diferença das coordenadas
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Raio médio da Terra em quilômetros
    R = 6371.0
    distance = R * c
    return distance

# Coordenadas do CSV
lat1, lon1 = -9.982814549850332, -68.97692745741533
lat2, lon2 = -4.802369167118106, -58.617193971958855

# Calcula a distância
distancia = haversine(lat1, lon1, lat2, lon2)
print(f"A distância é de {distancia:.2f} km")

#Calcular um raio em volta da coordenada principal e ver quais coordenadas estão dentro desse raio

#Calcular a distância de cada coordenada dentro desse raio para a coordenada principal