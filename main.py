from employee import add_employee, view_all, search_by_id, search_by_name, update_salary, delete_employee
from attendance import mark_attendance, record_work_hours, monthly_attendance
# from salary import calculate_salary
def main():
    while True:
        print('\n' + '='*50)
        print("Employee Management System")
        print('='*50)
        print("""
         1. Add Employee
        2. Mark Attendance
        3. Record Working Hours
        4. View Monthly Attendance Report
        5. Calculate Salary
        6. View All Employees
        7. Search Employee by Name or ID
        8. Update Employee Salary
        9. Delete Employee Record
        10. Exit 
        """)
 
        choice = input("Enter your choice: ")
 
        if choice == '1':
            emp_id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            print(add_employee(emp_id, name, position, department, salary))
 
        elif choice == '2':
            emp_id=int(input("Enter Employee_id:"))
            date=input("Enter Date (DD-MM-YYYY): ")
            status=input("Status(Present/Absent):")
            mark_attendance(emp_id,date,status)
 
        elif choice == '3':
            emp_id=int(input("Enter Employee Id:"))
            date=input("Enter Date (DD-MM-YYYY):")
            hours=int(input("Enter hours worked:"))
            record_work_hours(emp_id,date,hours)
 
        elif choice == '4':
            emp_id=int(input("Enter Employee Id:"))
            month=input("Enter the month (MM-YY) for attendance report:")
            monthly_attendance(emp_id,month)
 
        elif choice == '5':
            # emp_id=int(input("Enter Emplooye Id:"))
            # month=input("Enter the month (MM-YY) for attendance report:")
            # calculate_salary(emp_id,month)
            pass
 
 
        elif choice == '6':
            employees = view_all()
            for emp in employees:
                print(emp)
 
        elif choice == '7':
            sub = input("Search by (1) ID or (2) Name: ")
            if sub == '1':
                emp_id = int(input("Enter ID: "))
                print(search_by_id(emp_id))
            else:
                name = input("Enter Name: ")
                print(search_by_name(name))
 
        elif choice == '8':
            emp_id = int(input("Enter ID: "))
            new_salary = float(input("Enter New Salary: "))
            print(update_salary(emp_id, new_salary))
 
        elif choice == '9':
            emp_id = int(input("Enter ID: "))
            print(delete_employee(emp_id))
 
        elif choice == '10':
            print("Exiting the system. Goodbye!")
            break
 
        else:
            print("Invalid choice. Please try again.")
 
if __name__ == "__main__":
    main()
 

 
 