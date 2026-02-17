attendance={}
def mark_attendance(emp_id,date,status):
    if emp_id not in attendance:
        attendance[emp_id] = {}
    if date in attendance[emp_id]:
        print("Attendance already marked")
        return
    attendance[emp_id][date] = status
    print("Attendance Marked")
 
work_hours={}
def record_work_hours(emp_id, date, hours):
    if hours <= 0:
        print("Invalid working hours")
        return
    if emp_id not in work_hours:
        work_hours[emp_id] = {}
    if date in work_hours[emp_id]:
        print("Working hours already recorded for this date")
        return
    work_hours[emp_id][date] = hours
    print("Working hours recorded successfully")
 
def monthly_attendance(emp_id,month):
    if emp_id not in attendance:
        print("No attendance found.")
        return
    print("\nMonthly Attendance for", month)
    print("---------------------------")
    for date in attendance[emp_id]:
        if month in date:
            print(date, ":", attendance[emp_id][date])
 