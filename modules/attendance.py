import json
import os
from modules.scanner import NetworkScanner

class AttendanceTracker:
    """
    Attendance tracker class that handles loading, saving, and marking attendance.
    """
    def __init__(self, data_file="data/data.json", attendance_file = "data/attendance.json"):
        self.data_file = data_file
        self.attendance_file = attendance_file

    def save_attendance(self, students):
        """
        Saves the current attendance list to the JSON file.
        """
        os.makedirs(os.path.dirname(self.attendance_file), exist_ok=True)
        # Ensure the data folder exists before saving
        with open(self.attendance_file, "w") as file:
            json.dump(students, file, indent=4)
            # Save attendance list to JSON nicely formatted

    def load_data(self):
        with open(self.data_file, "r") as file:
            data = json.load(file)
            return data
            
    
    def mark_present(self, net_range=None):
        student_data = self.load_data()  
        scanner = NetworkScanner(net_range)  
        devices = scanner.scan() 

       #I put the loop through devices outside to make work clearer
        online_macs = {device['mac']for device in devices}
        
        #  Initialize an empty list to collect students found during this specific scan
        present_students = []

        # We iterate through student database one by one.
        for student in student_data:
            
            if student["mac_address"] in online_macs:
                student["status"] = "Present"
                present_students.append(student)                
                print(f"Student Found: {student.get('name', 'Student')} is present.")
        # Saving the results:)
        # If the list isn't empty save it to attendance.json.
        if present_students:
            self.save_attendance(present_students)
        else:
            print("Scan complete: No matching students found on this network.")
