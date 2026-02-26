# Student Attendance Tracker System

A modular Python-based network-driven attendance management system that
automatically marks students present using their device MAC addresses.

Repository: https://github.com/Mwalloh/Student-Attendance-Tracker-System

## Team Members

- Kimberley Madoya
- Ryan Ayunda
- Ratib Khalfah
- Jim Mwalloh

## Project Concept

This system automates attendance by:

1.  Scanning the network
2.  Detecting connected MAC addresses
3.  Comparing them with registered student records
4.  Automatically marking matching students as Present

## Project Structure

├── data │ ├── attendance.json │ └── data.json ├── main.py └── modules
├── attendance.py ├── scanner.py └── student.py

## Module Breakdown

### scanner.py

Responsibility: Network detection

- Works independently without internal project imports
- Scans the network
- Returns a list of connected MAC addresses

### attendance.py

Responsibility: Attendance processing

- Imports student records from data/data.json
- Calls the scanner function
- Compares detected MAC addresses with stored records
- Marks matched students as Present
- Saves results to data/attendance.json

### student.py

Responsibility: Student management (CRUD operations)

Features:

- Create student accounts
- Delete student accounts
- Update student information

Each student record contains:

{ "name": "Student Name", "mac_address": "AA:BB:CC:DD:EE:FF" }

### main.py (Entry Point)

Acts as the CLI controller.

Available options:

- Create student account
- View present students
- Delete student
- Update student data
- Exit the System

## Data Storage Strategy

This project uses JSON for lightweight persistence:

- data.json stores registered students
- attendance.json stores detected present students

This reinforces file-handling fundamentals and modular design.

## Technical Skills Demonstrated

- Modular Python architecture
- Separation of concerns
- JSON serialization and deserialization
- File I/O handling
- CLI application design
- Data comparison algorithms
- Clean project structuring

## System Workflow

1.  Admin registers students (name and MAC address)
2.  Scanner detects connected devices
3.  Attendance module compares data
4.  Matching MAC addresses are marked Present
5.  Results are stored in attendance.json

## How To Run

1.  Clone the repository:

    git clone
    https://github.com/Mwalloh/Student-Attendance-Tracker-System.git

2.  Navigate into the project directory:

    cd Student-Attendance-Tracker-System

3.  Run the program:

    python main.py

## Limitations

- MAC address spoofing is possible
- Works only within the same network
- No authentication system yet
- JSON is not ideal for large-scale production systems

## Future Improvements

- Add SQLite database integration
- Implement admin authentication
- Add logging system
- Improve scanner reliability
- Implement unit testing
- Add a GUI or web interface
- Containerize with Docker

## Learning Outcomes

- Real-world problem modeling
- Modular code organization
- Data persistence without databases
- Collaboration using Git and GitHub
- Designing scalable system structure
