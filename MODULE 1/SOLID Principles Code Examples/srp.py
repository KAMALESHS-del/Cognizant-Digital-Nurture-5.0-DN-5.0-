# Store student data
class Student:

    def __init__(self, name):
        self.name = name


# Save data
class DatabaseManager:

    def save(self, student):
        print(f"Saving {student.name} to database")


# Send email
class EmailService:

    def send_email(self, student):
        print(f"Sending email to {student.name}")


# Generate report
class ReportGenerator:

    def generate_report(self, student):
        print(f"Generating report for {student.name}")


student = Student("Kamalesh")

db = DatabaseManager()
email = EmailService()
report = ReportGenerator()

db.save(student)
email.send_email(student)
report.generate_report(student)