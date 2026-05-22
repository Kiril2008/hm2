############1

import time

def get_odd_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

start_range = int(input("Введіть початок діапазону: "))
end_range = int(input("Введіть кінець діапазону: "))

print(f"Непарні числа від {start_range} до {end_range}:")
for odd_num in get_odd_numbers(start_range, end_range):
    print(odd_num, end=" ")
print()

#2
def filter_values_outside_range(values_list, min_value, max_value):
    for value in values_list:
        if value < min_value or value > max_value:
            yield value

numbers = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(f"\nПочатковий список: {numbers}")

min_val = int(input("Введіть мінімальне значення діапазону: "))
max_val = int(input("Введіть максимальне значення діапазону: "))

filtered_numbers = list(filter_values_outside_range(numbers, min_val, max_val))
print(f"Значення поза діапазоном [{min_val}, {max_val}]: {filtered_numbers}")


#3

def draw_horizontal_line(symbol, length=20):
    print(symbol * length)

def draw_vertical_line(symbol, length=10):
    for _ in range(length):
        print(symbol)

def show_line(symbol, function_to_call):
    function_to_call(symbol)

user_symbol = input("\nВведіть символ для лінії: ")
line_type = input("Який тип лінії? (горизонтальна/вертикальна): ").lower()

if line_type == "горизонтальна":
    show_line(user_symbol, draw_horizontal_line)
elif line_type == "вертикальна":
    show_line(user_symbol, draw_vertical_line)
else:
    print("Невірний тип лінії!")


#4
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\nЧас виконання: {end - start:.5f} секунд")
        return result
    return wrapper

@measure_time
def get_even_numbers_0_to_100000():
    return [num for num in range(0, 100001) if num % 2 == 0]

print("\nОбчислення парних чисел від 0 до 100000...")
even_numbers = get_even_numbers_0_to_100000()
print(f"Знайдено {len(even_numbers)} парних чисел")
print("Перші 20:", even_numbers[:20])
print("Останні 20:", even_numbers[-20:])


#55

@measure_time
def get_even_numbers_in_range(start=0, end=100000):
    return [num for num in range(start, end + 1) if num % 2 == 0]

print("\nТестування з різними діапазонами:")

print("\n1. Діапазон 0-1000:")
r1 = get_even_numbers_in_range(0, 1000)
print(f"Знайдено {len(r1)}")

print("\n2. Діапазон 50-150:")
r2 = get_even_numbers_in_range(50, 150)
print(f"Знайдено {len(r2)}: {r2}")

print("\n3. Діапазон 0-500000:")
r3 = get_even_numbers_in_range(0, 500000)
print(f"Знайдено {len(r3)}")