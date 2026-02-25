import json
import os

# File path where attendance data is stored
ATTENDANCE_FILE = "data/attendance.json"


def load_attendance():
    """
    Loads attendance records from the JSON file.
    Returns an empty list if the file does not exist or is empty.
    """
    # Check if the attendance file exists
    if not os.path.exists(ATTENDANCE_FILE):
        # Return empty list if file is missing
        return []
    
    # Open the file in read mode
    with open(ATTENDANCE_FILE, "r") as file:
        # Load JSON data and return it as a Python list
        return json.load(file)


def save_attendance(data):
    """
    Saves the attendance records to the JSON file.
    """
    # Open the file in write mode
    with open(ATTENDANCE_FILE, "w") as file:
        # Convert Python list/dict to JSON and save
        json.dump(data, file, indent=4)


def mark_present(name, mac):
    # Load existing attendance data
    attendance = load_attendance()

    # Loop through existing records to check for duplicates
    for student in attendance:
        if student["mac"] == mac:
            # Return message if student is already marked present
            return "Student already marked present."

    # Create a new attendance record
    new_record = {
        "name": name,
        "mac": mac,
        "is_present": True
    }

    # Add the new record to the list
    attendance.append(new_record)

    # Save updated attendance data
    save_attendance(attendance)

    # Return confirmation message
    return "Student marked present successfully."


def get_present_students():
    """
    Returns a list of names of students who are marked present.
    """
    # Load attendance data
    attendance = load_attendance()

    # Initialize list for present students
    present_students = []

    # Loops through each record and check if the student is present
    for student in attendance:
        if student.get("is_present") == True:
            # Add student name to present list
            present_students.append(student["name"])

    # Return the list of present students
    return present_students