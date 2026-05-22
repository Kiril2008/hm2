# 1

import statistics

class AdvancedCalculator:

    def __init__(self, precision=2):
        self.precision = precision

    def calculate(self, operation, *args, **kwargs):

        if not self.validate_numbers(*args):
            return "Помилка: всі аргументи повинні бути числами"

        if operation == "add":
            return self.format_result(self._add_numbers(*args))

        elif operation == "multiply":
            return self.format_result(self._multiply_numbers(*args))

        elif operation == "power":
            exponent = kwargs.get("exponent", 2)
            return self.format_result(self._power_operation(args[0], exponent))

        elif operation == "statistics":
            stat_operation = kwargs.get("operation", "mean")
            return self.format_result(
                self._statistics(*args, operation=stat_operation)
            )

        else:
            return "Невідома операція"

    def _add_numbers(self, *numbers):
        return sum(numbers)

    def _multiply_numbers(self, *numbers):
        result = 1
        for num in numbers:
            result *= num
        return result

    def _power_operation(self, base, exponent=2):
        return base ** exponent

    def _statistics(self, *numbers, operation="mean"):

        if operation == "mean":
            return statistics.mean(numbers)

        elif operation == "median":
            return statistics.median(numbers)

        elif operation == "max":
            return max(numbers)

        elif operation == "min":
            return min(numbers)

    @staticmethod
    def validate_numbers(*args):
        return all(isinstance(x, (int, float)) for x in args)

    def format_result(self, result):
        return round(result, self.precision)
calc = AdvancedCalculator(precision=3)

print(calc.calculate("add", 1, 2, 3, 4, 5))
print(calc.calculate("multiply", 2, 3, 4))
print(calc.calculate("power", 2, exponent=3))
print(calc.calculate("statistics", 1, 2, 3, 4, 5, operation="median"))

# 2

class Book:
    

    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"{self.title} - {self.author} ({self.year}) [{self.genre}]"


class BookIterator:
    

    def __init__(self, books, filter_by=None, filter_value=None):

        if filter_by and filter_value:
            self.books = [
                book for book in books
                if getattr(book, filter_by) == filter_value
            ]
        else:
            self.books = books

        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= len(self.books):
            raise StopIteration

        book = self.books[self.index]
        self.index += 1
        return book


class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

    def __iter__(self):
        return BookIterator(self.books)

    def by_author(self, author):
        return BookIterator(self.books, "author", author)

    def by_year(self, year):
        return BookIterator(self.books, "year", year)

    def by_genre(self, genre):
        return BookIterator(self.books, "genre", genre)



collection = BookCollection()

collection.add_book(Book("1984", "Orwell", 1949, "Dystopia"))
collection.add_book(Book("Brave New World", "Huxley", 1932, "Dystopia"))
collection.add_book(Book("Dune", "Herbert", 1965, "Sci-Fi"))

print("Всі книги:")
for book in collection:
    print(f"  {book}")

print("\nКниги жанру Dystopia:")
for book in collection.by_genre("Dystopia"):
    print(f"  {book}")


    # 3

from datetime import datetime
from enum import Enum
import statistics


class Subject(Enum):
    MATH = "алгебра"
    PHYSICS = "Фізика"
    CHEMISTRY = "Укрмова"
    BIOLOGY = "біологія"
    HISTORY = "Історія"


class Grade:

    def __init__(self, subject, value, date=None):
        self.subject = subject
        self.value = value
        self.date = date if date else datetime.now()

    def __str__(self):
        return f"{self.subject.value}: {self.value}"

    def __repr__(self):
        return self.__str__()


class Student:

    _student_count = 0

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

        Student._student_count += 1

    @classmethod
    def get_student_count(cls):
        return cls._student_count

    @classmethod
    def from_string(cls, student_string):
        name, student_id = student_string.split(",")
        return cls(name, student_id)

    @staticmethod
    def validate_grade(grade):
        return 1 <= grade <= 12

    def add_grade(self, subject, value):

        if self.validate_grade(value):
            self.grades.append(Grade(subject, value))
        else:
            print("Неправильна оцінка")

    def get_average(self, subject=None):

        if subject:
            values = [
                grade.value
                for grade in self.grades
                if grade.subject == subject
            ]
        else:
            values = [grade.value for grade in self.grades]

        if not values:
            return 0

        return round(statistics.mean(values), 2)

    def __str__(self):
        return f"{self.name} ({self.student_id})"

    def __len__(self):
        return len(self.grades)

    def __getitem__(self, subject):
        return [
            grade for grade in self.grades
            if grade.subject == subject
        ]

    def __iter__(self):
        return iter(self.grades)


class StudentRegistry:

    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def __len__(self):
        return len(self.students)

    def __contains__(self, student_id):
        return student_id in self.students

    def __getitem__(self, student_id):
        return self.students.get(student_id)

    def __iter__(self):
        return iter(self.students.values())

    def top_students(self, n=5):

        sorted_students = sorted(
            self.students.values(),
            key=lambda s: s.get_average(),
            reverse=True
        )

        for student in sorted_students[:n]:
            yield student

    def students_by_average(self, min_average):

        for student in self.students.values():
            if student.get_average() >= min_average:
                yield student

    def get_statistics(self):

        averages = [
            student.get_average()
            for student in self.students.values()
        ]

        if not averages:
            return {}

        return {
            "students_count": len(self.students),
            "overall_average": round(statistics.mean(averages), 2),
            "max_average": max(averages),
            "min_average": min(averages)
        }
registry = StudentRegistry()

student1 = Student("Іван Петренко", "S001")
student2 = Student.from_string("Марія Коваленко,S002")

student1.add_grade(Subject.MATH, 10)
student1.add_grade(Subject.PHYSICS, 9)

student2.add_grade(Subject.MATH, 12)
student2.add_grade(Subject.CHEMISTRY, 11)

registry.add_student(student1)
registry.add_student(student2)

print(f"Кількість студентів: {len(registry)}")
print(f"Середній бал Івана з математики: {student1.get_average(Subject.MATH)}")

print("\nТоп студенти:")
for student in registry.top_students(2):
    print(f"  {student}")

print(f"\nСтатистика: {registry.get_statistics()}")