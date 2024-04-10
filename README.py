class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def hw_grades(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_attached and course in lector.courses_in_progress:
            if course in lector.grades:
                lector.grade[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return  f'{self.name}, {self.surname}, {", ".join(self.courses_in_progress)}, {", ".join(self.finished_courses)}, {self._get_average_grade()}'

    def _get_average_grade(self):
        return sum(self.grades.values()) / len(self.grades)
    
    def __lt__(self, other):
        return self.name < other.name


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def hw_grades(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_attached and course in lector.courses_in_progress:
            if course in lector.grades:
                lector.grade[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'{self.name}, {self.surname}, {", ".join(self.courses_in_progress)}, {", ".join(self.finished_courses)}, {self._get_average_grade()}'

    def _get_average_grade(self):
        return sum(self.grades.values()) / len(self.grades)
    
    def __lt__(self, other):
        return self.name < other.name


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __str__(self):
        return f'{self.name}, {self.surname},{self._homework_average_grade()}'
                              
    def _homework_average_grade(self):
        return sum(self.grades.values()) / len(self.grades)
    
    def __lt__(self, other):
        return self.name < other.name


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __str__(self):
        return f'{self.name}, {self.surname}, {self._homework_average_grade()}'
                              
    def _homework_average_grade(self):
        return sum(self.grades.values()) / len(self.grades)
    
    def __lt__(self, other):
        return self.name < other.name


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'{self.name} {self.surname}'
        

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'{self.name} {self.surname}'


def average_grades_for_students(persons, course):
    if not isinstance(persons, list):
        return 'Ошибка'
    all_average_grades = []
    for person in persons:
        all_average_grades.extend(person.all_average_grades.get(course, []))
    if not all_average_grades:
        return 'Оценок по курсу нет'
    return sum(all_average_grades) / len(all_average_grades)

def average_grades_for_lecturers(persons, course):
    if not isinstance(persons, list):
        return 'Ошибка'
    all_average_grades = []
    for person in persons:
        all_average_grades.extend(person.all_average_grades.get(course, []))
    if not all_average_grades:
        return 'Оценок по курсу нет'
    return sum(all_average_grades) / len(all_average_grades)
    
student_1 = Student('Вадим', 'Левченко', "М")
student_2 = Student('Анна', "Левченко", "Ж")
student_3 = Student('Яман', 'Култум', 'М')
student_1.courses_in_progress += ['Python', 'Java']
student_2.courses_in_progress += ['Python'] 
student_3.courses_in_progress += ['Python']
student_1.__str__()
student_1.hw_grades(lecturer_1, 'Python', 5)
student_2.hw_grades(lecturer_1, 'Python', 4)
student_3.hw_grades(lecturer_1, 'Python', 3)
student_1.hw_grades(lecturer_1, 'Python', 4)

lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_1.__str__()
lecturer_1._homework_average_grade()

mentor_1 = Mentor('Иван', 'Иванов')

reviewer_1 = Reviewer('Петр', 'Петров')
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Python', 4)
reviewer_1.rate_hw(student_3, 'Python', 3)
reviewer_1.rate_hw(student_1, 'Python', 4)
student_1._get_average_grade()
student_1.__lt__(student_2)


