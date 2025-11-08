def even_bigger_10(numbers):
    # Возвращает список четных чисел больше 10 из заданного списка.
    result = []
    ostatok = []
    for num in numbers:
        if num % 2 == 0 and num > 10:
            result.append(num)
        else:
            ostatok.append(num)
    return f"Четные числа больше 10: {result}, оставшиеся: {ostatok}."
numbers_str = input("Введите числа, разделенные пробелом: ")
numbers_list = numbers_str.split()
numbers = []
for number in numbers_list:
    numbers.append(int(number))
result_list = even_bigger_10(numbers)
print(f"Четные числа больше 10: {result_list}")