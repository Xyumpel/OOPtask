class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)  

    def lector_grade(self, lec,course, grade):
        if isinstance(lec, Lecturer) and course in self.courses_in_progress and 1 <= grade and grade <=10:
            if course in lec.courses_attached and course not in lec.lector_grades:
                lec.lector_grades[course] = [grade]
            elif course in lec.courses_attached and course in lec.lector_grades:
                lec.lector_grades[course] += [grade]
            else:
                print('Не преподает на данном курсе')    
        else:
            print('Ошибка')
    

    def avg_hw(self):
        sum = 0
        i = 0
        for key, value in self.grades.items():
            for gr in value:
                sum += gr
                i += 1
        return sum/i
    

    def __str__(self):
        name = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg_hw()} \nКурсы, в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'
        return name


    def __lt__(self,other):
        if not isinstance(other, Student):
            print('Не является студентом')
            return
        return self.avg_hw() < other.avg_hw()
                


  
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lector_grades = {}

    
    def avg_lec(self):
        sum = 0
        i = 0
        for key, value in self.lector_grades.items():
            for gr in value:
                sum += gr
                i += 1
        return sum/i


    def __str__(self):
        name = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_lec()}'
        return name


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является лектором')
            return
        return self.avg_lec() < other.avg_lec()

    


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
        name = f'Имя: {self.name} \nФамилия: {self.surname}'
        return name


def avg_hw_all(students, course):
    summa = 0
    i = 0
    for student in students:
        if course in student.grades:
            for gr in student.grades[course]:
                summa += gr
                i +=1
        else:
            return f'Не обучается на данном курсе'
    return f'Средняя оценка за домашнее задание по {course}: {summa/i}'
        
            

def avg_lec_all(lectors, course):
    summa = 0
    i = 0
    for lector in lectors:
        if course in lector.courses_attached:
            for gr in lector.lector_grades[course]:
                summa += gr
                i +=1
        else:
            return f'Не обучается на данном курсе'
    return f'Средняя оценка за лекции по {course}: {summa/i}'



        

        
student1 = Student('Izuku', 'Midoria', 'man')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Uroraka', 'Chan', 'Woman')
student2.courses_in_progress += ['Git', 'Python']
student2.finished_courses += ['Web-дизайн']

 
reviewer1 = Reviewer('All', 'Might')
reviewer1.courses_attached += ['Python', 'Git']
reviewer2 = Reviewer('Aizava', 'Shota')
reviewer2.courses_attached += ['Git', 'Python']

lector1 = Lecturer('Katsuki', 'Bakugo')
lector1.courses_attached += ['Python', 'Git']
lector2 = Lecturer('Shoto', 'Todoroki')
lector2.courses_attached += ['Git', 'Python']

student1.lector_grade( lector1, 'Git', 9)
student2.lector_grade( lector1, 'Git', 7)
student1.lector_grade( lector1, 'Python', 6)
student2.lector_grade( lector1, 'Git', 3)
student1.lector_grade( lector1, 'Python', 5)
student2.lector_grade( lector2, 'Git', 2)
student1.lector_grade( lector2, 'Python', 5)
student2.lector_grade( lector2, 'Git', 9)
student2.lector_grade( lector2, 'Git', 2)
student1.lector_grade( lector2, 'Python', 5)
student2.lector_grade( lector2, 'Git', 9)


reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 6)
reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 5)
reviewer2.rate_hw(student1, 'Git', 9)
reviewer2.rate_hw(student1, 'Git', 7)
reviewer2.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student2, 'Git', 10)
reviewer2.rate_hw(student2, 'Git', 7)
reviewer2.rate_hw(student2, 'Git', 6)


print(student1)
print(lector1)
print(reviewer1)
print(student1 > student2)
print(lector1 < lector2)
print(avg_hw_all([student1, student2], 'Git'))
print(avg_lec_all([lector1, lector2], 'Python'))

