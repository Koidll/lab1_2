def bubble_sort(numbers, ascending=True):
    """Сортировка списка методом пузырька.
    ascending=True — по возрастанию, False — по убыванию
    """
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if ascending:
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            else:
                if numbers[j] < numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == "__main__":
    print("Программа сортировки пузырьком (по возрастанию или по убыванию)")
    n = int(input("Введите количество чисел: "))

    numbers = []
    for i in range(n):
        num = float(input(f"Введите число {i + 1}: "))
        numbers.append(num)

    direction = input("Введите направление сортировки (asc - по возрастанию, desc - по убыванию): ").strip().lower()

    if direction == "desc":
        ascending = False
    else:
        ascending = True

    print("\nИсходный список:", numbers)
    sorted_numbers = bubble_sort(numbers, ascending)
    print("Отсортированный список:", sorted_numbers)
