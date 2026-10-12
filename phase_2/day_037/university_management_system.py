# Day 37 12/10/26

import re

PATTERN_STRING = r"[A-Za-z\s]+"

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades, self.courses = [], []
    
    def display(self):
        if len(self.courses) == 0:
            print(f"\nID: {self.id}\nName: {self.name}\nGrades: {self.grades}\nCourses: {self.courses}")
        else:
            print(f"\nID: {self.id}\nName: {self.name}\nGrades: {self.grades}\nCourses: ")
            print("-" * 40)
            for c in self.courses:
                print(f"ID: {c.id}\nName: {c.name}\nInstructor: {c.instructor}")
                print("-" * 40)
        
    def add_grade(self, grade):
        self.grades.append(grade)

class Course:
    def __init__(self, id, name, instructor):
        self.id = id
        self.name = name
        self.instructor = instructor
        self.students = []
    
    def display(self):
        if len(self.students) == 0:
            print(f"\nID: {self.id}\nName: {self.name}\nInstructor: {self.instructor}\nStudents: {self.students}")
        else:
            print(f"\nID: {self.id}\nName: {self.name}\nInstructor: {self.instructor}\nStudents: ")
            print("-" * 40)
            for s in self.students:
                print(f"ID: {s.id}\nName: {s.name}\nGrades: {s.grades}")
                print("-" * 40)
        
    def add_student(self, student):
        self.students.append(student)
    
    def remove_student(self, student):
        self.students.remove(student)
    
    def get_student_count(self):
        return len(self.students)

