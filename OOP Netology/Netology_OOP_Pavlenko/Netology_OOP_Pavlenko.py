
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'

    def __average_grade(self):
        if len(self.grades) != 0:
            av_grades = [sum(i)/len(i) for i in self.grades.values()]
            return sum(av_grades)/len(self.grades)
        else:
            return 0

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return result
    
    def __lt__(self, other):
        if not isinstance(self, Student) and course not in self.courses_in_progress:
            print('Error')
            return
        else:
            return self.__average_grade() < other.__average_grade()

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_grade(self):
        if len(self.grades) != 0:
            av_grades = [sum(i)/len(i) for i in self.grades.values()]
            return sum(av_grades)/len(self.grades)
        else:
            return 0

    def __lt__(self, course, other):
        if not isinstance(self, Lecturer) and course not in self.courses_attached:
            print('Error')
            return
        else:
            return self.__average_grade() < other.__average_grade()

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_grade()}'
        return result


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'
    
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result
 


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Physics']

standart_student = Student('Maxim', 'Pavlenko', 'Male')
standart_student.courses_in_progress += ['Physics']
standart_student.courses_in_progress += ['Geometry']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
best_reviewer = Reviewer('Dmitry', 'Nagiev')
best_reviewer.courses_attached += ['Python']
best_reviewer.courses_attached += ['Geometry']

best_lecturer = Lecturer('Albert', 'Einstein')
best_lecturer.courses_attached += ['Physics']
cool_lecturer = Lecturer('Polina','Gagarina')
cool_lecturer.courses_attached += ['Geometry']
 
cool_reviewer.rate_hw(best_student, 'Python', 1)
cool_reviewer.rate_hw(best_student, 'Geometry', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lecturer(best_lecturer, 'Physics', 9)
 

print(best_student)
print(standart_student)
print(best_lecturer)
print(cool_lecturer)
print(cool_reviewer)
print(best_reviewer)