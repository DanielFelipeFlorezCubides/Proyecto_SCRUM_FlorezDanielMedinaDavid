from usuarios import storage
import re

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

            idNumber = int(input("Please type the id number for this user: "))
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
                storage(idNumber, name, email, role, status)
                print("Info succesfully saved!")
                break
            elif (option == 0):
                print("Operation canceled.")
                break

        except ValueError as e:
            print("\nInvalid option. Please type a number for id a correct email, role or status") 