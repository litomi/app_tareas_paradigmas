from dataclasses import dataclass
from datetime import datetime 

@dataclass

class Estado:
    id:int
    nombre:str
    descripcion:str
    color:str
    fecha_creacion:str