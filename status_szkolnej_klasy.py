import random


class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = []

    def __repr__(self):
        return f"{self.get_full_name()} ma nastepujące oceny: {self.grades}, średnia ocen: {self.count_average()} "

    def get_full_name(self):
        return self.name + " " + self.surname

    def add_grade(self, teacher_choice):
        if len(self.grades) < 3:
            self.grades.append(teacher_choice)

    def count_average(self):
        if len(self.grades) == 0:
            return 3.0
        for item in self.grades:
            if len(self.grades) == 3 and item == 1:
                average = (sum(self.grades) - 1) / (len(self.grades) - 1)
                return average
        average = sum(self.grades) / len(self.grades)
        return average

    def add_random_grade(self):
        random_grade = random.randint(1, 5)
        self.add_grade(random_grade)


class Classroom:

    def __init__(self, number, letter, profile, year, teacher):
        self.number = number
        self.letter = letter
        self.profile = profile
        self.year = year
        self.teacher = teacher
        self.list_of_students = []

    def get_full_class_name(self):
        return self.number + self.letter

    def __repr__(self):
        return f"Do klasy {self.get_full_class_name()} o profilu {self.profile}, w roku {self.year} uczęszczają " \
               f"następujący uczniowie {self.list_of_students}, ich wychowawcą jest {self.teacher}."

    def add_student(self, teacher_choice):
        self.list_of_students.append(teacher_choice)
        self.list_of_students = sorted(self.list_of_students, key=lambda student: student.surname)

    def add_random_grade_n_times(self, count):
        for i in range(count):
            random_student = random.choice(self.list_of_students)
            random_student.add_random_grade()

    def choose_best_student(self):
        best_student = max(self.list_of_students, key=lambda student: student.count_average())
        return best_student

    def alphabetical_order(self):
        sorted_students = sorted(self.list_of_students, key=lambda student: student.surname)
        return list(map(lambda student: student.get_full_name(), sorted_students))

    def failed_students(self):
        filtered = filter(lambda student: student.count_average() < 3.0, self.list_of_students)
        return list(map(lambda failed_student: failed_student.get_full_name(), filtered))



