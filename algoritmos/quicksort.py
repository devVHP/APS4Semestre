def quicksort(A, p, r):
    # Caso base: se o subarray contém 0 ou 1 elemento, não é necessário ordenar
    if p >= r:
        return
    
    # Particiona o array e obtém o índice 'q' do pivô após a partição
    q = partition(A, p, r)
    
    # Chama recursivamente o quicksort para os elementos à esquerda do pivô
    quicksort(A, p, q - 1)
    
    # Chama recursivamente o quicksort para os elementos à direita do pivô
    quicksort(A, q + 1, r)

def partition(A, p, r):
    # Inicializa o índice de separação 'q' no início do subarray
    q = p

    # Loop através dos elementos de 'p' até 'r - 1'
    for u in range(p, r):
        
        # Se o elemento atual for menor ou igual ao pivô (A[r]), faz a troca
        if A[u] <= A[r]:
            A[q], A[u] = A[u], A[q]  # Troca o elemento A[q] com A[u]
            q += 1  # Incrementa 'q' para manter a posição do próximo maior elemento
    
    # Coloca o pivô na posição correta (troca A[q] com A[r])
    A[q], A[r] = A[r], A[q]
    
    # Retorna o índice 'q', que é a nova posição do pivô
    return q
