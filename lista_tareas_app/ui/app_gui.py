import tkinter as tk
from tkinter import messagebox


class TareaApp(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio

        self.title("Mis Tareas Diarias - POO")
        self.geometry("450x550")
        self.configure(bg="#f0f0f0")

        self._crear_componentes()
        self._establecer_eventos()
        self._refrescar_lista()

    def _crear_componentes(self):
        # ... (Mantén tu código anterior de Entry y Botones) ...
        self.label = tk.Label(self, text="Descripción de la Tarea:", bg="#f0f0f0", font=("Arial", 10, "bold"))
        self.label.pack(pady=(20, 0))

        self.entrada_tarea = tk.Entry(self, width=40, font=("Arial", 12))
        self.entrada_tarea.pack(pady=10, padx=20)

        frame_btns = tk.Frame(self, bg="#f0f0f0")
        frame_btns.pack(pady=10)

        tk.Button(frame_btns, text="Añadir Tarea", command=self._handle_agregar, bg="#4CAF50", fg="white",
                  width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btns, text="Completar", command=self._handle_completar, bg="#2196F3", fg="white",
                  width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btns, text="Eliminar", command=self._handle_eliminar, bg="#f44336", fg="white", width=12).pack(
            side=tk.LEFT, padx=5)

        # Listbox con selección mejorada
        self.lista_tareas = tk.Listbox(self, width=50, height=15, font=("Arial", 11, "bold"),
                                       selectmode=tk.SINGLE, activestyle='none')
        self.lista_tareas.pack(pady=10, padx=20)

    def _establecer_eventos(self):
        self.entrada_tarea.bind("<Return>", lambda e: self._handle_agregar())
        self.lista_tareas.bind("<Double-1>", lambda e: self._handle_completar())

    def _handle_agregar(self):
        try:
            desc = self.entrada_tarea.get()
            self.servicio.agregar_tarea(desc)
            self.entrada_tarea.delete(0, tk.END)
            self._refrescar_lista()
        except ValueError as e:
            messagebox.showwarning("Atención", str(e))

    def _handle_completar(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            self.servicio.marcar_completada(seleccion[0])
            self._refrescar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea de la lista.")

    def _handle_eliminar(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            self.servicio.eliminar_tarea(seleccion[0])
            self._refrescar_lista()

    def _refrescar_lista(self):
        """Aquí aplicamos el resaltado verde y el visto"""
        self.lista_tareas.delete(0, tk.END)

        for i, tarea in enumerate(self.servicio.obtener_todas()):
            if tarea.completada:
                # Texto con el Visto (✔)
                texto_mostrar = f" ✔  {tarea.descripcion} [COMPLETADA]"
                self.lista_tareas.insert(tk.END, texto_mostrar)

                # Aplicar colores: Fondo verde claro, letras verdes oscuras
                self.lista_tareas.itemconfig(i, {
                    'bg': '#d4edda',  # Verde suave (estilo Bootstrap success)
                    'fg': '#155724',  # Verde oscuro para el texto
                    'selectbackground': '#c3e6cb'  # Color cuando se selecciona la completada
                })
            else:
                self.lista_tareas.insert(tk.END, f"    {tarea.descripcion}")
                self.lista_tareas.itemconfig(i, {'bg': 'white', 'fg': 'black'})