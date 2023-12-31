from dataclasses import dataclass
from datetime import datetime

@dataclass
class Usuario:
    id:int
    nombre:str
    descripcion:str
    color:str
    fechaCreación:datetime