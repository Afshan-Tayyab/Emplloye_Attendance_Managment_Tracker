import streamlit as st
from employee import add_employee, view_all, search_by_id, search_by_name, update_salary, delete_employee
from attendance import mark_attendance, record_work_hours, monthly_attendance
from salary import calculate_salary

st.title("📝 Employee Management System")
st.subheader("Manage Smart, Work Better")

menu = [
    "Add Employee",
    "Mark Attendance",
    "Record Working Hours",
    "View Monthly Attendance Report",
    "Calculate Salary",
    "View All Employees",
    "Search Employee by Name or ID",
    "Update Employee Salary",
    "Delete Employee Record"
]

choice = st.sidebar.selectbox("Select Action", menu)

if choice == "Add Employee":
    st.header("Add New Employee")
    emp_id = st.number_input("Enter ID", step=1)
    name = st.text_input("Enter Name")
    position = st.text_input("Enter Position")
    department = st.text_input("Enter Department")
    salary = st.number_input("Enter Salary", step=1.0)
    if st.button("Add Employee"):
        result = add_employee(emp_id, name, position, department, salary)
        st.write(result)

elif choice == "Mark Attendance":
    st.header("Mark Attendance")
    emp_id = st.number_input("Enter Employee ID", step=1)
    date = st.date_input("Select Date")
    status = st.selectbox("Status", ["Present", "Absent"])
    if st.button("Mark Attendance"):
        mark_attendance(emp_id, date.strftime("%d-%m-%Y"), status)
        st.success(f"Attendance marked for Employee ID {emp_id} on {date}")

elif choice == "Record Working Hours":
    st.header("Record Working Hours")
    emp_id = st.number_input("Enter Employee ID", step=1)
    date = st.date_input("Select Date")
    hours = st.number_input("Hours Worked", step=1)
    if st.button("Record Hours"):
        record_work_hours(emp_id, date.strftime("%d-%m-%Y"), hours)
        st.success(f"{hours} hours recorded for Employee ID {emp_id} on {date}")

elif choice == "View Monthly Attendance Report":
    st.header("Monthly Attendance Report")
    emp_id = st.number_input("Enter Employee ID", step=1, key="att_emp")
    month = st.text_input("Enter Month (MM-YY)")
    if st.button("View Report"):
        report = monthly_attendance(emp_id, month)
        st.write(report)

elif choice == "Calculate Salary":
    st.header("Calculate Salary")
    emp_id = st.number_input("Enter Employee ID", step=1, key="sal_emp")
    month = st.text_input("Enter Month (MM-YYYY)")
    if st.button("Calculate"):
        salary_info = calculate_salary(emp_id, month)
        st.write(salary_info)

elif choice == "View All Employees":
    st.header("All Employees")
    employees = view_all()
    st.dataframe(employees)

elif choice == "Search Employee by Name or ID":
    st.header("Search Employee")
    search_type = st.radio("Search by", ["ID", "Name"])
    if search_type == "ID":
        emp_id = st.number_input("Enter Employee ID", step=1, key="search_id")
        if st.button("Search by ID"):
            st.write(search_by_id(emp_id))
    else:
        name = st.text_input("Enter Name", key="search_name")
        if st.button("Search by Name"):
            st.write(search_by_name(name))

elif choice == "Update Employee Salary":
    st.header("Update Salary")
    emp_id = st.number_input("Enter Employee ID", step=1, key="update_id")
    new_salary = st.number_input("Enter New Salary", step=1.0)
    if st.button("Update Salary"):
        result = update_salary(emp_id, new_salary)
        st.write(result)

elif choice == "Delete Employee Record":
    st.header("Delete Employee")
    emp_id = st.number_input("Enter Employee ID", step=1, key="delete_id")
    if st.button("Delete Employee"):
        result = delete_employee(emp_id)
        st.write(result)