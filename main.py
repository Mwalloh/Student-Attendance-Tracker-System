# Import scanner_function from modules.scanner.py
# Import 'json'
from json import JSONDecodeError
from modules.scanner import NetworkScanner
from modules.utils import NetworkUtils
import json
from modules.student import StudentManager
from modules.attendance import AttendanceTracker


class Main:
    def __init__(self):
         # Emojis for better UI experience ;)
         print("System Starting...")

         print("\nDetecting network range...")
         self.net_range = NetworkUtils.get_local_network()
         print(self.net_range)

         # self.scanner = NetworkScanner(self.net_range)
         self.tracker = AttendanceTracker()
         self.tracker.mark_present(net_range=self.net_range)

    def main(self):
        print("\n")
        print("\t-------🌍STUDENT ATTENDANCE TRACKER🌍-------")
        print("⭐----------------------⭐WELCOME⭐----------------------⭐")
        # 1. Scanner function is called and runs automatically
        
        print("Choose an option:  ")
        print("1. Create Student Account")
        print("2. View Present Students")
        print("3. Delete Student Account")
        print("4. Update Student Data")
        print("5. Exit")
        option = input("Select an option 1 - 5: ")

        # OPTION 1
        if option == "1":
            print("\n")
            print("\t----------- 🎒CREATE ACCOUNT FOR STUDENT🎒 -------------")
        
            # Name Input
            while True:
                name = input("Enter student name: ").strip()
                if not name:
                    print("❌ Name cannot be empty. 🤦")
                    
                elif len(name) < 5:
                    print("❌ Name cannot be less than 5 characters. ❌")
                    
                elif len(name) > 30:
                    print("❌ Name cannot be more than 30 characters. ❌")
                    
                else :
                    break
                
            # MAC ADDRESS INPUT
            while True:
                mac_address = input("Enter student mac address: ").strip()
                if not mac_address:
                    print("🤦 MAC address cannot be empty. ❌")
                
                elif len(mac_address) < 15:
                    print("MAC Address cannot be less than 10 characters.")
                    
                else :
                    break
        
            # Parse the data & mac-address to the 'create_account_function'
            student = StudentManager()
            student.create_student(name, mac_address)
            self.main()

        # OPTION 2
        elif option == "2":
            try :
                print("\n")
                print("✅----------------PRESENT STUDENTS-----------------✅")
                with open("data/attendance.json", "r") as file:
                    data = json.load(file)
                    if not data:
                        print(f"No students found.")
                    else:
                        for person in data:
                                print(f"📌 {person['name']} - {person['status']}")
                self.main()
                        # else:
                        #      print("😱 Students absent. 😱")
                        #      self.main()
            except:
                print("File not found.")
                self.main()


        # OPTION 3
        elif option == "3":
            print("\n")
            print("🚮-------------------- 🚮DELETE STUDENT🚮 ---------------------------🚮")
            while True:
                # Name Input
                name = input("Enter student's name: ").strip()
                if not name:
                    print("🤦 Name cannot be empty. ❌")
                    
                elif len(name) < 5:
                    print("❌ Name cannot be less than 5 characters. ❌")
                    
                elif len(name) > 30:
                    print("❌ Name cannot be more than 30 characters. ❌")
                    
                else:
                    break
            
            while True:
                # Mac Address Input
                mac_address = input("Enter student's MAC address: ").strip()
                if len(mac_address) < 10:
                    print("MAC Address cannot be less than 10 characters.")
                else:
                    break
            
        
            # Parse the name and mac address to the delete_student function
            student = StudentManager()
            student.delete_student(name, mac_address)
            self.main()
            
        # OPTION 4
        elif option == "4":
            print("\n")
            print("------------------- 🗃UPDATE STUDENT DATA🗄 --------------------")
            print("What would you like to update? ")
            print("\t1. Name")
            print("\t2. MAC Address")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                while True:
                    # Name Input
                    current_name = input("\tEnter current student's name: ").strip()
                    if not current_name:
                        print("🤦 Name cannot be empty. ❌")
                    elif len(current_name) < 5:
                        print("❌ Name cannot be less than 5 characters. ❌")
                    elif len(current_name) > 30:
                        print("❌ Name cannot be more than 30 characters. ❌")
                    
                    else:
                        break
                
                while True:
                    # New Name Input
                    new_name = input("\tEnter new name for the student: ").strip()
                    if not new_name:
                        print("🤦 Name cannot be empty. ❌")
                    elif len(new_name) < 5:
                        print("❌ Name cannot be less than 5 characters. ❌")
                    elif len(new_name) > 30:
                        print("❌ Name cannot be more than 30 characters. ❌")
                    
                    else:
                        break
                    
                # Parse the current name and new name to the update_student fn
                student = StudentManager()
                student.update_student(current_name=current_name, new_name=new_name)
                
            elif choice == "2":
                while True:
                    # Name Input
                    current_name = input("\tEnter current student's name: ").strip()
                    if not current_name:
                        print("🤦 Name cannot be empty. ❌")
                    elif len(current_name) < 5:
                        print("❌ Name cannot be less than 5 characters. ❌")
                    elif len(current_name) > 30:
                        print("❌ Name cannot be more than 30 characters. ❌")
                    
                    else:
                        break
                    
                while True:
                    # Mac Address Input
                    new_mac = input("\tEnter new MAC Address: ").strip()
                    if len(new_mac) < 10:
                        print("❌ MAC Address cannot be less than 10 characters. ❌")
                        
                    else:
                        break
                   
                # Parse the current name and new mac address to the update_student function
                student = StudentManager()
                student.update_student(current_name=current_name, new_mac=new_mac)
                 
            else:
                print("❌ Invalid option. ❌")
                self.main()
                
            
            
            self.main()
            
        elif option == "5":
            print("\n")
            print("~~~~~~~~~~~~~~~~~ 👋 BYE! WELCOME BACK AGAIN 👋 ~~~~~~~~~~~~~~~~~~~~~~~~")
            return
    
        else :
            print("❌ Invalid option. ❌")
            self.main()

if __name__ == "__main__":
    Main().main()