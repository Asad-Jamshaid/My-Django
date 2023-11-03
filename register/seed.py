from faker import faker 
fake = Faker()  
import random
from .models import *

def seed_db(n = 10) -> None:
    for _ in range(n):
        departments_obj = Department.objects.all() 
        random_index = random.randint(0, len(departments_obj)) 
        department = department_obj[random_index] 
        student_id = f'STU-0-{random.randint(100, 999)}'
        student_name = fake.name()  
        student_email = fake.email() 
        student_age = random.randint(20, 30) 
        student_address = fake.address()

        student_id_obj = StudentID.objects.create(student_id = student_id)  

        student_obj = Student.objects.create(
            department = department,
            student_id = student_id_obj,
            student_name = student_name,
            student_email = student_email,
            student_age = student_age,
            student_address = student_address,
        )