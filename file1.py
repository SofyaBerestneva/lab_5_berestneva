def even_bigger_10(numbers):
    # result: Список четных чисел больше 10.
    # ostatok: Список оставшихся чисел.
    result = []
    ostatok = []
    for num in numbers:
        if num % 2 == 0 and num > 10:
            result.append(num)
        else:
            ostatok.append(num)
    return {'result': result, 'ostatok': ostatok}

def sort_results(results_dict):
    for key in results_dict:
        results_dict[key].sort()
    return results_dict

numbers_str = input("Введите числа, разделенные пробелом: ")
numbers_list = numbers_str.split()
numbers = []
for number in numbers_list:
    numbers.append(int(number))
results_dict = even_bigger_10(numbers)
sorted_results = sort_results(results_dict)
final_result = sorted_results['result']
final_ostatok = sorted_results['ostatok']
print(f"Четные числа больше 10: {final_result}")
print(f"Оставшиеся числа: {final_ostatok}")