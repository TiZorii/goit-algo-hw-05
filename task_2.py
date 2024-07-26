def binary_search(sorted_array, target):
    left, right = 0, len(sorted_array) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2
        iterations += 1
        
        if sorted_array[mid] < target:
            left = mid + 1
        elif sorted_array[mid] > target:
            right = mid - 1
        else:
            return iterations, sorted_array[mid]

    if right < 0:
        return iterations, sorted_array[0]
    elif left >= len(sorted_array):
        return iterations, None
    else:
        return iterations, sorted_array[left]

# Приклад використання:
sorted_array = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
target = 3.5

iterations, upper_bound = binary_search(sorted_array, target)
print(f"Кількість ітерацій: {iterations}")
print(f"Верхня межа: {upper_bound}")
