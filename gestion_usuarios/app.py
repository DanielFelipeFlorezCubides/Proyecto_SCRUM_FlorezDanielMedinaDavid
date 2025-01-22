from gestion_usuarios.usuarios import mainMenu
from gestion_usuarios.usuarios import agregar

while True:
    match mainMenu():
        case 1: agregar()
        case _: exit()