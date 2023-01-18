
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
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}\n'
        return result
    
    def __lt__(self, other):
        if not isinstance(self, Student):
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

    def __lt__(self, other):
        if not isinstance(self, Lecturer):
            print('Error')
            return
        else:
            return self.__average_grade() < other.__average_grade()

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_grade()}\n'
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
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return result
 


first_student = Student('Ruoy', 'Eman', 'Male')
second_student = Student('Maxim', 'Pavlenko', 'Male')

first_student.courses_in_progress += ['Python','Physics','Geometry']
#first_student.courses_in_progress += ['Physics']
#first_student.courses_in_progress += ['Geometry']
second_student.courses_in_progress += ['Python','Physics','Geometry']
#second_student.courses_in_progress += ['Physics']
#second_student.courses_in_progress += ['Geometry']

 
first_reviewer = Reviewer('Some', 'Buddy')
second_reviewer = Reviewer('Dmitry', 'Nagiev')

first_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Phisics','Geometry']
#second_reviewer.courses_attached += ['Geometry']

first_lecturer = Lecturer('Albert', 'Einstein')
second_lecturer = Lecturer('Polina','Gagarina')

first_lecturer.courses_attached += ['Physics']
second_lecturer.courses_attached += ['Geometry','Python']
#second_lecturer.courses_attached += ['Geometry'] 
first_reviewer.rate_hw(first_student, 'Python', 5)
first_reviewer.rate_hw(first_student, 'Geometry', 10)
first_reviewer.rate_hw(first_student, 'Physics', 5)
second_reviewer.rate_hw(second_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Geometry', 10)
second_reviewer.rate_hw(first_student, 'Physics', 10)




first_student.rate_lecturer(first_lecturer, 'Physics', 10)
second_student.rate_lecturer(first_lecturer, 'Physics', 10)
first_student.rate_lecturer(second_lecturer, 'Phyton', 9)
second_student.rate_lecturer(second_lecturer, 'Phyton', 5)
first_student.rate_lecturer(second_lecturer, 'Geometry', 5)
second_student.rate_lecturer(second_lecturer, 'Geometry', 10)
 

print(first_student, second_student)
print(first_lecturer, second_lecturer)
print(first_reviewer,second_reviewer)
