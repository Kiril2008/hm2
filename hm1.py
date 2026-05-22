from functools import reduce
import math
def create_student_record(name, *grades):
    return (name, grades)

def calculate_average(student_record):
    grades = student_record[1]
    return sum(grades) / len(grades)

def find_best_student(students):
    return max(students, key=lambda s: calculate_average(s))

def count_excellent_students(students, threshold=90):
    return len(list(filter(lambda s: calculate_average(s) > threshold, students)))


# Тест
students = [
    create_student_record("Олексій", 85, 92, 78, 88),
    create_student_record("Марина", 95, 89, 92, 87),
    create_student_record("Дмитро", 76, 82, 79, 85),
    create_student_record("Анна", 98, 94, 96, 91)
]

print("Студенти та їх середні оцінки:")
for student in students:
    avg = calculate_average(student)
    print(f"{student[0]}: {avg:.1f}")

best = find_best_student(students)
print(f"\nНайкращий студент: {best[0]} ({calculate_average(best):.1f})")

excellent_count = count_excellent_students(students, 90)
print(f"Студентів з середньою оцінкою >90: {excellent_count}")

#2
def add_book(library, isbn, title, author, year, genre):
    library[isbn] = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'available': True
    }

def remove_book(library, isbn):
    library.pop(isbn, None)

def search_by_author(library, author):
    return [isbn for isbn, book in library.items() if book['author'] == author]

def search_by_genre(library, genre):
    return [isbn for isbn, book in library.items() if book['genre'] == genre]

def search_by_year_range(library, start_year, end_year):
    return [isbn for isbn, book in library.items() if start_year <= book['year'] <= end_year]

def borrow_book(library, isbn):
    if isbn in library and library[isbn]['available']:
        library[isbn ]['available'] = False

def return_book(library, isbn):
    if isbn  in library:
        library[isbn]['available'] = True

def get_available_books(library):
    return [isbn for isbn, book in library.items() if book['available']]

def get_library_statistics(library):
    total = len(library)
    available = len(get_available_books(library))
    borrowed= total -  available
    return {
        'total': total,
        'available': available,
        'borrowed': borrowed
    }
#3
employees = [
 {'name': 'Олексій', 'department': 'IT', 'salary': 45000, 'experience': 3, 'performance': 8. 5},
 {'name': 'Марина', 'department': 'HR', 'salary': 35000, 'experience': 5, 'performance': 9.2},
 {'name': 'Дмитро', 'department': 'IT', 'salary': 55000, 'experience': 7, 'performance': 8.8},
 {'name': 'Анна', 'department': 'Finance', 'salary ': 48000, 'experience': 4, 'performance': 9.0},
 {'name': 'Сергій', 'department': 'IT', 'salary': 38000, 'experience': 2, 'performance': 7.5},
 {'name': 'Ольга', 'department': 'Marketing', 'salary': 42000, 'experience': 6, 'performance': 8.7},
]

it_high_salary = list(filter(lambda e: e['department'] == 'IT' and e['salary'] > 40000, employees))

top_performers = list(map(lambda e: e['name'],
                    filter(lambda e: e['performance'] > 8 .5,  employees)))
bonuses = list(map(lambda e: e['salary'] * (0.1 if e['performance'] > 8.0 else 0.05),  employees))

sorted_employees = sorted(employees, key=lambda e: (-e['experience'], -e['performance']))
from itertools import groupby
employees_sorted = sorted(employees, key=lambda e: e['department'])
avg_salary_by_dept = { 
    dept: sum(emp['salary'] for emp in group) / len(list(group))
    for dept, group in groupby(employees_sorted, key=lambda e: e['department'])
}

dept_employees = {}
for emp in employees:
    dept_employees.setdefault(emp['department'], []).append(emp[' name'])
#3.2
basic_operations = {
    'add': lambda a, b: a + b,
    'subtract': lambda a, b: a - b,
    'multiply': lambda a, b: a * b,
    'divide': lambda a, b: a / b if b != 0 else None,
    'power': lambda a, b: a ** b,
    'mod': lambda a, b: a % b
}

advanced_functions = {
    'factorial': lambda n: reduce(lambda x, y: x * y, range(1, n+1), 1),
    'fibonacci': lambda n: (lambda f: f(f, n))(lambda self, x: x if x <= 1 else self(self, x-1) + self(self, x-2)),
    'is_prime': lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)),
    'gcd': lambda a, b: math.gcd(a, b)
}

list_operations = {
    'sum_squares': lambda lst: sum(map(lambda x: x**2, lst)),
    'product': lambda lst: reduce(lambda x, y: x * y, lst, 1),
    'average': lambda lst: sum(lst) / len(lst),
    'max_min_diff': lambda lst: max(lst) - min(lst)
}

def calculate(operation_type, operation_name, *args):
    operations = {
        'basic': basic_operations,
        'advanced': advanced_functions,
        'list': list_operations
    }
    return operations[operation_type][operation_name](*args)

def create_custom_function(formula_lambda):
    return formula_lambda

