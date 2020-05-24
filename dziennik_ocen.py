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


def add_random_grade_n_times(students, count):
    for i in range(count):
        random_student = random.choice(students)
        random_student.add_random_grade()


def choose_best_student(students):
    best_student = max(students, key=lambda student:student.count_average())
    return best_student


def alphabetical_order(students):
    sorted_students = sorted(students, key=lambda student: student.surname)
    return list(map(lambda student: student.get_full_name(), sorted_students))


def failed_students(students_list):
    filtered = filter(lambda student: student.count_average() < 3.0, students_list)
    return list(map(lambda failed_student: failed_student.get_full_name(), filtered))


student1 = Student("Marek", "Markowski")
student2 = Student("Anna", "Kwiatkowska")
student3 = Student("Władysław", "Kowalski")
lst = [student1, student2, student3]
student1.add_grade(1)
student1.add_grade(5)
student1.add_grade(3)
student1.add_grade(5)
student3.add_grade(1)
student2.add_random_grade()
student2.add_random_grade()
add_random_grade_n_times(lst, 3)


print(student1)
print(student2)
print(student3)

print("Gratulacje " + choose_best_student(lst).get_full_name())
print(alphabetical_order(lst))
print(failed_students(lst))