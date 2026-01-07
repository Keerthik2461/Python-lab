import re
from collections import defaultdict

# -------------------------------
# Student Class
# -------------------------------
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.activities = []

    def add_activity(self, activity, date, time):
        self.activities.append((activity, date, time))

    def display_summary(self):
        logins = sum(1 for a in self.activities if a[0] == "LOGIN")
        submissions = sum(1 for a in self.activities if a[0] == "SUBMIT_ASSIGNMENT")
        return logins, submissions


# -------------------------------
# Generator to read log file
# -------------------------------
def read_log_file(filename):
    with open(filename, "r") as file:
        for line in file:
            try:
                parts = [p.strip() for p in line.strip().split("|")]

                if len(parts) != 5:
                    raise ValueError

                student_id, name, activity, date, time = parts

                if not re.match(r"^S\d+$", student_id):
                    raise ValueError

                if activity not in ["LOGIN", "LOGOUT", "SUBMIT_ASSIGNMENT"]:
                    raise ValueError

                if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
                    raise ValueError

                if not re.match(r"^\d{2}:\d{2}$", time):
                    raise ValueError

                yield student_id, name, activity, date, time

            except ValueError:
                print("Invalid log entry skipped:", line.strip())


# -------------------------------
# MAIN PROGRAM
# -------------------------------
students = {}
daily_activity = defaultdict(int)
login_tracker = defaultdict(int)

# 🔹 USER INPUT FILE
input_file = input("Enter activity log file name: ")
output_file = "activity_report.txt"

try:
    for sid, name, activity, date, time in read_log_file(input_file):

        if sid not in students:
            students[sid] = Student(sid, name)

        students[sid].add_activity(activity, date, time)
        daily_activity[date] += 1

        if activity == "LOGIN":
            login_tracker[sid] += 1
        elif activity == "LOGOUT":
            login_tracker[sid] = max(0, login_tracker[sid] - 1)

except FileNotFoundError:
    print("❌ File not found. Please check the file name.")
    exit()


# -------------------------------
# OUTPUT REPORT
# -------------------------------
with open(output_file, "w") as out:

    out.write("STUDENT ACTIVITY REPORT\n")
    out.write("-" * 50 + "\n")

    for student in students.values():
        logins, submissions = student.display_summary()
        out.write(f"Student ID   : {student.student_id}\n")
        out.write(f"Name         : {student.name}\n")
        out.write(f"Total Logins : {logins}\n")
        out.write(f"Submissions  : {submissions}\n\n")

    out.write("DAILY ACTIVITY STATISTICS\n")
    out.write("-" * 50 + "\n")

    for date, count in daily_activity.items():
        out.write(f"{date} : {count} activities\n")

    out.write("\nABNORMAL BEHAVIOR DETECTED\n")
    out.write("-" * 50 + "\n")

    abnormal = False
    for sid, count in login_tracker.items():
        if count > 0:
            abnormal = True
            out.write(f"{sid} has multiple logins without logout\n")

    if not abnormal:
        out.write("No abnormal behavior detected\n")

print("✅ Report created:", output_file)