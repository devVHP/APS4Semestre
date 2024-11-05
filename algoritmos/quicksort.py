def quicksort(A, p, r):
    if p >= r:
        return
    q = partition(A, p, r)
    quicksort(A, p, q - 1)
    quicksort(A, q + 1, r)

def partition(A, p, r):
    q = p
    for u in range(p, r):
        if A[u] <= A[r]:
            A[q], A[u] = A[u], A[q]  # Troca A[q] por A[u]
            q += 1
    A[q], A[r] = A[r], A[q]  # Troca A[q] por A[r]
    return q

# Exemplo de uso
A = [11, 8, 1, 3, 2]
quicksort(A, 0, len(A) - 1)
print(A)