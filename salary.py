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
            # Check if date ENDS WITH month (MM-YYYY)
            if date.endswith(month):  # "01-01-2026".endswith("01-2026") = True
                if attendance[emp_id][date].lower() == "present":
                    days_present += 1

                    if emp_id in work_hours:
                        if date in work_hours[emp_id]:
                            total_hours += work_hours[emp_id][date]

    bonus = 0
    if days_present == 5:
        bonus = 2000

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