from dataclasses import dataclass

@dataclass
class Tarea:
    id:int
    titulo :str
    descripcion:str
    categoria:int #id Categoria
    creada_por:int #id Usuario
    asignada_a:int #id Usuario
    fecha_creacion:str
    fecha_vencimiento:str
    fecha_edicion:str
    estado:int