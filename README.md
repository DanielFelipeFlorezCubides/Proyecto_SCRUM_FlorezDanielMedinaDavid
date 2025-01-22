Desarrollar un sistema de gestión de usuarios que permita a los administradores almacenar, editar, buscar y eliminar información de usuarios de manera organizada y segura.





# **Requerimientos Funcionales**

1. **Agregar Usuario**: Permitir al administrador añadir un nuevo usuario ingresando información como nombre, correo electrónico, rol (administrador, usuario normal) y estado (activo/inactivo).
2. **Editar Usuario**: Buscar un usuario por nombre o correo electrónico y actualizar su información.
3. **Eliminar Usuario**: Buscar y eliminar un usuario de la lista.
4. **Buscar Usuario**: Permitir buscar un usuario por nombre o correo electrónico.
5. **Listar Usuarios**: Mostrar una lista de todos los usuarios registrados.
6. **Autenticación**: Permitir el inicio de sesión con correo electrónico y contraseña.





# **Requerimientos No Funcionales**

1. **Persistencia de Datos**: Guardar la información de los usuarios en un archivo (por ejemplo, CSV o JSON) para que los datos se mantengan después de cerrar la aplicación.
2. **Interfaz de Usuario en Consola**: La interfaz debe ser simple y fácil de navegar, presentando un menú con las opciones principales.
3. **Validación de Datos**: Verificar la entrada de datos para evitar errores como correos duplicados o contraseñas débiles.
4. **Seguridad**: Implementar hashing de contraseñas para almacenar de manera segura las contraseñas de los usuarios.





# **Estructura del Proyecto**

```
gestion_usuarios/
├── app.py         # Archivo principal de ejecución del sistema
├── usuarios.py       # Módulo para la gestión de usuarios (agregar, buscar, editar, eliminar)
├── data/
│ └── usuarios.json    # Archivo JSON para almacenar usuarios
└── utils.py        # Módulo de utilidades para validaciones y formateo de datos
```

# **Implementación de Funcionalidades**

```
--- Sistema de Gestión de Usuarios ---
1. Agregar Usuario
2. Editar Usuario
3. Eliminar Usuario
4. Buscar Usuario
5. Listar Usuarios
6. Iniciar Sesión
7. Salir
Seleccione una opción:
```

# **Backlog**

1. **Agregar Usuario**
2. **Editar Usuario**
3. **Eliminar Usuario**
4. **Buscar Usuario**
5. **Listar Usuarios**
6. **Implementar Autenticación**





# **Historias Técnicas**

1. **Persistencia de Datos**
2. **Validación de Datos**
3. **Interfaz de Menú en Consola**
4. **Manejo de Errores**
5. **Seguridad en el Almacenamiento de Contraseñas**





# **Historias de Usuario Opcionales (Backlog Futuro)**

1. **Exportar Usuarios a CSV**
2. **Importar Usuarios desde CSV**
3. **Recuperación de Contraseña**

# **Tecnologías Recomendadas**

1. Inicio:

- Utiliza Trello para crear historias de usuario a partir del backlog, organizando las tareas con el método Kanban en columnas como **"En Proceso"**, **"En Revisión"** y **"Entregado"**. Realiza un scrumpoker para evaluar las tareas y asignarlas a los miembros del equipo.

1. Backend:

- Python

1. Arquitectura del Proyecto:

- La arquitectura debe seguir la estructura proporcionada en el documento de Estructura del Proyecto.

1. Base de Datos:

- **JSON**: Utiliza JSON para la persistencia de datos.

1. Entregas:

- Entrega el repositorio compartido de GitHub al trainer y sus colaboradores. En la sección "About" del repositorio, incluye el enlace de Trello compartido para su verificación.
- Código funcional para su calificación.

1. GitHub:

- Utiliza GitHub para la gestión de versiones del código durante el desarrollo, aplicando **conventional commits**.