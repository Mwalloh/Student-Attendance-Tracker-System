# 🎓 Student Attendance Tracker

### Automated Network-Based Presence Detection

Stop taking manual roll calls. This system automatically marks students
**"Present"** by scanning the local network for their device's unique
**MAC Address**.

------------------------------------------------------------------------

## 🌟 Key Features

-   📡 **ARP Network Scanning** -- High-speed device discovery using
    Scapy.\
-   👤 **Student CRUD** -- Full management of student profiles (Create,
    Read, Update, Delete).\
-   🔍 **Auto-Network Discovery** -- Automatically detects your IP range
    and subnet mask.\
-   📂 **Data Persistence** -- Uses structured JSON for easy data
    portability.\
-   🖥️ **Interactive CLI** -- A user-friendly emoji-driven command-line
    interface.

------------------------------------------------------------------------

## 📂 Project Architecture

``` bash
.
├── main.py                # 🚀 Application Entry Point
├── data/                  # 🗄️ Database Folder
│   ├── attendance.json    # ✅ Latest Scan Results
│   └── data.json          # 👥 Registered Student Database
└── modules/               # ⚙️ Core Logic
    ├── attendance.py      # Logic for marking presence
    ├── scanner.py         # ARP Packet scanning engine
    ├── student.py         # Student record management
    └── utils.py           # Network interface utilities
```

------------------------------------------------------------------------

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

``` bash
https://github.com/Mwalloh/Student-Attendance-Tracker-System
cd attendance-tracker
```

### 2️⃣ Install Dependencies

This project requires **scapy** for packet manipulation and
**netifaces** for network detection.

``` bash
pip install scapy netifaces
```

------------------------------------------------------------------------

## ⚡ How to Run

> ⚠️ **Root Privileges Required**\
> Since the program performs raw network scans (ARP), it must be
> executed with sudo.

``` bash
sudo python3 main.py
```

------------------------------------------------------------------------

## 📖 System Workflow

  ------------------------------------------------------------------------
  Step            Action                    Description
  --------------- ------------------------- ------------------------------
  1️⃣              Scan                      The system identifies your
                                            local network (e.g.,
                                            192.168.1.0/24).

  2️⃣              Detect                    It sends ARP requests to find
                                            all active MAC addresses.

  3️⃣              Compare                   It matches discovered MACs
                                            against your student database.

  4️⃣              Log                       Matches are written to
                                            `attendance.json` with a
                                            "Present" status.
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## 🎨 Preview

``` plaintext
-------🌍 STUDENT ATTENDANCE TRACKER 🌍-------
⭐----------------------⭐ WELCOME ⭐----------------------⭐

Choose an option:
1. Create Student Account
2. View Present Students
3. Delete Student Account
4. Update Student Data
5. Exit
```

