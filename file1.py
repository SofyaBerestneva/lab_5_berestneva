import random
def even_bigger_10(numbers):
    # result: Список чётных чисел больше 10.
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
# Генерируем список из 20 случайных чисел от 0 до 100 и добавляем их с помощью цикла
numbers = [random.randint(0, 100) for _ in range(20)]
print(f"Сгенерированные числа: {numbers}")
results_dict = even_bigger_10(numbers)
sorted_results = sort_results(results_dict)
final_result = sorted_results['result']
final_ostatok = sorted_results['ostatok']
print(f"Чётные числа больше 10: {final_result}")
print(f"Оставшиеся числа: {final_ostatok}")