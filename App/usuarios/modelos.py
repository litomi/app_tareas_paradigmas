from dataclasses import dataclass
from datetime import datetime

@dataclass
class Usuario:
    id:int
    nombreCompleto:str
    email:str
    password:str
    activo:str
    rol:str
    fechaCreación:str
