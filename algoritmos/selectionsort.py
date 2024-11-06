import random

def selection_sort(vetor):
    n = len(vetor)
    for i in range(n):
        k = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[k]:
                k = j
        if k != i:
            vetor[i], vetor[k] = vetor[k], vetor[i]

def main():
    n = 10
    max_value = 100
    
    # Gerando um vetor de números aleatórios
    vetor = [random.randint(0, max_value - 1) for _ in range(n)]
    
    print("Vetor aleatório =", vetor)

    # Ordenando o vetor
    selection_sort(vetor)
    
    print("Vetor ordenado =", vetor)

if __name__ == "__main__":
    main()


# https://www.italoinfo.com.br/algoritmos/selectionsort/