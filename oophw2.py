class Student:
    def __init__(self, name, surname, gender):
        self._grades_list = []
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
##############################################################################################
    def _midgrade(self):
        grades_list = []
        for grades in self.grades.values():
            for grade in grades:
                grades_list.append(grade)
            if len(grades_list) == 0:
                self.midgrade = 0
            else:
                self.midgrade = sum(grades_list) / len(grades_list)
            return self.midgrade
##############################################################################################
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self._midgrade()}\n' 
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' 
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')
##############################################################################################
    def __lt__(self, other_student):
        """Check, who is better - you or other student?"""
        if isinstance(other_student, Student) and len(self.grades) > 0 and len(other_student.grades) > 0:
            return (f'Средняя оценка студента {self.name} = {self._midgrade()}. \n'
                    f'Средняя оценка студента {other_student.name} {other_student._midgrade()}\n'
                    f'Студент {self.name} лучше.')
        else:
            return 'У кого то из студентов нет оценок.'
##############################################################################################
    def lect_rate(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses):
            if course in lecturer.courses_grades:
                lecturer.courses_grades[course] += [grade]
            else:
                lecturer.courses_grades[course] = [grade]
        else:
            return 'Ошибка!'
##############################################################################################
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
##############################################################################################
class Reviewer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
##############################################################################################
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'
##############################################################################################
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка!'
##############################################################################################
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses = []
        self.courses_grades = {}
##############################################################################################
    def _midgrade(self):
        grades_list = []
        for grades in self.courses_grades.values():
            for grade in grades:
                grades_list.append(grade)
        if len(grades_list) == 0:
            self.midgrade = 0
        else:
            self.midgrade = sum(grades_list) / len(grades_list)
        return self.midgrade
##############################################################################################
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._midgrade()}\n'
##############################################################################################
    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer) and len(self.courses_grades) > 0 and len(other_lecturer.courses_grades) > 0:
            return (f'Средняя оценка лектора {self.name} = {self._midgrade()}. \n'
                    f'Средняя оценка лектора {other_lecturer.name} {other_lecturer._midgrade()}\n'
                    f'Лектор {self.name} лучше.')
        else:
            return 'У кого то из лекторов нет оценок.'
##############################################################################################
student1 = Student('Антон', 'Мельник', 'муж')
student1.courses_in_progress = ['Языки', 'Технологии', 'Python']
student1.finished_courses = ['C++', 'Java']
##############################################################################################
student2 = Student('Борис', 'Джонсон', 'муж')
student2.courses_in_progress = ['Языки', 'Технологии', 'Python', 'C++']
student2.finished_courses = ['Java']
##############################################################################################
lecturer1 = Lecturer('Арнольд', 'Шварценеггер')
lecturer1.courses = ['C++', 'Технологии']
##############################################################################################
lecturer2 = Lecturer('Брюс', 'Вейн')
lecturer2.courses = ['Языки', 'Python', 'Java']
##############################################################################################
reviwer1 = Reviewer('Эрик', 'Картман')
reviwer1.courses_attached = ['Языки', 'Технологии',]
reviwer1.rate_hw(student2,'Языки', 9)
reviwer1.rate_hw(student2,'Языки', 8)
reviwer1.rate_hw(student2,'Технологии', 5)
reviwer1.rate_hw(student1,'Языки', 7)
reviwer1.rate_hw(student1,'Языки', 6)
reviwer1.rate_hw(student1,'Технологии', 10)
reviwer2 = Reviewer('Кенни', 'МакКормик')
reviwer2.courses_attached = ['Python', 'C++', 'Java']
##############################################################################################
student1.lect_rate(lecturer1,'Технологии', 4)
student2.lect_rate(lecturer1,'C++', 10)
student1.lect_rate(lecturer2,'Языки', 5)
student2.lect_rate(lecturer2,'Языки', 10)
##############################################################################################
print(reviwer1)
print(reviwer2)
print(lecturer1)
print(lecturer2)
print(student1)
print(student2)
print(f'{student2.__lt__(student1)}')
print(f'{lecturer2.__lt__(lecturer1)}')
print('')
##############################################################################################
students_list = [student1,student2]
lecturers_list = [lecturer2,lecturer1]
courses = ['C++', 'Языки', 'Python', 'Технологии', 'Java']
##############################################################################################
def student_midgrades(students, course):
    all_course_grades = []
    for student in students:
        for grade in student.grades.get(course):
            all_course_grades += [grade]
    mid_grade = sum(all_course_grades) / len(all_course_grades)
    print(f'Средняя оценка за курс {course}: {mid_grade}')
##############################################################################################
def lecturer_midgrades(lecturers, course):
    all_course_grades = []
    for lecturer in lecturers:
        for grade in lecturer.grades.get(course):
            all_course_grades += [grade]
    mid_grade = sum(all_course_grades) / len(all_course_grades)
    print(f'Средняя оценка за курс {course}: {mid_grade}')
##############################################################################################
student_midgrades(students_list,courses[1])
lecturer_midgrades(students_list,courses[3])
##############################################################################################