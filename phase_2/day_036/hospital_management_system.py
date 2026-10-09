# Day 36 9/10/26

from datetime import datetime
import re

PATTERN_STRING = r"[A-Za-z\s]+"

class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    
    def display(self):
        print(f"\nID: {self.id}\nName: {self.name}\nAge: {self.age}")

class Patient(Person):
    def __init__(self, id, name, age, medical_record_number):
        super().__init__(id, name, age)
        self.medical_record_number = medical_record_number
        self.appointments = []
    
    def display(self):
        super().display()
        print(f"Medical record number: {self.medical_record_number}")

class Doctor(Person):
    def __init__(self, id, name, age, specialty, consultation_fee):
        super().__init__(id, name, age)
        self.specialty = specialty
        self.consultation_fee = consultation_fee
    
    def display(self):
        super().display()
        print(f"Specialty: {self.specialty}\nConsultation fee: {self.consultation_fee}")

class Appointment:
    def __init__(self, id, patient, doctor, date):
        self.id = id
        self.patient = Patient(patient.id, patient.name, patient.age, patient.medical_record_number)
        self.doctor = Doctor(doctor.id, doctor.name, doctor.age, doctor.specialty, doctor.consultation_fee)
        self.date = date
        self.status = "Scheduled"
    
    def display(self):
        print(f"\nID: {self.id}\nPatient:")
        print("-" * 40)
        self.patient.display()
        print("\nDoctor:")
        print("-" * 40)
        self.doctor.display()
        print("\n" + "-" * 40)
        print(f"\nDate: {self.date}\nStatus: {self.status}")
        print("\n" + "-" * 40)
    
    def cancel(self):
        self.status = "Cancelled"
    
    def complete(self):
        self.status = "Completed"