class University:
    def __init__(self):
        self.students, self.courses = [], []
    
    def add_student(self):
        id, nm = 0, ""
        
        while True:
            try:
                id = int(input("\nID: "))
                if id <= 0:
                    print("\nID cannot be negative or 0")
                    continue
                if len(self.students) == 0:
                    break
                flag = True
                
                for s in self.students:
                    if id == s.id:
                        print(f"\nStudent with ID {id} already exists!")
                        flag = False
                
                if flag:
                    break
            except ValueError:
                continue
        
        while not re.fullmatch(PATTERN_STRING, nm):
            nm = input("Name: ")
        
        self.students.append(Student(id, nm))
    
    def add_course(self):
        id, nm, ins = 0, "", ""
        
        while True:
            try:
                id = int(input("\nID: "))
                if id <= 0:
                    print("\nID cannot be negative or 0.")
                    continue
                if len(self.courses) == 0:
                    break
                flag = True
                
                for c in self.courses:
                    if id == c.id:
                        print(f"\nCourse with ID {id} already exists!")
                        flag = False
                
                if flag:
                    break
            except ValueError:
                continue
            
        while not re.fullmatch(PATTERN_STRING, nm):
            nm = input("Name: ")
            
        while not re.fullmatch(PATTERN_STRING, ins):
            ins = input("Instructor: ")
            
        self.courses.append(Course(id, nm, ins))
    
    def show_students(self):
        if len(self.students) == 0:
            return print("\nNo students found!")
        
        for s in self.students:
            s.display()
    
    def show_courses(self):
        if len(self.courses) == 0:
            return print("\nNo courses found!")
        
        for c in self.courses:
            c.display()
    
    def find_student(self):
        if len(self.students) == 0:
            return print("\nNo students found!")
        id, flag = 0, False
        
        while True:
            try:
                id = abs(int(input("\nID: ")))
                if id != 0:
                    break
                print("\nID cannot be 0.")
            except ValueError:
                continue
        
        for s in self.students:
            if id == s.id:
                s.display()
                flag = True
        
        if not flag:
            print(f"\nStudent with ID {id} not found!")
    
    def find_course(self):
        if len(self.courses) == 0:
            return print("\nNo courses found.")
        id, flag = 0, False
        
        while True:
            try:
                id = abs(int(input("\nID: ")))
                if id != 0:
                    break
                print("\nID cannot be 0.")
            except ValueError:
                continue
        
        for c in self.courses:
            if id == c.id:
                c.display()
                flag = True
        
        if not flag:
            print(f"\nCourse with ID {id} not found.")
    
    def enroll_student(self):
        if len(self.students) == 0 or len(self.courses) == 0:
            return print("\nNo students and/or courses found!")
        s_id, pos_s, c_id, pos_c = 0, 0, 0, 0
        
        while True:
            try:
                s_id = int(input("\nStudent ID: "))
                if s_id > 0:
                    flag = False
                    
                    for i, s in enumerate(self.students):
                        if s_id == s.id:
                            pos_s, flag = i, True
                    
                    if flag:
                        break
                    print(f"\nStudent with ID {s_id} not found!")
                else:
                    print("\nStudent ID cannot be negative 0.")
            except ValueError:
                continue
        
        while True:
            try:
                c_id = int(input("Course ID: "))
                if c_id > 0:
                    flag = False
                    
                    for i, c in enumerate(self.courses):
                        if c_id == c.id:
                            pos_c, flag = i, True
                    
                    if flag:
                        break
                    print(f"\nCourse with ID {c_id} not found!")
                else:
                    print("\nCourse ID cannot be negative or 0.")
            except ValueError:
                continue
        
        s, c = self.students[pos_s], self.courses[pos_c]
        already_enrolled_student = any(student.id == s_id for student in c.students)
        already_enrolled_course = any(course.id == c_id for course in s.courses)
        if already_enrolled_course and already_enrolled_student:
            return print(f"\nStudent with ID {s_id} already enrolled in course with ID {c_id}.")
        c.add_student(s)
        s.courses.append(c)
        print("\nThe enrollement was successful.")
    
    def unenroll_student(self):
        if len(self.students) == 0 or len(self.courses) == 0:
            return print("\nNo students and/or courses found!")
        
        s_id, pos_s, c_id, pos_c = 0, 0, 0, 0
        
        while True:
            try:
                s_id = int(input("\nStudent ID: "))
                if s_id > 0:
                    flag = False
                    
                    for i, s in enumerate(self.students):
                        if s_id == s.id:
                            pos_s, flag = i, True
                    
                    if flag:
                        break
                    print(f"\nStudent ID {s_id} not found!")
                else:
                    print("\nStudent ID cannot be negative or 0.")
            except ValueError:
                continue
        
        while True:
            try:
                c_id = int(input("Course ID: "))
                if c_id > 0:
                    flag = False
                    
                    for i, c in enumerate(self.courses):
                        if c_id == c.id:
                            pos_c, flag = i, True
                    
                    if flag:
                        break
                    print(f"\nCourse ID {c_id} not found!")
                else:
                    print("\nCourse ID cannot be negative or 0.")
            except ValueError:
                continue
        
        s, c = self.students[pos_s], self.courses[pos_c]
        
        if (c in s.courses) and (s in c.students):
            c = self.courses[pos_c]
            c.remove_student(s)
            s.courses.remove(c)
            print("\nUnenrollment was successful!")
        else:
            return print("\nCannot unenroll a student that hasn't been enrolled in the first place")
        
    def add_grade(self):
        if len(self.students) == 0:
            return print("\nNo students found!")
        s_id, pos_s, gr = 0, 0, 0.0
        
        while True:
            try:
                s_id = int(input("\nStudent ID: "))
                if s_id > 0:
                    flag = False
                    
                    for i, s in enumerate(self.students):
                        if s_id == s.id:
                            pos_s, flag = i, True
                    
                    if flag:
                        break
                    print(f"\nStudent with ID {s_id} not found!")
                else:
                    print("\nStudent ID cannot be negative or 0!")
            except ValueError:
                continue
        
        while True:
            try:
                gr = float(input("Grade (0-10): "))
                if (0 <= gr <= 10):
                    break
            except ValueError:
                continue
        
        s = self.students[pos_s]
        s.add_grade(gr)
    
    def show_statistics(self):
        total_s, total_c, total_enr, max_c_s, name_max_c, id_max_c = len(self.students), len(self.courses), 0, 0, "", 0
        total_gr, avg_gr, name_max_avg, max_gr_avg, total_length_gr, total_avg, id_max_avg = 0, 0, 0, 0, 0, 0, 0
        
        for c in self.courses:
            st = len(c.students)
            total_enr += st
            if st >= max_c_s:
                max_c_s = st
                name_max_c = c.name
                id_max_c = c.id
        
        for s in self.students:
            length = len(s.grades)
            if length != 0:
                total_length_gr += length
                gr_s = 0
                for i in range(length):
                    total_gr += s.grades[i]
                    gr_s += s.grades[i]
                
                avg_gr = gr_s / length
                if avg_gr >= max_gr_avg:
                    max_gr_avg = avg_gr
                    name_max_avg = s.name
                    id_max_avg = s.id
        
        if total_length_gr != 0:
            total_avg = total_gr / total_length_gr
            print(f"\nTotal students: {total_s}\nTotal courses: {total_c}\nTotal enrollments: {total_enr}\nCourse with the most students: {max_c_s} (ID: {id_max_c}, Name: {name_max_c})\nStudent with the highest avg: {max_gr_avg} (ID: {id_max_avg}, Name: {name_max_avg})\nOverall avg: {(total_avg):.2f}")
        else:
            print(f"\nTotal students: {total_s}\nTotal courses: {total_c}\nTotal enrollments: {total_enr}\nCourse with the most students: {max_c_s} (ID: {id_max_c}, Name: {name_max_c})\nStudent with the highest avg: N/A\nOverall avg: N/A")
        

def main():
    print("====== UNIVERSITY MANAGEMENT SYSTEM ======")
    uni = University()
    
    while True:
        num = get_num("\n1. Show students\n2. Add student\n3. Show courses\n4. Add course\n5. Find student\n6. Find course\n7. Enroll student\n8. Unenroll student\n9. Add grade\n10. Show statistics\n11. Exit\n\nChoose: ")
        match(num):
            case 1: uni.show_students()
            case 2: uni.add_student()
            case 3: uni.show_courses()
            case 4: uni.add_course()
            case 5: uni.find_student()
            case 6: uni.find_course()
            case 7: uni.enroll_student()
            case 8: uni.unenroll_student()
            case 9: uni.add_grade()
            case 10: uni.show_statistics()
            case 11: break
    
    print("\nGoodbye!")

def get_num(p):
    while True:
        try:
            n = int(input(p))
            return n if (1 <= n <= 11) else print("\nChoose between 1 and 11.")
        except ValueError:
            continue

main()
