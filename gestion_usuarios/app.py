from usuarios import mainMenu
from agregar import agregar
from editar import editar

while True:
    match mainMenu():
        case 1: agregar()
        case 2: editar()
        case _: exit()