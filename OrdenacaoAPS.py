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
        trocou = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista
    
#QuickSort
#InsertionSort
#BinaryInsertionSort
#SelectionSort
#HeapSort
#MergeSort
#BucketSort



#MENU