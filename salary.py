# from employee import employee
# from attendance import attendance, work_hours

# def calculate_salary(emp_id, month):
#     found = False
#     for emp in employee:
#         if emp["id"] == emp_id:
#             found = True
#             name = emp["name"]
#             position = emp["position"]
#             base_salary = emp["salary"]
#             break

#     if found == False:
#         print("Employee not found")
#         return

#     days_present = 0
#     total_hours = 0

#     if emp_id in attendance:
#         for date in attendance[emp_id]:

#             if month in date:

#                 if attendance[emp_id][date].lower() == "present":
#                     days_present = days_present + 1

#                     if emp_id in work_hours:
#                         if date in work_hours[emp_id]:
#                             total_hours = total_hours + work_hours[emp_id][date]

#     bonus = 0

#     if days_present >= 22:
#         bonus = 2000

#     net_salary = base_salary + bonus

#     print("\n=== PAYROLL SUMMARY ===")
#     print("Employee Name:", name)
#     print("Employee ID:", emp_id)
#     print("Position:", position)
#     print("Month:", month)
#     print("Days Present:", days_present)
#     print("Total Hours Worked:", total_hours)
#     print("Base Salary:", base_salary)
#     print("Bonus:", bonus)
#     print("Net Salary:", net_salary)