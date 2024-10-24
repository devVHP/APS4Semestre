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
#HeapSort
#MergeSort
#BucketSort
def bucket_sort(lista):
    balde = []
    n = len(lista)
    for i in range(n):
        balde.append([])
    for elemento in lista:
        indice = int(elemento*10)
        balde[indice].append(elemento)
    for i in range(n):
        balde[i] = sorted(balde[i])
    k = 0
    for i in range(n):
        for j in range(len(balde[i])):
            lista[k] = balde[i][j]
            k += 1
    return lista

lista = [.42, .32, .33, .52, .37, .47, .51]
bucket_sort(lista)
print(lista)


#MENU