class Hospital:
    def __init__(self):
        self.patients, self.doctors, self.appointments = [], [], []
    
    def add_patient(self):
        id, nm, a, mrn = 0, "", 0, 0
        
        while True:
            try:
                id = abs(int(input("\nID: ")))
            except ValueError:
                continue
            if (len(self.patients) == 0) and id != 0:
                break
            
            flag = True
            
            for p in self.patients:
                if id == p.id:
                    print(f"\nPatient with ID {id} already exists")
                    id, flag = 0, False
                    break
            
            if flag and id != 0:
                break
        
        while not re.fullmatch(PATTERN_STRING, nm):
            nm = input("Name: ")
        
        while a == 0:
            try:
                a = abs(int(input("Age: ")))
            except ValueError:
                continue
        
        while mrn == 0:
            try:
                mrn = abs(int(input("Medical record number: ")))
            except ValueError:
                continue
        
        self.patients.append(Patient(id, nm, a, mrn))
    
    def add_doctor(self):
        id, nm, a, sp, cf = 0, "", 0, "", 0.0
        
        while True:
            try:
                id = abs(int(input("\nID: ")))
            except ValueError:
                continue
            
            flag = True
            
            for d in self.doctors:
                if id == d.id:
                    print(f"\nDoctor with ID {id} already exists!")
                    id, flag = 0, False
                    break
            
            if flag and id != 0:
                break
        
        while not re.fullmatch(PATTERN_STRING, nm):
            nm = input("Name: ")
        
        while a == 0:
            try:
                a = abs(int(input("Age: ")))
            except ValueError:
                continue
        
        while not re.fullmatch(PATTERN_STRING, sp):
            sp = input("Specialty: ")
        
        while cf == 0.0:
            try:
                cf = abs(float(input("Consultation fee: ")))
            except ValueError:
                continue
        
        self.doctors.append(Doctor(id, nm, a, sp, cf))
    
    def show_patients(self):
        if len(self.patients) == 0:
            return print("\nNo patiens found!")
        
        for p in self.patients:
            p.display()
    
    def show_doctors(self):
        if len(self.doctors) == 0:
            return print("\nNo doctors found!")
        
        for d in self.doctors:
            d.display()
    
    def find_patient(self):
        if len(self.patients) == 0:
            return print("\nNo patients found!")
        
        id, flag = 0, False
        
        while id == 0:
            try:
                id = abs(int(input("\nID: ")))
            except ValueError:
                continue
        
        for p in self.patients:
            if id == p.id:
                p.display()
                flag = True
        
        if not flag:
            print("\nPatient with ID {id} not found!")
    
    def find_doctor(self):
        if len(self.doctors) == 0:
            return print("\nNo doctors found!")
        
        id, flag = 0, False
        
        while id == 0:
            try:
                id = abs(int(input("\nID: ")))
            except ValueError:
                continue
        
        for d in self.doctors:
            if id == d.id:
                d.display()
                flag = True
        
        if not flag:
            print(f"\nDoctor with ID {id} not found!")
    
    def create_appointment(self):
        if (len(self.patients) == 0) or (len(self.doctors) == 0):
            return print("\nNo patients and/or doctors found!")
        
        p_id, pos_p, d_id, pos_d, ad = 0, 0, 0, 0, ""
        
        while True:
            try:
                p_id = abs(int(input("\nPatient ID: ")))
            except ValueError:
                continue
            
            flag = False
            
            for i, p in enumerate(self.patients):
                if p_id == p.id:
                    pos_p, flag = i, True
            
            if flag:
                break
            print(f"\nPatient with ID {p_id} not found!")
        
        while True:
            try:
                d_id = abs(int(input("Doctor ID: ")))
            except ValueError:
                continue
            
            flag = False
            
            for i, d in enumerate(self.doctors):
                if d_id == d.id:
                    pos_d, flag = i, True
            
            if flag:
                break
            print(f"\nDoctor with ID {d_id} not found!")
        
        while True:
            ad = input("Appointment date (YYYY-MM-DD): ")
            if is_valid_date(ad):
                break
            print("\nEnter a valid date!")
        
        p, d = self.patients[pos_p], self.doctors[pos_d]
        
        if len(self.appointments) == 0:
            temp = Appointment(1, p, d, ad)
            self.appointments.append(temp)
            p.appointments.append(temp)
            print("\nAppointment created successfully!")
        else:
            id, flag = len(self.appointments), True
            
            for a in self.appointments:
                if p_id == a.patient.id and d_id == a.doctor.id and ad == a.date:
                    print(f"\nThis appointment with doctor {d_id} and patient {p_id} and date {ad} already exists!")
                    flag = False
                
            if flag:
                temp = Appointment(id+1, p, d, ad)
                self.appointments.append(temp)
                p.appointments.append(temp)
                print("\nAppointment created successfully!")
                    
    def show_appointments(self):
        if len(self.appointments) == 0:
            return print("\nNo appointments found!")
        
        for a in self.appointments:
            a.display()
    
    def cancel_appointment(self):
        if len(self.appointments) == 0:
            return print("\nNo appointments found!")
        
        a_id, pos_a = 0, 0
        
        while True:
            try:
                a_id = abs(int(input("\nID: ")))
            except ValueError:
                continue
            
            flag = False
            
            for i, a in enumerate(self.appointments):
                if a_id == a.id:
                    pos_a, flag = i, True
                    break
            
            if flag:
                break
        
        a = self.appointments[pos_a]
        if a.status != "Completed":
            a.cancel()
            print(f"\nAppointment {a_id} cancelled!")
        else:
            print("\nAppointment that has been completed cannot be cancelled!")
    
    def complete_appointment(self):
        if len(self.appointments) == 0:
            return print("\nNo appointments found!")
        
        a_id, pos_a = 0, 0
        
        while True:
            try:
                a_id = abs(int(input("\nID: ")))
            except ValueError:
                continue
            
            flag = False
            
            for i, a in enumerate(self.appointments):
                if a_id == a.id:
                    pos_a, flag = i, True
                    break
            
            if flag:
                break
        
        a = self.appointments[pos_a]
        if a.status != "Cancelled":
            a.complete()
            print(f"\nAppointment {a_id} completed!")
        else:
            print("\nAppointment that has been cancelled cannot be completed!")
    
    def show_statistics(self):
        total_p, total_d, total_a = len(self.patients), len(self.doctors), len(self.appointments)
        temp, sch_a, com_a, can_a, max_req_sp, nm_max_req_sp = {}, 0, 0, 0, 0, ""
        
        if total_a == 0:
            print(f"Total patients: {total_p}\nTotal doctors: {total_d}\nTotal appointments: {total_a}")
        else:
            for a in self.appointments:
                if a.status == "Scheduled":
                    sch_a += 1
                elif a.status == "Cancelled":
                    can_a += 1
                else:
                    com_a += 1
                if a.doctor.specialty not in temp:
                    temp[f"{a.doctor.specialty}"] = 1
                else:
                    temp[f"{a.doctor.specialty}"] += 1
            
            for k, v in temp.items():
                if v > max_req_sp:
                    max_req_sp = v
                    nm_max_req_sp = k
                    
            print(f"Total patients: {total_p}\nTotal doctors: {total_d}\nTotal appointments: {total_a}\nScheduled: {sch_a}\nCompleted: {com_a}\nCancelled: {can_a}\nMost requested specialty: {nm_max_req_sp} ({max_req_sp})")
        
def main():
    print("===== HOSPITAL MANAGEMENT SYSTEM =====")
    hospital = Hospital()
    
    while True:
        num = get_int("\n1. Show patients\n2. Add patient\n3. Show doctors\n4. Add doctor\n5. Find patient\n6. Find doctor\n7. Create appointment\n8. Show appointments\n9. Cancel appointment\n10. Complete appointment\n11. Show statistics\n12. Exit\n\nChoose: ")
        match(num):
            case 1: hospital.show_patients()
            case 2: hospital.add_patient()
            case 3: hospital.show_doctors()
            case 4: hospital.add_doctor()
            case 5: hospital.find_patient()
            case 6: hospital.find_doctor()
            case 7: hospital.create_appointment()
            case 8: hospital.show_appointments()
            case 9: hospital.cancel_appointment()
            case 10: hospital.complete_appointment()
            case 11: hospital.show_statistics()
            case 12: break

    print("\nGoodbye!")

def get_int(p):
    while True:
        try:
            n = int(input(p))
        except ValueError:
            continue
        return n if (1 <= n <= 12) else print("\nChoose between 1 and 12")

def is_valid_date(d, date_format="%Y-%m-%d"):
    try:
        datetime.strptime(d, date_format)
        return True
    except ValueError:
        return False

main()
