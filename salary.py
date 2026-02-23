from employee import employee
from attendance import attendance, work_hours

def calculate_salary(emp_id, month):
    for emp in employee:
        if emp["id"] == emp_id:
            name = emp["name"]
            position = emp["position"]
            base_salary = emp["salary"]
            break
    else:
        print("Employee not found")
        return

    days_present = 0
    total_hours = 0

    if emp_id in attendance:
        for date in attendance[emp_id]:

            if month in date:

                if attendance[emp_id][date].lower() == "present":
                    days_present = days_present + 1

                    if emp_id in work_hours:
                        if date in work_hours[emp_id]:
                            total_hours = total_hours + work_hours[emp_id][date]



    if days_present >= 22:
        bonus = 2000
    else:
        bonus = 0

    net_salary = base_salary + bonus

    print("\n=== PAYROLL SUMMARY ===")
    print("Employee Name:", name)
    print("Employee ID:", emp_id)
    print("Position:", position)
    print("Month:", month)
    print("Days Present:", days_present)
    print("Total Hours Worked:", total_hours)
    print("Base Salary:", base_salary)
    print("Bonus:", bonus)
    print("Net Salary:", net_salary)