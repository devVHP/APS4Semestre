def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            
            if lista[j] > lista[j + 1]:  
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista  

def bubble_sort(lista):
    # Define o número de elementos na lista
    n = len(lista)

    # Loop externo para passar por toda a lista n vezes
    for i in range(n):
        
        # Loop interno para comparar os elementos adjacentes
        # À medida que i aumenta, não precisamos comparar os últimos elementos,
        # pois eles já estão ordenados, então o limite é 'n - i - 1'
        for j in range(0, n - i - 1):
            
            # Verifica se o elemento atual é maior que o próximo
            if lista[j] > lista[j + 1]:  
                # Se for, troca de posição com o próximo elemento
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    # Retorna a lista ordenada após todas as iterações
    return lista  