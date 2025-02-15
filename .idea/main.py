def filter_short_strings(arr):
    """Фильтрует массив строк, оставляя только строки длиной <=3 символов"""
    return [s for s in arr if len(s) <= 3] #Используем списковое включение

#Ввод массива строк с клавиатурым (разделение по пробелам)
input_array = input("Введите строки через пробел: ").split()

#Фильтрация массива
filtered_array = filter_short_strings(input_array)

#Вывод результата
print("Результат:",  filtered_array)