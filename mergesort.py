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