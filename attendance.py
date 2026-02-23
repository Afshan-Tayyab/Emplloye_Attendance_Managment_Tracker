from employee import employee

attendance = {
    1: {  # John Doe - Software Engineer
        "01-01-2026": "Present",
        "02-01-2026": "Present", 
        "03-01-2026": "Present",
        "04-01-2026": "Present",
        "05-01-2026": "Present"
    },
    2: {  # Jane Smith - Product Manager
        "01-01-2026": "Present",
        "02-01-2026": "Present",
        "03-01-2026": "Present", 
        "04-01-2026": "Present",
        "05-01-2026": "Present"
    },
    3: {  # Alice Johnson - Data Scientist
        "01-01-2026": "Present",
        "02-01-2026": "Absent",
        "03-01-2026": "Present",
        "04-01-2026": "Present",
        "05-01-2026": "Absent"
    },
    4: {  # Bob Brown - UX Designer
        "01-01-2026": "Present",
        "02-01-2026": "Present",
        "03-01-2026": "Absent",
        "04-01-2026": "Present",
        "05-01-2026": "Present"
    },
    5: {  # Charlie Davis - DevOps Engineer
        "01-01-2026": "Present",
        "02-01-2026": "Absent",
        "03-01-2026": "Present",
        "04-01-2026": "Present",
        "05-01-2026": "Present"
    }
}

work_hours = {
    1: {  # John Doe
        "01-01-2026": 8,
        "02-01-2026": 8,
        "03-01-2026": 8,
        "04-01-2026": 8,
        "05-01-2026": 8
    },
    2: {  # Jane Smith
        "01-01-2026": 8,
        "02-01-2026": 8,
        "03-01-2026": 8,
        "04-01-2026": 8,
        "05-01-2026": 8
    },
    3: {  # Alice Johnson
        "01-01-2026": 8,
        "02-01-2026": 0,
        "03-01-2026": 8,
        "04-01-2026": 8,
        "05-01-2026": 0
    },
    4: {  # Bob Brown
        "01-01-2026": 8,
        "02-01-2026": 8,
        "03-01-2026": 0,
        "04-01-2026": 8,
        "05-01-2026": 8
    },
    5: {  # Charlie Davis
        "01-01-2026": 8,
        "02-01-2026": 0,
        "03-01-2026": 8,
        "04-01-2026": 8,
        "05-01-2026": 8
    }
}

def mark_attendance(emp_id, date, status):
    # Check if employee exists without flag variable
    for emp in employee:
        if emp['id'] == emp_id:
            # Employee found
            if emp_id not in attendance:
                attendance[emp_id] = {}
            
            if date in attendance[emp_id]:
                print("Attendance already marked for this date")
                return
            
            attendance[emp_id][date] = status
            print("Attendance Marked")
            return
    
    # Employee not found
    print("Employee ID not found in system")

def record_work_hours(emp_id, date, hours):
    # Check if employee exists without flag variable
    for emp in employee:
        if emp['id'] == emp_id:
            # Employee found
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
            return
    
    # Employee not found
    print("Employee ID not found in system")

def monthly_attendance(emp_id, month):
    for emp in employee:
        if emp['id'] == emp_id:
            if emp_id not in attendance:
                print("No attendance found")
                return
            
            print(f"\nAttendance for {month}")
            for date in attendance[emp_id]:
                if date.endswith(month):  # Checks if date ends with "01-2026"
                    print(f"{date}: {attendance[emp_id][date]}")
            return
    
    print("Employee not found")
 