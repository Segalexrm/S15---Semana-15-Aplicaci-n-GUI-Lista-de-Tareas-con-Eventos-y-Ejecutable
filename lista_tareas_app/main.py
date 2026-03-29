from servicios.tarea_servicio import TareaServicio
from ui.app_gui import TareaApp

if __name__ == "__main__":
    # Inyección de dependencias
    servicio = TareaServicio()
    app = TareaApp(servicio)
    app.mainloop()