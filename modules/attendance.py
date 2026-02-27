import json
import os

class AttendanceTracker:
    """
    Attendance tracker class that handles loading, saving, and marking attendance.
    """
    def __init__(self, attendance_file="data/attendance.json"):
        self.attendance_file = attendance_file
        self.attendance = self.load_attendance()
        #  Initialize attendance list from file on startup

    def load_attendance(self):
        """
        Loads attendance records from the JSON file.
        Returns an empty list if the file does not exist or is empty.
        """
        if not os.path.exists(self.attendance_file):
            # If the file doesn't exist yet, return empty list
            return []
        with open(self.attendance_file, "r") as file:
            #it reads the file and converts json text into python data
            try:
                return json.load(file)
            except json.JSONDecodeError:
                # Handle empty or corrupt JSON file preventing the program from stopping
                return []

    def save_attendance(self):
        """
        Saves the current attendance list to the JSON file.
        """
        os.makedirs(os.path.dirname(self.attendance_file), exist_ok=True)
        # Ensure the data folder exists before saving
        with open(self.attendance_file, "w") as file:
            json.dump(self.attendance, file, indent=4)
            # Save attendance list to JSON nicely formatted

    def mark_present(self, name, mac):
        """
        Marks a student as present based on their name and MAC address.
        Returns a status message.
        """
        for student in self.attendance:
            if student["mac"] == mac:
                # Check if this MAC is already recorded
                return f"{name} is already marked present."

        new_record = {
            "name": name,
            "mac": mac,
            "status": "Present"  # <-- Updated from is_present: True
        }
        self.attendance.append(new_record)
        # Add new record to the attendance list
        self.save_attendance()
        # Save updated attendance to file
        return f"{name} marked present successfully."

    def get_present_students(self):
        """
        Returns a list of names of students who are marked present.
        """
        # Gather names where status is 'Present'
        return [student["name"] for student in self.attendance if student.get("status") == "Present"]

    def mark_from_scanner(self, scanned_macs, student_db):
        """
        Automatically marks present students based on scanned MAC addresses.

        scanned_macs: list of MAC addresses detected by scanner
        student_db: list of dictionaries with 'name' and 'mac' keys for all students
        """
        # Loop through all students and mark those whose MAC is in scanned_macs
        for student in student_db:
            if student["mac"] in scanned_macs:
                self.mark_present(student["name"], student["mac"])