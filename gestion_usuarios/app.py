from usuarios import mainMenu
from agregar import agregar

while True:
    match mainMenu():
        case 1: agregar()
        case _: exit()