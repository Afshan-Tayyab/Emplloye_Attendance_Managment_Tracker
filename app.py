import streamlit as st
from employee import (
    add_employee,
    view_all,
    search_by_id,
    search_by_name,
    update_salary,
    delete_employee,
    employee
)
from attendance import (
    mark_attendance,
    record_work_hours,
    monthly_attendance,
    attendance,
    work_hours
)

st.set_page_config(
    page_title="Employee Management System",
    page_icon="👨‍💼",
    layout="wide"
)

st.title("Employee Attendance Management System")
st.write("Manage employees, attendance, working hours and salaries.")

st.sidebar.title("Menu")

menu = st.sidebar.radio(
    "Select an option",
    [
        "Dashboard",
        "Add Employee",
        "Attendance",
        "Working Hours",
        "Attendance Report",
        "Employees",
        "Search Employee",
        "Update Salary",
        "Delete Employee"
    ]
)

# Dashboard
if menu == "Dashboard":
    st.header("Dashboard")

    total_employees = len(employee)

    present_count = 0
    absent_count = 0

    for emp_id in attendance:
        for date in attendance[emp_id]:
            if attendance[emp_id][date].lower() == "present":
                present_count += 1
            elif attendance[emp_id][date].lower() == "absent":
                absent_count += 1

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Employees", total_employees)
    col2.metric("Present Records", present_count)
    col3.metric("Absent Records", absent_count)

    st.subheader("Employee List")
    st.dataframe(employee, use_container_width=True)


# Add Employee
elif menu == "Add Employee":
    st.header("Add Employee")

    emp_id = st.number_input("Employee ID", min_value=1, step=1)
    name = st.text_input("Employee Name")
    position = st.text_input("Position")
    department = st.text_input("Department")
    salary = st.number_input("Salary", min_value=0.0, step=1000.0)

    if st.button("Add Employee"):
        if name and position and department:
            result = add_employee(
                emp_id,
                name,
                position,
                department,
                salary
            )
            st.success(result)
        else:
            st.warning("Please fill all fields.")


# Attendance
elif menu == "Attendance":
    st.header("Mark Attendance")

    emp_id = st.number_input("Employee ID", min_value=1, step=1)
    date = st.text_input("Date", placeholder="DD-MM-YYYY")
    status = st.selectbox("Status", ["Present", "Absent"])

    if st.button("Mark Attendance"):
        if date:
            mark_attendance(emp_id, date, status)
            st.success("Attendance processed.")
        else:
            st.warning("Please enter a date.")


# Working Hours
elif menu == "Working Hours":
    st.header("Record Working Hours")

    emp_id = st.number_input("Employee ID", min_value=1, step=1)
    date = st.text_input("Date", placeholder="DD-MM-YYYY")
    hours = st.number_input("Hours Worked", min_value=0, max_value=24, step=1)

    if st.button("Record Hours"):
        if date:
            record_work_hours(emp_id, date, hours)
            st.success("Working hours processed.")
        else:
            st.warning("Please enter a date.")


# Attendance Report
elif menu == "Attendance Report":
    st.header("Monthly Attendance Report")

    emp_id = st.number_input("Employee ID", min_value=1, step=1)
    month = st.text_input(
        "Month",
        placeholder="MM-YYYY",
        help="Example: 01-2026"
    )

    if st.button("View Attendance"):
        if emp_id in attendance:
            records = []

            for date, status in attendance[emp_id].items():
                if date.endswith(month):
                    records.append({
                        "Date": date,
                        "Status": status
                    })

            if records:
                st.dataframe(records, use_container_width=True)
            else:
                st.info("No attendance found for this month.")
        else:
            st.info("No attendance found for this employee.")


# Employees
elif menu == "Employees":
    st.header("All Employees")

    st.dataframe(employee, use_container_width=True)


# Search Employee
elif menu == "Search Employee":
    st.header("Search Employee")

    search_type = st.selectbox(
        "Search by",
        ["Employee ID", "Employee Name"]
    )

    if search_type == "Employee ID":
        emp_id = st.number_input("Employee ID", min_value=1, step=1)

        if st.button("Search"):
            result = search_by_id(emp_id)

            if isinstance(result, dict):
                st.json(result)
            else:
                st.warning(result)

    else:
        name = st.text_input("Employee Name")

        if st.button("Search"):
            result = search_by_name(name)

            if isinstance(result, dict):
                st.json(result)
            else:
                st.warning(result)


# Update Salary
elif menu == "Update Salary":
    st.header("Update Employee Salary")

    emp_id = st.number_input("Employee ID", min_value=1, step=1)
    new_salary = st.number_input(
        "New Salary",
        min_value=0.0,
        step=1000.0
    )

    if st.button("Update Salary"):
        result = update_salary(emp_id, new_salary)
        st.success(result)


# Delete Employee
elif menu == "Delete Employee":
    st.header("Delete Employee")

    emp_id = st.number_input("Employee ID", min_value=1, step=1)

    if st.button("Delete Employee"):
        result = delete_employee(emp_id)
        st.warning(result)