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
        if net_range is None:
            net_range = NetworkUtils.get_local_network()
            print(f"Auto-detected network: {net_range}")

        student_data = self.load_data()  
        scanner = NetworkScanner(net_range)  
        devices = scanner.scan() 

        online_macs = {device['mac'].lower() for device in devices}
        present_students = []

        for student in student_data:
            if student["mac_address"].lower() in online_macs:
                student["status"] = "Present"
                present_students.append(student)                
                print(f"{student.get('name')} is present.")

        if present_students:
            self.save_attendance(present_students)
        else:
            print("Scan complete: No students found.")

# if __name__ == "__main__":
#     tracker = AttendanceTracker()
    
#     detected_range = NetworkUtils.get_local_network()
#     print(f"Current Network Detected: {detected_range}")
    
#     choice = input("Use this range? (y/n): ").lower()
    
#     if choice == 'y':
#         tracker.mark_present(net_range=detected_range)
#     else:
#         custom_range = input("Enter custom network range (e.g. 192.168.1.0/24): ")
#         tracker.mark_present(net_range=custom_range)
