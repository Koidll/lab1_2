def bubble_sort(numbers):
    """Сортировка списка методом пузырька по возрастанию"""
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == "__main__":
    print("Программа сортировки пузырьком по возрастанию")
    n = int(input("Введите количество чисел: "))

    numbers = []
    for i in range(n):
        num = float(input(f"Введите число {i + 1}: "))
        numbers.append(num)

    print("\nИсходный список:", numbers)
    sorted_numbers = bubble_sort(numbers)
    print("Отсортированный список:", sorted_numbers)
