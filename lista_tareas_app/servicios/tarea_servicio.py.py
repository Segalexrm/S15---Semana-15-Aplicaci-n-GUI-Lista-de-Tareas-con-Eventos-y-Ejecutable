from modelos.tarea import Tarea
from typing import List

class TareaServicio:
    def __init__(self):
        # Simulamos una base de datos en memoria
        self._tareas: List[Tarea] = []

    def agregar_tarea(self, descripcion: str):
        nueva_tarea = Tarea(descripcion)
        self._tareas.append(nueva_tarea)
        return nueva_tarea

    def obtener_todas(self) -> List[Tarea]:
        return self._tareas

    def eliminar_tarea(self, indice: int):
        if 0 <= indice < len(self._tareas):
            self._tareas.pop(indice)
        else:
            raise IndexError("La tarea seleccionada no existe.")

    def marcar_completada(self, indice: int):
        if 0 <= indice < len(self._tareas):
            self._tareas[indice].completada = True
        else:
            raise IndexError("La tarea seleccionada no existe.")