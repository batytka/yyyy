class Student:
    def __init__(self, name, surname, grade, institution=""):
        self.name = name
        self.surname = surname
        self.grade = grade
        self.institution = institution

    def is_institution_valid(self):
        """Перевіряє, чи атрибут 'institution' не є пустим."""
        return bool(self.institution)

    def get_grade_description(self):
        """Виводить фразу залежно від балу студента."""
        if self.grade == 12:
            return "Відмінно"
        elif self.grade >= 10:
            return "Добре"
        elif self.grade >= 7:
            return "Задовільно"
        elif self.grade >= 4:
            return "Погано"
        elif self.grade >= 1:
            return "Дуже погано"
        else:
            return "Невідомий бал"


# Приклад використання:
student1 = Student("Іван", "Петров", 10, "Київський університет")
student2 = Student("Марія", "Іванова", 6)
student3 = Student("Петро", "Сидоров", 12, "Львівська політехніка")
student4 = Student("Олена", "Коваль", 3)
student5 = Student("Андрій", "Шевченко", 0)


print(f"{student1.name} {student1.surname}: Навчальний заклад - {student1.institution}, Оцінка - {student1.get_grade_description()}")
print(f"Валідність навчального закладу для {student1.name}: {student1.is_institution_valid()}")

print(f"{student2.name} {student2.surname}: Навчальний заклад - {student2.institution}, Оцінка - {student2.get_grade_description()}")
print(f"Валідність навчального закладу для {student2.name}: {student2.is_institution_valid()}")


print(f"{student3.name} {student3.surname}: Навчальний заклад - {student3.institution}, Оцінка - {student3.get_grade_description()}")
print(f"Валідність навчального закладу для {student3.name}: {student3.is_institution_valid()}")

print(f"{student4.name} {student4.surname}: Навчальний заклад - {student4.institution}, Оцінка - {student4.get_grade_description()}")
print(f"Валідність навчального закладу для {student4.name}: {student4.is_institution_valid()}")

print(f"{student5.name} {student5.surname}: Навчальний заклад - {student5.institution}, Оцінка - {student5.get_grade_description()}")
print(f"Валідність навчального закладу для {student5.name}: {student5.is_institution_valid()}")