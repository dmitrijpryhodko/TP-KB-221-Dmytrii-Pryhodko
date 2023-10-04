def find_pos(list, target):
    left, right = 0, len(list) - 1

    while left <= right:
        mid = (left + right) // 2

        if list[mid] == target:
            return mid  # Елемент вже присутній у списку
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Позиція для вставки нового елементу

# Приклад використання:
list = [1, 3, 5, 7, 9]
new_element = int(input("Введіть новий елемент: "))
position = find_pos(list, new_element)
print(f"Позиція для вставки {new_element} у список: {position}")
list.insert(position, new_element)
print(list)

