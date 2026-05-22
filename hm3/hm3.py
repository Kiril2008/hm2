import time

#1

class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        self.price = new_price

    def add_stock(self, amount):
        self.quantity += amount

    def remove_stock(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount

    def is_available(self):
        return self.quantity > 0

    def get_total_value(self):
        return self.price * self.quantity

    def get_info(self):
        return f"{self.name} ({self.category}) - {self.price} грн, кількість: {self.quantity}"


#2

class RestaurantBill:
    def __init__(self, table_number):
        self.table_number = table_number
        self.__items = {}

    def add_item(self, dish_name, price):
        self.__items[dish_name] = price

    def remove_item(self, dish_name):
        self.__items.pop(dish_name, None)

    @property
    def total(self):
        return sum(self.__items.values())

    def apply_discount(self, percentage):
        for item in self.__items:
            self.__items[item] *= (1 - percentage / 100)

    def get_bill_details(self):
        result = f"Стіл №{self.table_number}\n"
        for name, price in self.__items.items():
            result += f"{name}: {price} грн\n"
        return result


#3

class ElectronicDevice:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def power_on(self):
        return "Увімкнено"

    def power_off(self):
        return "Вимкнено"

    def get_info(self):
        return f"{self.brand} {self.model} - {self.price} грн"


class Smartphone(ElectronicDevice):
    def __init__(self, brand, model, price, screen_size, camera_mp):
        super().__init__(brand, model, price)
        self.screen_size = screen_size
        self.camera_mp = camera_mp

    def make_call(self, number):
        return f"Дзвінок на {number}"

    def take_photo(self):
        return "Фото зроблено"


class Laptop(ElectronicDevice):
    def __init__(self, brand, model, price, ram_gb, storage_gb):
        super().__init__(brand, model, price)
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb

    def run_program(self, program_name):
        return f"Запуск {program_name}"

    def upgrade_ram(self, additional_gb):
        self.ram_gb += additional_gb
        return f"RAM: {self.ram_gb} GB"


class Tablet(ElectronicDevice):
    def __init__(self, brand, model, price, screen_size, has_stylus):
        super().__init__(brand, model, price)
        self.screen_size = screen_size
        self.has_stylus = has_stylus

    def draw(self):
        return "Малювання"

    def rotate_screen(self):
        return "Екран повернуто"


#4

class DeliveryService:
    def __init__(self, package_weight, distance):
        self.package_weight = package_weight
        self.distance = distance

    def calculate_cost(self):
        raise NotImplementedError

    def estimate_delivery_time(self):
        raise NotImplementedError

    def get_info(self):
        return f"{self.calculate_cost()} грн, {self.estimate_delivery_time()}"


class CourierDelivery(DeliveryService):
    def __init__(self, package_weight, distance, is_fragile):
        super().__init__(package_weight, distance)
        self.is_fragile = is_fragile

    def calculate_cost(self):
        cost = 50 + self.distance * 10 + self.package_weight * 5
        if self.is_fragile:
            cost += 30
        return cost

    def estimate_delivery_time(self):
        return "1-3 години"


class PostDelivery(DeliveryService):
    def __init__(self, package_weight, distance, delivery_type):
        super().__init__(package_weight, distance)
        self.delivery_type = delivery_type

    def calculate_cost(self):
        cost = 30 + self.package_weight * 3
        if self.delivery_type == "рекомендована":
            cost += 20
        return cost

    def estimate_delivery_time(self):
        return "3-7 днів"


class ExpressDelivery(DeliveryService):
    def __init__(self, package_weight, distance, delivery_time):
        super().__init__(package_weight, distance)
        self.delivery_time = delivery_time

    def calculate_cost(self):
        return 100 + self.distance * 15 + self.package_weight * 8

    def estimate_delivery_time(self):
        return "сьогодні"


def compare_delivery_options(deliveries):
    for d in deliveries:
        print(d.get_info())


#5

class Course:
    def __init__(self, title, instructor, duration_hours, price):
        self.title = title
        self.instructor = instructor
        self.duration_hours = duration_hours
        self.price = price

    def get_info(self):
        return f"{self.title} - {self.price} грн"

    def start_course(self):
        return "Старт курсу"

    def calculate_price_per_hour(self):
        return self.price / self.duration_hours


class VideoCourse(Course):
    def __init__(self, title, instructor, duration_hours, price, video_quality, total_videos):
        super().__init__(title, instructor, duration_hours, price)
        self.video_quality = video_quality
        self.total_videos = total_videos

    def start_course(self):
        return "Відеокурс розпочато"

    def download_videos(self):
        return "Завантаження відео"


class TextCourse(Course):
    def __init__(self, title, instructor, duration_hours, price, total_pages, has_exercises):
        super().__init__(title, instructor, duration_hours, price)
        self.total_pages = total_pages
        self.has_exercises = has_exercises

    def start_course(self):
        return "Читання курсу"

    def print_materials(self):
        return "Друк матеріалів"


class InteractiveCourse(Course):
    def __init__(self, title, instructor, duration_hours, price, has_live_sessions, max_students):
        super().__init__(title, instructor, duration_hours, price)
        self.has_live_sessions = has_live_sessions
        self.max_students = max_students

    def start_course(self):
        return "Інтерактивний курс"

    def join_live_session(self):
        return "Підключення до сесії"


class CourseManager:
    def __init__(self, platform_name):
        self.platform_name = platform_name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course_title):
        self.courses = [c for c in self.courses if c.title != course_title]

    def find_course(self, course_title):
        for c in self.courses:
            if c.title == course_title:
                return c

    def list_all_courses(self):
        for c in self.courses:
            print(c.get_info())

    def get_total_revenue(self):
        return sum(c.price for c in self.courses)

    def get_average_price(self):
        return sum(c.price for c in self.courses) / len(self.courses)