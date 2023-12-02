from dataclasses import dataclass
from datetime import datetime

# (+)Rol:CLASS
#     (-)id:INT
#     (-)nombre:STRING
#     (-)permisos:PERMISO
#     (-)fechaCreación: DATE
#     (-)activo: BOOLEAN

@dataclass
class Rol:
    id:int
    nombre:str
    permisos:'Permiso'
    fechaCreación:datetime
    activo: bool

@dataclass
class Permiso:  
    id:int
    nombre:str
    descripcion:str
    fechaCreacion:datetime
