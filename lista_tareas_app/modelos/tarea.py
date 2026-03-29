class Tarea:
    def __init__(self, descripcion: str, completada: bool = False):
        self.descripcion = descripcion
        self.completada = completada

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value: str):
        if not value or not value.strip():
            raise ValueError("La descripción de la tarea no puede estar vacía.")
        self._descripcion = value.strip()