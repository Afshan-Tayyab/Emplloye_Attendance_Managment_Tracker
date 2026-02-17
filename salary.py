from employee import employee
from attendance import attendance

def calculate_salary(emp_id, month):
    if emp_id not in employee:
        print("Employee not found.")
        return

    days_present = set()
    total_hours = 0

    if emp_id in attendance:
        for rec in attendance[emp_id]:
            if rec["date"].startswith(month) and rec["status"].lower() == "present":
                days_present.add(rec["date"])
                total_hours += rec["hours"]

    base = employee[emp_id]["salary"]
    bonus = 2000 if len(days_present) >= 22 else 0
    net = base + bonus

    print("\n=== PAYROLL SUMMARY ===")
    print("Employee:", employee[emp_id]["name"], f"({emp_id})")
    print("Position:", employee[emp_id]["position"])
    print("Month:", month)
    print("Days Present:", len(days_present))
    print("Total Hours:", total_hours)
    print("Base Salary:", base)
    print("Bonus:", bonus)
    print("Net Pay:", net)
 