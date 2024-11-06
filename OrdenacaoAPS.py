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

#BubbleSort
def bubble_sort(lista):
    print("\n------BubbleSort------")
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compara o valor de 'dist' em cada dicionário
            if lista[j]["dist"] > lista[j + 1]["dist"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista   
    
#QuickSort


#InsertionSort
#BinaryInsertionSort
#SelectionSort
def selection_sort(lst):
    print("\n------SelectionSort------")
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
    print("\n------HeapSort------")
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
    print("\n------MergeSort------")
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
    print("\n------BucketSort------")
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

#Coordenadas

#Calcular a distância de uma coordenada a outra
import math

# Função para calcular a distância entre duas coordenadas usando a fórmula de Haversine
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


# Lista de coordenadas do CSV
import pandas as pd
from geopy.distance import geodesic

# Carrega os dados do arquivo CSV
# df = pd.read_csv('fotos.csv')

# # Extrai as coordenadas do primeiro ponto
# latitude_ref = df.loc[0, 'latitude']
# longitude_ref = df.loc[0, 'longitude']
# ponto_referencia = (latitude_ref, longitude_ref)

# # Calcula a distância do primeiro ponto para cada ponto no DataFrame
# distancias = []
# for i, row in df.iterrows():
#     ponto_atual = (row['latitude'], row['longitude'])
#     distancia_km = geodesic(ponto_referencia, ponto_atual).kilometers
#     distancias.append(distancia_km)

# # Atualiza a coluna "dist" com os valores calculados
# df['dist'] = distancias

# # Salva o DataFrame atualizado em um novo arquivo CSV
# df.to_csv('fotos_dist.csv', index=False)


#MENU
opcao = 0

while opcao != 5:
    opcao = int(input("""
------- ALGORITMOS DE ORDENAÇÃO --------

1 - Comparar dois algoritmos aleatórios
2 - Executar todos os algoritmos
3 - Buscar menor distância 
4 - Relatório
5 - Sair    

Escolha uma opção: """))
    if opcao > 5 or opcao < 1:
        print('Digite uma opção válida')
    lista = [1,6,5,9,10]
    if opcao == 1:
        import random
        functions = [bubble_sort, selection_sort, heap_sort, merge_sort, bucket_sort]

        # Escolher duas funções aleatórias
        random_function = random.sample(functions, 2)

        # Executar as funções escolhidas
        for func in random_function:
            # Leitura do arquivo CSV
            df = pd.read_csv('fotos_dist.csv')

            # Converte o DataFrame em uma lista de dicionários
            dados = df.to_dict(orient="records")

            # Ordena os dados usando Bubble Sort
            dados_ordenados = bubble_sort(dados)

            # Converte a lista de dicionários ordenada de volta para um DataFrame
            df_ordenado = pd.DataFrame(dados_ordenados)

            # Salva o DataFrame ordenado em um novo arquivo CSV
            df_ordenado.to_csv('dados_ordenados.csv', index=False)

            print("Dados ordenados salvos em 'dados_ordenados.csv'")
            func(lista)            
            system_info = get_system_info()
            for key, value in system_info.items():
                print(f"{key}: {value}")
        continuar = input("Aperte ENTER para continuar")

    