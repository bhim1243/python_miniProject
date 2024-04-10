import csv
from tkinter import *
from tkinter import messagebox
from openpyxl import Workbook


# Function to register a new student
def register_student():
    def submit_registration():
        student_id = student_id_entry.get()
        name = name_entry.get()
        address = address_entry.get()
        dob = dob_entry.get()

        # Write student details to CSV file
        with open('students.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_id, name, address, dob])

        messagebox.showinfo("Success", "Student registered successfully!")

    # Create registration window
    register_window = Tk()
    register_window.title("Register Student")

    # Create labels and entry fields
    Label(register_window, text="Student ID:").grid(row=0, column=0, padx=10, pady=5)
    student_id_entry = Entry(register_window)
    student_id_entry.grid(row=0, column=1, padx=10, pady=5)

    Label(register_window, text="Name:").grid(row=1, column=0, padx=10, pady=5)
    name_entry = Entry(register_window)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    Label(register_window, text="Address:").grid(row=2, column=0, padx=10, pady=5)
    address_entry = Entry(register_window)
    address_entry.grid(row=2, column=1, padx=10, pady=5)

    Label(register_window, text="Date of Birth (DD/MM/YYYY):").grid(row=3, column=0, padx=10, pady=5)
    dob_entry = Entry(register_window)
    dob_entry.grid(row=3, column=1, padx=10, pady=5)

    # Create submit button
    submit_button = Button(register_window, text="Submit", command=submit_registration, padx=10, pady=5)
    submit_button.grid(row=4, column=1, padx=10, pady=10)

    register_window.mainloop()


# Function to record fee payment for a student
def record_fee_payment():
    pass


# Function to check fee balance for a student
def check_fee_balance():
    pass


# Function to print student ID card for a student
def print_student_id_card(student_id, name, address, dob):
    # Create a new window for displaying ID card
    id_card_window = Tk()
    id_card_window.title("Student ID Card")

    # Create labels to display student information
    Label(id_card_window, text="Student ID:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    Label(id_card_window, text=student_id).grid(row=0, column=1, padx=10, pady=5)

    Label(id_card_window, text="Name:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    Label(id_card_window, text=name).grid(row=1, column=1, padx=10, pady=5)

    Label(id_card_window, text="Address:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    Label(id_card_window, text=address).grid(row=2, column=1, padx=10, pady=5)

    Label(id_card_window, text="Date of Birth:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    Label(id_card_window, text=dob).grid(row=3, column=1, padx=10, pady=5)



# Main menu
def main():
    root = Tk()
    root.title("School Management System")

    # Set the size of the window
    root.geometry("400x200")

    # Add padding
    root.config(padx=10, pady=10)

    # Create buttons for various functions with grid layout
    register_button = Button(root, text="Register Student", command=register_student, padx=10, pady=5)
    register_button.grid(row=0, column=0, padx=10, pady=5)

    record_fee_payment_button = Button(root, text="Record Fee Payment", command=record_fee_payment, padx=10, pady=5)
    record_fee_payment_button.grid(row=1, column=0, padx=10, pady=5)

    check_fee_balance_button = Button(root, text="Check Fee Balance", command=check_fee_balance, padx=10, pady=5)
    check_fee_balance_button.grid(row=2, column=0, padx=10, pady=5)

    print_id_card_button = Button(root, text="Print Student ID Card", command=print_student_id_card, padx=10, pady=5)
    print_id_card_button.grid(row=3, column=0, padx=10, pady=5)



    root.mainloop()


if __name__ == "__main__":
    main()
