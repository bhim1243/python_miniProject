class Student:
    def __init__(self, student_id, name, dob, address, email, phone_number, major, year_of_study):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.major = major
        self.year_of_study = year_of_study
        self.enrollments = []

    def __str__(self):
        student_info = f"Student ID: {self.student_id}\nName: {self.name}\nDate of Birth: {self.dob}\nAddress: {self.address}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nMajor: {self.major}\nYear of Study: {self.year_of_study}\n"
        enrollment_info = "\n".join([f"Enrollment {i + 1}: {enrollment}" for i, enrollment in enumerate(self.enrollments)])
        return student_info + enrollment_info

    def enroll(self, course, date_enrolled):
        enrollment = Enrollment(course, date_enrolled)
        self.enrollments.append(enrollment)

class Faculty:
    def __init__(self, faculty_id, name, dob, address, email, phone_number, department):
        self.faculty_id = faculty_id
        self.name = name
        self.dob = dob
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.department = department
        self.courses_taught = []

    def __str__(self):
        faculty_info = f"Faculty ID: {self.faculty_id}\nName: {self.name}\nDate of Birth: {self.dob}\nAddress: {self.address}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nDepartment: {self.department}\n"
        courses_taught_info = "\n".join([f"Teaching Course {i + 1}: {course}" for i, course in enumerate(self.courses_taught)])
        return faculty_info + courses_taught_info

    def teach_course(self, course):
        self.courses_taught.append(course)

class Course:
    def __init__(self, course_id, title, description, credit_hours, department):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.credit_hours = credit_hours
        self.department = department
        self.faculty = []

    def __str__(self):
        return f"Course ID: {self.course_id}\nTitle: {self.title}\nDescription: {self.description}\nCredit Hours: {self.credit_hours}\nDepartment: {self.department}"

class Enrollment:
    def __init__(self, course, date_enrolled):
        self.course = course
        self.date_enrolled = date_enrolled

    def __str__(self):
        return f"Course: {self.course.title}, Date Enrolled: {self.date_enrolled}"

class Grade:
    def __init__(self, grade_value, student):
        self.grade_value = grade_value
        self.student = student

    def __str__(self):
        return f"Grade: {self.grade_value}, Student: {self.student.name}"

class Library:
    def __init__(self, book_id, title, author, genre, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = availability

    def __str__(self):
        return f"Book ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nAvailability: {self.availability}"

class Attendance:
    def __init__(self, attendance_id, class_id, student, date, status):
        self.attendance_id = attendance_id
        self.class_id = class_id
        self.student = student
        self.date = date
        self.status = status

    def __str__(self):
        return f"Attendance ID: {self.attendance_id}\nClass ID: {self.class_id}\nStudent: {self.student}\nDate: {self.date}\nStatus: {self.status}"

class Class:
    def __init__(self, class_id, course, faculty, time, room):
        self.class_id = class_id
        self.course = course
        self.faculty = faculty
        self.time = time
        self.room = room
        self.attendance_records = []

    def add_attendance_record(self, attendance_record):
        self.attendance_records.append(attendance_record)

    def __str__(self):
        attendance_info = "\n".join([f"Attendance: {attendance}" for attendance in self.attendance_records])
        return f"Class ID: {self.class_id}\nCourse: {self.course}\nFaculty: {self.faculty}\nTime: {self.time}\nRoom: {self.room}\n{attendance_info}"

class Finance:
    def __init__(self, transaction_id, amount, transaction_date):
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_date = transaction_date
        self.staff_member = None

    def assign_staff_member(self, staff_member):
        self.staff_member = staff_member

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}\nAmount: {self.amount}\nTransaction Date: {self.transaction_date}\nStaff Member: {self.staff_member.name if self.staff_member else 'Not Assigned'}"

class Staff:
    def __init__(self, staff_id, name, date_of_birth, address, email, phone_number, position):
        self.staff_id = staff_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.position = position
        self.financial_transactions = []

    def add_financial_transaction(self, transaction):
        self.financial_transactions.append(transaction)

    def __str__(self):
        return f"Staff ID: {self.staff_id}\nName: {self.name}\nDate of Birth: {self.date_of_birth}\nAddress: {self.address}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nPosition: {self.position}\nFinancial Transactions:\n{('n'.join([str(transaction) for transaction in self.financial_transactions]))}"

