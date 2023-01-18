
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
            return round(sum(av_grades)/len(self.grades),1)
        else:
            return 0

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
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
            return round(sum(av_grades)/len(self.grades),1)
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(self, Lecturer):
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
 




first_student = Student('Ruoy', 'Eman', 'Male')
second_student = Student('Maxim', 'Pavlenko', 'Male')

first_student.courses_in_progress += ['Python','Physics','Geometry']
second_student.courses_in_progress += ['Python','Physics','Geometry']

 
first_reviewer = Reviewer('Some', 'Buddy')
second_reviewer = Reviewer('Dmitry', 'Nagiev')

first_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Physics','Geometry']


first_lecturer = Lecturer('Albert', 'Einstein')
second_lecturer = Lecturer('Polina','Gagarina')

first_lecturer.courses_attached += ['Physics']
second_lecturer.courses_attached += ['Geometry','Python']

first_reviewer.rate_hw(first_student, 'Python', 5)
first_reviewer.rate_hw(second_student, 'Python', 10)

second_reviewer.rate_hw(first_student, 'Physics', 10)
second_reviewer.rate_hw(first_student, 'Geometry', 5)

second_reviewer.rate_hw(second_student, 'Physics', 10)
second_reviewer.rate_hw(second_student, 'Geometry', 10)

first_student.rate_lecturer(first_lecturer, 'Physics', 5)
second_student.rate_lecturer(first_lecturer, 'Physics', 7)
first_student.rate_lecturer(second_lecturer, 'Python', 5)
second_student.rate_lecturer(second_lecturer, 'Python', 8)
first_student.rate_lecturer(second_lecturer, 'Geometry', 5)
second_student.rate_lecturer(second_lecturer, 'Geometry', 10)


print(f'{first_student}\n\n{second_student}')
print('\n')
print(f'{first_lecturer}\n\n{second_lecturer}')
print('\n')
print(f'{first_reviewer}\n\n{second_reviewer}')

print(second_student>first_student)
print(second_lecturer<first_lecturer)

students = (first_student, second_student)
course = 'Python'

def average_grade_students(course, *args):
    sum_marks = 0
    number_marks = 0
    for j in range(len(args)):
        if course in args[j].grades:
            number_marks += len(args[j].grades[course])
            sum_marks += sum(args[j].grades[course])
    
    if number_marks != 0:
        av_score=round(sum_marks/number_marks,1)
        print(f'Средняя оценка студентов по курсу {course}: {av_score}')
    else:
        print(f'На курсе {course} студенты еще не получили оценок')
                  

average_grade_students(course, *students)

lecturers = (first_lecturer, second_lecturer)
course = 'Python'

def average_grade_lecturers(course, *args):
    sum_marks = 0
    number_marks = 0
    for j in range(len(args)):
        if course in args[j].grades:
            number_marks += len(args[j].grades[course])
            sum_marks += sum(args[j].grades[course])
    
    if number_marks != 0:
        av_score=round(sum_marks/number_marks,1)
        print(f'Средняя оценка лекторов по курсу {course}: {av_score}')
    else:
        print(f'На курсе {course} лекторы еще не получили оценок')
                  

average_grade_lecturers(course, *lecturers)