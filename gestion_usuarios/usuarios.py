import json
import os

def read_file(path):
        with open(f'gestion_usuarios/data/{path}', 'r') as file:
            data = file.read()
            convertList = json.loads(data)
            return convertList
    
def write_file(data, path):
    with open(f'gestion_usuarios/data/{path}', 'w') as file:
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

def storage(idNumber, name, email, role, status):
    data = read_file('usuarios.json')
    formato = {
         "ID": idNumber,
        "Name": name,
        "Email": email,
        "Role": role,
        "Status": status
    }
    data.append(formato)
    write_file(data, 'usuarios.json')
    return data