import json
import re
import os

def read_file(path):
        with open(f'data/{path}', 'r') as file:
            data = file.read()
            convertList = json.loads(data)
            return convertList
    
def write_file(data, path):
    with open(f'data/{path}', 'w') as file:
        convertJson = json.dumps(data, indent=4)
        file.write(convertJson)
        file.close()

def mainMenu():
    while True:
        try:
            print('''
    =============================================
                USERS MANAGEMENT SYSTEM
    =============================================
    Options to choose from:

    1. Add user
    2. Edit an user
    3. Delete an user
    4. Search for a user
    5. User's list
    6. Log in
    7. Exit
    =============================================
            ''')
            options = int(input('Please choose an option(1-7): '))
            if (options >= 1 and options <= 6):
                return options
            elif options == 7:
                    decission = int(input('Are you sure you want to leave?(1 = yes, 0 = no): '))
                    if decission == 1:
                        print(''' 
    ============================================
    Thank you for using users management system!
    ============================================
                              ''')
                        break
                    elif decission == 0:
                        print('ok')
                        os.system('clear')
            else: raise ValueError()
        
        except ValueError as e:
            print("Invalid option. Please choose a number between 1 and 7.")

def agregar():
    while True:
        try:
            print("""
    ---------------------------------------------------
                    ADD A NEW USER
    ---------------------------------------------------
    """)    
            roleOptions= ["admin", "user"]
            statusOptions= ["active", "inactive"]

            name = input("Please type your name: ")
            email = input("Please type your email: ")
            role = input("Please type your role(Admin / User): ").lower()
            status = input("Please type the (admin / user) status (Active / Inactive): ").lower()

            regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
            
            if re.match(regex, email):
                pass
            else:
                raise ValueError()
            
            if role in roleOptions:
                pass
            else:
                raise ValueError()
            
            if status in statusOptions:
                pass
            else:
                raise ValueError()
            
            option = int(input("Type '1' to save or '0' to cancel: "))
            if (option == 1):
                storage(name, email, role, status)
                print("Info succesfully saved!")
                break
            elif (option == 0):
                print("Operation canceled.")
                break

        except ValueError as e:
            print("\nInvalid option. Please type a correct email, role or status") 

def storage(name, email, role, status):
    data = read_file('usuarios.json')
    formato = {
        "Name": name,
        "Email": email,
        "Role": role,
        "Status": status
    }
    data.append(formato)
    write_file(data, 'usuarios.json')
    return data