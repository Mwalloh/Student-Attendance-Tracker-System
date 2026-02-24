# Import scanner_function from modules.scanner.py
# Import 'json'
import json
class Main:
    def __init__(self):
        pass
    
    def main(self):
        print("\n")
        print("⭐----------------------⭐WELCOME⭐----------------------⭐")
        # 1. Scanner function is called and runs automatically
        
        print("Choose an option:  ")
        print("1. Create Student Account")
        print("2. View Present Students")
        print("3. Delete Student Account")
        print("4. Update Student Data")
        print("5. Exit")
        option = input("Select an option 1 - 5: ")
    
        if option == "1":
            print("\n")
            print("\t----------- 🎒CREATE ACCOUNT FOR STUDENT🎒 -------------")
        
            # NAME INPUT
            name = input("Enter student name: ").strip()
            if not name:
                print("❌ Name cannot be empty. ❌")
                name = input("Enter student name: ").strip()
            if len(name) < 10:
                print("❌ Name cannot be less than 3 characters. ❌")
                name = input("Enter student name: ").strip()
            if len(name) > 20:
                print("❌ Name cannot be more than 20 characters. ❌")
                name = input("Enter student name: ").strip()
            
            # MAC ADDRESS 
            mac_address = input("Enter student mac address: ").strip()
            if len(mac_address) < 10:
                print("MAC Address cannot be less than 10 characters.")
                mac_address = input("Enter student's MAC address: ").strip()
        
            # Parse the data & mac-address to the the 'create_account_function'
        
            print(f"🎉 Student Account for {name} has been created successfully. 🎉")
            self.main()
    
        elif option == "2":
            try :
                print("\t")
                print("✅----------------PRESENT STUDENTS-----------------✅")
                with open("data/attendance.json", "r") as file:
                    data = json.load(file)
                    for person in data:
                        if person['is_present'] == True:
                            print(person['name'])
                        else:
                            print("An error occurred.")
                
            except:
                print("An exception occurred.")
                self.main()
    
        elif option == "3":
            print("\n")
            print("--------------------DELETE STUDENT---------------------------")
            name = input("Enter student's name: ").strip()
            if not name:
                print("❌ Name cannot be empty. ❌")
                name = input("Enter student's name: ").strip()
            if len(name) < 3:
                print("❌ Name cannot be less than 3 characters. ❌")
                name = input("Enter student's name: ").strip()
            if len(name) > 20:
                print("❌ Name cannot be more than 20 characters. ❌")
                name = input("Enter student's name: ").strip()
            
            mac_address = input("Enter student's MAC address: ").strip()
            if len(mac_address) < 10:
                print("MAC Address cannot be less than 10 characters.")
                mac_address = input("Enter student's MAC address: ").strip()
            
        
            # Parse the data to the delete_student function
            print("Student deleted successfully.")
            self.main()
        elif option == "4":
            print("\n")
            print("-------------------UPDATE STUDENT DATA--------------------")
        
            name = input("Enter student's name: ").strip()
            if not name:
                print("❌ Name cannot be empty. ❌")
                name = input("Enter student's name: ").strip()
            if len(name) < 3:
                print("❌ Name cannot be less than 3 characters. ❌")
                name = input("Enter student's name: ").strip()
            if len(name) > 20:
                print("❌ Name cannot be more than 20 characters. ❌")
                name = input("Enter student's name: ").strip()
    
            self.main()
        elif option == "5":
            return
    
        else :
            print("❌ Invalid option. ❌")

__main__ = Main()
__main__.main()