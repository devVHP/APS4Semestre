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
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compara o valor de 'dist' em cada dicionário
            if lista[j]["dist"] > lista[j + 1]["dist"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista   
    
#QuickSort
def quick_sort(arr):
    # Caso base: se o array tem 0 ou 1 elementos, já está ordenado
    if len(arr) <= 1:
        return arr
    
    # Escolhe o pivô (neste caso, o elemento central)
    pivot = arr[len(arr) // 2]["dist"]

    # Divide a lista em três partes: menor, igual, e maior que o pivô
    left = [x for x in arr if x["dist"] < pivot]
    middle = [x for x in arr if x["dist"] == pivot]
    right = [x for x in arr if x["dist"] > pivot]

    # Ordena recursivamente as sublistas e concatena os resultados
    return quick_sort(left) + middle + quick_sort(right)

#InsertionSort
def insertion_sort(arr):
    # Percorre cada elemento da lista começando pelo segundo
    for i in range(1, len(arr)):
        # Seleciona o elemento atual
        key = arr[i]
        
        # Move os elementos de arr[0..i-1] que são maiores que key["dist"]
        # para uma posição à frente de sua posição atual
        j = i - 1
        while j >= 0 and arr[j]["dist"] > key["dist"]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Coloca o key na posição correta
        arr[j + 1] = key

    return arr

#BinaryInsertionSort
def binary_insertion_sort(arr):
    # Função auxiliar para encontrar o índice de inserção usando busca binária
    def binary_search(sub_arr, key_dist, start, end):
        # Enquanto houver uma faixa válida para busca
        while start < end:
            mid = (start + end) // 2
            # Compara o valor de 'dist' do meio com a chave de busca
            if sub_arr[mid]["dist"] < key_dist:
                start = mid + 1
            else:
                end = mid
        return start
    
    # Percorre a lista a partir do segundo elemento
    for i in range(1, len(arr)):
        # Elemento atual a ser inserido
        key = arr[i]
        # Encontra a posição correta de inserção usando busca binária na parte ordenada
        pos = binary_search(arr, key["dist"], 0, i)
        
        # Move todos os elementos para a direita para abrir espaço para o key
        j = i
        while j > pos:
            arr[j] = arr[j - 1]
            j -= 1
        
        # Insere o key na posição encontrada
        arr[pos] = key

    return arr

#SelectionSort
def selection_sort(lst):
    n = len(lst)  # Obtém o tamanho da lista

    # Percorre cada elemento da lista
    for i in range(n):
        # Assume que o menor elemento está na posição atual 'i'
        min_index = i

        # Percorre o restante da lista para encontrar o menor elemento
        for j in range(i + 1, n):
            if lst[j]["dist"] < lst[min_index]["dist"]:  # Compara o campo 'dist' nos dicionários
                min_index = j  # Atualiza o índice do menor elemento

        # Troca o elemento atual com o menor elemento encontrado
        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst  # Retorna a lista ordenada

#HeapSort
def heap_sort(arr):
    n = len(arr)

    # Função para transformar o array em um heap máximo
    for i in range(n // 2 - 1, -1, -1):
        # Constrói o heap máximo a partir do índice i
        k = i
        while True:
            largest = k
            left = 2 * k + 1
            right = 2 * k + 2

            if left < n and arr[left]["dist"] > arr[largest]["dist"]:
                largest = left
            if right < n and arr[right]["dist"] > arr[largest]["dist"]:
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

            if left < i and arr[left]["dist"] > arr[largest]["dist"]:
                largest = left
            if right < i and arr[right]["dist"] > arr[largest]["dist"]:
                largest = right

            if largest != k:
                arr[k], arr[largest] = arr[largest], arr[k]
                k = largest
            else:
                break

    return arr

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
            if left_half[i]["dist"] < right_half[j]["dist"]:  # Compara o valor de 'dist'
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

    return arr

#BucketSort
def bucket_sort(lst):
    # Inicializa uma lista vazia de baldes
    n = len(lst)  # Define o número de baldes com base no tamanho da lista
    buckets = [[] for _ in range(n)]  # Cria 'n' baldes vazios

    # Encontra o valor máximo em 'dist' para normalizar as distribuições nos baldes
    max_dist = max(item["dist"] for item in lst)

    # Distribui cada elemento da lista no balde apropriado
    for element in lst:
        index = int(element["dist"] / max_dist * (n - 1))  # Calcula o índice do balde
        buckets[index].append(element)  # Adiciona o elemento ao balde correspondente

    # Ordena cada balde individualmente (aqui usando sorted)
    for i in range(n):
        buckets[i] = sorted(buckets[i], key=lambda x: x["dist"])  # Ordena pelo valor de 'dist'

    # Junta todos os elementos dos baldes de volta na lista original, agora ordenada
    k = 0  # Índice para atualizar a lista original
    for i in range(n):
        for j in range(len(buckets[i])):
            lst[k] = buckets[i][j]  # Copia o elemento do balde para a lista
            k += 1  # Move para o próximo índice da lista

    return lst  # Retorna a lista ordenada

#Coordenadas
# Função para calcular a distância entre duas coordenadas usando a fórmula de Haversine

import csv
import math

def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    raio_terra = 6371.0  # Raio da Terra em km
    return raio_terra * c

# Abrindo e lendo o arquivo CSV
with open('fotos.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Lê o cabeçalho
    dados = list(reader)

# Pega o primeiro ponto como referência
lat_ref = float(dados[0][1])  # Latitude da primeira linha
lon_ref = float(dados[0][2])  # Longitude da primeira linha

# Calcula a distância e atualiza a coluna 'dist' (coluna 4)
for row in dados:
    # Verifica se a linha tem pelo menos 3 colunas
    if len(row) > 2:
        lat = float(row[1])
        lon = float(row[2])
        distancia = haversine(lat_ref, lon_ref, lat, lon)  # Calcula a distância
        row[4] = f"{distancia:.2f}"  # Atualiza o valor da distância com 2 casas decimais
    else:
        print(f"Linha mal formatada ou vazia: {row}")

# Salva o arquivo atualizado com as distâncias calculadas
with open('fotos.dist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Escreve o cabeçalho
    writer.writerows(dados)  # Escreve os dados atualizados

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
    if opcao == 1:
        import time
        inicio = time.time()
        import random
        functions = [bubble_sort, selection_sort, heap_sort, merge_sort, bucket_sort, insertion_sort, binary_insertion_sort, quick_sort]

        # Escolher duas funções aleatórias
        random_function = random.sample(functions, 2)

        # Executar as funções escolhidas
        for func in random_function:
            print(f'\n------{func.__name__}------')
            # Leitura do arquivo CSV e conversão para uma lista de dicionários
            dados = []
            with open('fotos.dist.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Converte o campo 'dist' para float para realizar a ordenação
                    row['dist'] = float(row['dist'])
                    dados.append(row)

            # Ordena os dados usando Bubble Sort
            dados_ordenados = func(dados)

            # Escreve os dados ordenados em um novo arquivo CSV
            with open('coordenadas_ordenadas.csv', 'w', newline='') as file:
                fieldnames = dados[0].keys()  # Pega as chaves do dicionário para usar como cabeçalho
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                writer.writeheader()  # Escreve o cabeçalho
                writer.writerows(dados_ordenados)  # Escreve os dados ordenados   

            system_info = get_system_info()
            fim = time.time()
            tempo =  fim - inicio
            print(f'Tempo de execução: {tempo:.2f} segundos')
            for key, value in system_info.items():
                print(f"{key}: {value}")
        continuar = input("\nAperte ENTER para continuar")

    if opcao == 2:
        import time
        inicio = time.time()
        import random
        functions = [bubble_sort, selection_sort, heap_sort, merge_sort, bucket_sort, insertion_sort, binary_insertion_sort, quick_sort]

        # Escolher duas funções aleatórias
        random_function = random.sample(functions, 8)

        # Executar as funções escolhidas
        for func in random_function:
            print(f'\n------{func.__name__}------')
            # Leitura do arquivo CSV e conversão para uma lista de dicionários
            dados = []
            with open('fotos.dist.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Converte o campo 'dist' para float para realizar a ordenação
                    row['dist'] = float(row['dist'])
                    dados.append(row)

            # Ordena os dados usando Bubble Sort
            dados_ordenados = func(dados)

            # Escreve os dados ordenados em um novo arquivo CSV
            with open('coordenadas_ordenadas.csv', 'w', newline='') as file:
                fieldnames = dados[0].keys()  # Pega as chaves do dicionário para usar como cabeçalho
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                writer.writeheader()  # Escreve o cabeçalho
                writer.writerows(dados_ordenados)  # Escreve os dados ordenados   

            system_info = get_system_info()
            fim = time.time()
            tempo =  fim - inicio
            print(f'Tempo de execução: {tempo:.2f} segundos')
            for key, value in system_info.items():
                print(f"{key}: {value}")
        continuar = input("\nAperte ENTER para continuar")

    if opcao == 3:
        import csv

        # Tamanho do terminal ou da largura da saída
        largura = 50  # Ajuste conforme necessário

        # Abre o arquivo CSV
        with open('coordenadas_ordenadas.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Lê o cabeçalho
            dados = list(reader)  # Lê todos os dados no arquivo

            # Imprime o título centralizado
            print("--------MENORES DISTÂNCIAS EM UM RAIO DE 50KM--------".center(largura))

            # Imprime o cabeçalho centralizado
            print(f"{header[0]:<10}{header[4]:>10}".center(largura))

            # Loop para verificar e imprimir as distâncias menores que 50
            for row in dados:
                distancia = float(row[4])  # Converte a distância para float
                if distancia < 50:  # Verifica se a distância é menor que 50
                    print(f"{row[0]:<10}{row[4]:>10}".center(largura))
        continuar = input("\nAperte ENTER para continuar")
