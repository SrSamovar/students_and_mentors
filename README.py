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
        
    def __str__(self) -> str:
        return f'{self.name} 
                 {self.surname} 
                 {", ".join(self.courses_in_progress)} 
                 {", ".join(self.finished_courses)}
                 {self._get_average_grade()}'

    def _get_average_grade(self):
        return sum(self.grades.values()) / len(self.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __lt__(self, other):
        return self.name < other.name
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def __str__(self):
        return f'{self.name}
                 {self.surname}
                 {self._homework_average_grade()}'
                              
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
        
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)