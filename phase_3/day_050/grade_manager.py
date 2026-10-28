# Day 50 27/10/26

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
    
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    
    def get_average(self):
        return (sum(self.grades)/len(self.grades)) if len(self.grades) != 0 else None
    
    
    def display_info(self):
        if len(self.grades) == 0:
            print(f"\nID: {self.student_id}\nName: {self.name}\nGrades: []\nAverage: No grades yet")
        else:
            print(f"\nID: {self.student_id}\nName: {self.name}\nGrades:")
            for i, g in enumerate(self.grades):
                print(f"{i+1}. {g}")
            avg = self.get_average()
            print(f"Average: {avg:.2f}")

class GradeManager:
    def __init__(self):
        self.students = []
    
    
    def add_student(self):
        s_id, n = len(self.students) + 1, ""
        
        while not n.strip():
            n = input("\nName: ")

            if any(n.lower() == s.name.lower() for s in self.students):
                print(f"\nStudent with name {n} already exists!")
                n = ""
        
        self.students.append(Student(s_id, n))
        print("\nStudent was added successfully!")
    
    
    def display_students(self):
        if len(self.students) == 0:
            return print("\nNo students found!")
        
        for s in self.students:
            s.display_info()
    
    
    def search_student(self):
        if len(self.students) == 0:
            return print("\nNo students found!")
        
        txt, flag, s_id = "", False, None
        
        while not txt.strip():
            txt = input("\nEnter either the name or the ID: ")
        
        if txt.isdigit():
            s_id = int(txt)
        
        for s in self.students:
            if txt.lower() == s.name.lower() or (s_id is not None and s_id == s.student_id):
                flag = True
                s.display_info()
        
        if not flag:
            if s_id is not None:
                return print(f"\nNo student with ID {s_id} was found!")
            
            return print(f"\nNo student with name {txt} was found!")
    
    
    def add_grade_to_student(self):
        if len(self.students) == 0:
            return print("\nNo students found!")
        
        n, g, flag = "", 0.0, False
        
        while not n.strip():
            n = input("\nStudent name: ")
        
        for s in self.students:
            if n.lower() == s.name.lower():
                flag = True
                while True:
                    try:
                        g = float(input("\nGrade: "))
                        
                        if 0 <= g <= 100:
                            break
                        
                        print("\nOnly floating numbers between 0 and 100.")
                    except ValueError:
                        print("\nOnly numbers!")
                
                s.add_grade(g)
                print("\nGrade added successfully!")
        
        if not flag:
            print(f"\nNo student with name {n} was found!")
    
    
    def display_top_student(self):
        if len(self.students) == 0:
            return print("\nNo students found!")
        
        temp, avg_max, s_max = 0.0, 0.0, None
        
        for s in self.students:
            if s.grades:
                temp = s.get_average()
                if temp >= avg_max:
                    avg_max = temp
                    s_max = s
        
        if s_max is not None:
            s_max.display_info()
        else:
            print("\nNo averages were found!")
    
    def display_class_average(self):
        if len(self.students) == 0:
            return print("\nNo students found!")
        
        avg, sum_avg, total_count_avg = 0, 0, 0
        
        for s in self.students:
            if s.grades:
                total_count_avg += len(s.grades)
                for g in s.grades:
                    sum_avg += g
        
        try:
            avg = sum_avg/total_count_avg
        except ZeroDivisionError:
            return print("\nNo division with 0!")
            
        print(f"\nTotal class average: {avg:.2f}")


def main():
    print("========== GRADE MANAGER ==========")
    
    grade_manager = GradeManager()
    
    while True:
        num = get_num("\n1. Add student\n2. Display all students\n3. Search student\n4. Add grade to student\n5. Display top student\n6. Display class average\n7. Exit\n\nChoose: ")
        
        match(num):
            case 1:
                grade_manager.add_student()
            case 2:
                grade_manager.display_students()
            case 3:
                grade_manager.search_student()
            case 4:
                grade_manager.add_grade_to_student()
            case 5:
                grade_manager.display_top_student()
            case 6:
                grade_manager.display_class_average()
            case 7:
                break
    
    print("\nGoodbye!")


def get_num(p):
    while True:
        try:
            n = int(input(p))
            
            if 1 <= n <= 7:
                return n
                
            print("\nChoose between 1 and 7!")
        except ValueError:
            print("\nOnly numbers!")


main()
