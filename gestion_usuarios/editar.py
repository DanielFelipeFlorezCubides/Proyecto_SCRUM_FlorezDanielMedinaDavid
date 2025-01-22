from usuarios import read_file, write_file

def editar():
    while True:
        try:
            print("""
    ---------------------------------------------------
                    EDIT AN USER INFO
    ---------------------------------------------------
    """)
            roleOptions= ["admin", "user"]
            statusOptions= ["active", "inactive"]

            idNumber = int(input("Please type the id to update: "))
            data = read_file('usuarios.json')
            for diccionario in data:
                if diccionario['ID'] == idNumber:
                    diccionario['Name'] = input('Please type the new name: ')
                    diccionario['Email'] = input("Please type the new email: ")
                    diccionario['Role'] = input("Please type the new role(Admin / user): ")
                    diccionario['Status'] = input("Please type the new status(Active / Inactive): ")
            
            option = int(input("Type '1' to update or '0' to cancel: "))
            if (option == 1):
                write_file(data, 'usuarios.json')
                print("Info succesfully updated!")
                break
            elif (option == 0):
                print("Operation canceled.")
                break
            
        except ValueError as e:
            print("\nInvalid option. Please type a correct email, role or status") 