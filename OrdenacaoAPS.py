#FUNÇÕES
import platform
import psutil
import csv
import random
import time
import math
import pymysql
from datetime import datetime
import os

#Conexão banco de dados
conexao = pymysql.connect(
    host="localhost",
    user="admin",
    password="123",
    database="aps4semestre",
    port=3307
)
cursor = conexao.cursor()

#Informações sistema operacional
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

#Relatório
def relatorio_print(alg):
    cursor.execute("SELECT * FROM relatorio WHERE algoritmo = %s", (alg,))
    resultados = cursor.fetchall()
    
    # Cabeçalho
    print(f"\n\nRELATÓRIO DO {alg.upper()}")
    print(f"{'Qtd Registros':<15} {'Data Execução':<15} {'Hora Execução':<20} {'Algoritmo':<25} {'Tempo':<10} {'Sistema Operacional':<20} {'RAM':<10} {'CPU Cores':<10} {'Frequência CPU':<15}")
    print("-" * 150)
    
    # Dados
    for linha in resultados:
        qtd_registros = linha[0]
        data_exec = linha[1].strftime("%d/%m/%Y")  # Formatar a data
        hora_exec = str(linha[2])  # Converte timedelta para string
        algoritmo = linha[3]
        tempo = linha[4]
        sistema_op = linha[5]
        ram = linha[6]
        cpu_core = linha[7]
        cpt_frequencia = linha[8]

        # Exibindo os dados
        print(f"{qtd_registros:<15} {data_exec:<15} {hora_exec:<20} {algoritmo:<25} {tempo:<10} {sistema_op:<20} {ram:<10} {cpu_core:<10} {cpt_frequencia:<15}")


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
    os.system('cls')
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
        os.system('cls')
        print("COMPARAÇÃO DE DOIS ALGORITMOS ALEATÓRIOS")
        functions = [bubble_sort, selection_sort, heap_sort, merge_sort, bucket_sort, insertion_sort, binary_insertion_sort, quick_sort]

        # Escolher duas funções aleatórias
        random_function = random.sample(functions, 2)

        # Executar as funções escolhidas
        for func in random_function:
            data_atual = datetime.now().date()
            hora_atual = datetime.now().strftime("%H:%M")
            inicio = time.time()
            print(f'\n------{func.__name__}------')
            # Leitura do arquivo CSV e conversão para uma lista de dicionários
            dados = []
            with open('fotos.dist.csv', 'r') as file:
                reader = csv.DictReader(file)
                qtd_registros = 0
                for row in reader:
                    # Converte o campo 'dist' para float para realizar a ordenação
                    row['dist'] = float(row['dist'])
                    dados.append(row)
                    qtd_registros = qtd_registros+1

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

            print(f"""Quantidade de registros: {qtd_registros} 
Data: {data_atual} 
Hora: {hora_atual}
Tempo de execução: {tempo:.2f} segundos""")
            cursor.execute(
    """
    INSERT INTO relatorio 
    (qtd_registros, data_exec, hora_exec, algoritmo, tempo, sistema_op, ram, cpu_core, cpu_frequencia)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """,
    (
        qtd_registros,
        data_atual,
        hora_atual,
        func.__name__,
        f"{tempo:.2f}s",
        platform.system()+platform.release(),
        f"{psutil.virtual_memory().total / (1024.0 ** 3):.2f}GB",
        psutil.cpu_count(),
        f"{psutil.cpu_freq().current}MHz"
    )
)
            conexao.commit()
            for key, value in system_info.items():
                print(f"{key}: {value}")
        continuar = input("\nAperte ENTER para continuar")

    if opcao == 2:
        os.system('cls')
        print("EXECUÇÃO DE TODOS OS ALGORITMOS")
        functions = [bubble_sort, selection_sort, heap_sort, merge_sort, bucket_sort, insertion_sort, binary_insertion_sort, quick_sort]

        # Escolher duas funções aleatórias
        random_function = random.sample(functions, 8)

        # Executar as funções escolhidas
        for func in random_function:
            data_atual = datetime.now().date()
            hora_atual = datetime.now().strftime("%H:%M")
            inicio = time.time()
            print(f'\n------{func.__name__}------')
            # Leitura do arquivo CSV e conversão para uma lista de dicionários
            dados = []
            with open('fotos.dist.csv', 'r') as file:
                reader = csv.DictReader(file)
                qtd_registros = 0
                for row in reader:
                    # Converte o campo 'dist' para float para realizar a ordenação
                    row['dist'] = float(row['dist'])
                    dados.append(row)
                    qtd_registros = qtd_registros+1

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
            print(f"""Quantidade de registros: {qtd_registros} 
Data: {data_atual} 
Hora: {hora_atual}
Tempo de execução: {tempo:.2f} segundos""")
            cursor.execute(
    """
    INSERT INTO relatorio 
    (qtd_registros, data_exec, hora_exec, algoritmo, tempo, sistema_op, ram, cpu_core, cpu_frequencia)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """,
    (
        qtd_registros,
        data_atual,
        hora_atual,
        func.__name__,
        f"{tempo:.2f}s",
        platform.system()+platform.release(),
        f"{psutil.virtual_memory().total / (1024.0 ** 3):.2f}GB",
        psutil.cpu_count(),
        f"{psutil.cpu_freq().current}MHz"
    )
)
            conexao.commit()
            for key, value in system_info.items():
                print(f"{key}: {value}")
        continuar = input("\nAperte ENTER para continuar")

    if opcao == 3:
        os.system('cls')
        print("MENORES DISTÂNCIAS DO PRIMEIRO PONTO")
        # Tamanho do terminal ou da largura da saída
        largura = 50  # Ajuste conforme necessário
        distancia = float(input("Digite a distância em KM: "))
        # Abre o arquivo CSV
        with open('coordenadas_ordenadas.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Lê o cabeçalho
            dados = list(reader)  # Lê todos os dados no arquivo

            # Imprime o título centralizado
            print(f"--------MENORES DISTÂNCIAS EM UM RAIO DE {distancia}KM--------".center(largura))

            # Imprime o cabeçalho centralizado
            print(f"{header[0]:<10}{header[4]:>10}".center(largura))

            # Loop para verificar e imprimir as distâncias menores que 50
            for row in dados:
                distanciax = float(row[4])  # Converte a distância para float
                if distanciax < distancia:  # Verifica se a distância é menor que 50
                    print(f"{row[0]:<10}{row[4]:>10}".center(largura))
        continuar = input("\nAperte ENTER para continuar")

    if opcao == 4:
        os.system('cls')
        print("ARÉA DE RELATÓRIOS")
        contador = 1
        functions = [bubble_sort, selection_sort, heap_sort, merge_sort, bucket_sort, insertion_sort, binary_insertion_sort, quick_sort]
        # Executar as funções escolhidas
        print("-----------------------------------\n")
        for func in functions:
            print(contador, func.__name__)
            contador += 1
        escolha = int(input("\nDigite o número do algoritmo que deseja: "))
        if escolha == 1:
            relatorio_print('bubble_sort')
        if escolha == 2:
            relatorio_print('selection_sort')
        if escolha == 3:
            relatorio_print('heap_sort')
        if escolha == 4:
            relatorio_print('merge_sort')
        if escolha == 5:
            relatorio_print('bucket_sort')
        if escolha == 6:
            relatorio_print('insertion_sort')
        if escolha == 7:
            relatorio_print('binary_insertion_sort')
        if escolha == 8:
            relatorio_print('quick_sort4')
        continuar = input("\nAperte ENTER para continuar")
cursor.close()
conexao.close()