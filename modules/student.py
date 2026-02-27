import json
import os

#StudentManager defines the blueprint for management object
#Initializes the manager with a specific file path
class StudentManager:
    #runs the moment an instance is created and data is stored in the data.json so all files search there
    def __init__(self, data_path='data/data.json'):
        self.data_path = data_path 

#------------->Load Data From JSON File
#Internal helper to load student data
    def load_data(self):
        #checks if data.json exists if it doesn't create an empty list
        if not os.path.exists(self.data_path): 
            return []
        try: 
            #open and close the file safely
            with open(self.data_path, 'r') as f:
                #convert given text to JSON file into a list of dicts
                return json.load(f)
            #In case of any corruption in the file return an empty list
        except (json.JSONDecodeError, FileNotFoundError):
            return []
        
#----------->Save data
    def save_data(self, data):
        # Ensure the 'data' directory exists before saving to prevent FileNotFoundError
        os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
        #Possible error overwriting everything
        with open(self.data_path, 'w') as f:
            #Converts the list into JSON text
            json.dump(data, f, indent=4)

#--------->Create student acc
    def create_student(self, name, mac_address):
        #get current list of students
        students = self.load_data()
        #forces MAC addresses to lowercase
        mac_lower = mac_address.lower()
         
        #Loop to check the MAC addresses existence
        if any(student['mac_address'] == mac_lower for student in students):
            #use of any to return True if a value within the object comes as true
            print("❌ Error: MAC Address already Exists ❌")
            return
        
        #appending by adding the name and mac address to the list as a dict
        students.append({"name": name, "mac_address": mac_lower})
        self.save_data(students) 
        print(f"🎉 Student {name} added successfully. 🎊")
        return
    
#----------->Delete student
    def delete_student(self, name, mac_address):
        #get current list of students
        students = self.load_data()
        #forces MAC addresses to lowercase
        mac_lower = mac_address.lower()
        name_lower = name.lower()

        #List comprehension to create a new list excluding the specific student
        updated_list = [s for s in students if not (s['name'].lower() == name_lower and s['mac_address'].lower() == mac_lower)]

        #Check if the list size changed to verify deletion
        if len(updated_list) == len(students):
            print("😡 Student Not Found. 👀")
            return
        
        #Save the updated list back to JSON
        self.save_data(updated_list)
        print(f"😰 Student {name.capitalize()} removed successfully :) 😁") 
        return
    
#----------->Update student data
    def update_student(self, current_name, new_name=None, new_mac=None):
        #get current list of students
        students = self.load_data()
        found = False

        #Loop through the students to find the match by name
        for student in students:
            if student['name'].lower() == current_name.lower():
                #If a new name or mac is provided, update the specific field
                if new_name: student['name'] = new_name
                if new_mac: student['mac_address'] = new_mac.lower()
                found = True
                break
        
        #If found, save changes; otherwise return error
        if found:
            self.save_data(students)
            print(f"🤯 Student {current_name.capitalize()} updated successfully. 😇")
            return
        
        print("😞 Student not Found. 💔") 
        return
    


#manager = student_manager()
#print(manager.create_student("Luna", "AA:BB:CC:11:22:33"))
#print(manager.update_student("Luna", new_name="Luna Lovegood"))
#print(manager.delete_student("Luna Lovegood", "AA:BB:CC:11:22:33"))