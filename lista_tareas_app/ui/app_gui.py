import tkinter as tk
from tkinter import messagebox, ttk


class TareaApp(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio

        self.title("Mis Tareas Diarias - POO")
        self.geometry("450x500")
        self.configure(bg="#f0f0f0")

        self._crear_componentes()
        self._establecer_eventos()
        self._refrescar_lista()

    def _crear_componentes(self):
        # Campo de entrada
        self.label = tk.Label(self, text="Nueva Tarea:", bg="#f0f0f0", font=("Arial", 10, "bold"))
        self.label.pack(pady=(20, 0))

        self.entrada_tarea = tk.Entry(self, width=40, font=("Arial", 12))
        self.entrada_tarea.pack(pady=10, padx=20)
        self.entrada_tarea.focus()

        # Botones
        frame_botones = tk.Frame(self, bg="#f0f0f0")
        frame_botones.pack(pady=10)

        self.btn_add = tk.Button(frame_botones, text="Añadir", command=self._handle_agregar, bg="#4CAF50", fg="white")
        self.btn_add.pack(side=tk.LEFT, padx=5)

        self.btn_done = tk.Button(frame_botones, text="Completar", command=self._handle_completar, bg="#2196F3",
                                  fg="white")
        self.btn_done.pack(side=tk.LEFT, padx=5)

        self.btn_del = tk.Button(frame_botones, text="Eliminar", command=self._handle_eliminar, bg="#f44336",
                                 fg="white")
        self.btn_del.pack(side=tk.LEFT, padx=5)

        # Lista de tareas (Listbox)
        self.lista_tareas = tk.Listbox(self, width=50, height=15, font=("Arial", 11), selectmode=tk.SINGLE)
        self.lista_tareas.pack(pady=10, padx=20)

    def _establecer_eventos(self):
        # EVENTO DE TECLADO: Enter para añadir
        self.entrada_tarea.bind("<Return>", lambda event: self._handle_agregar())

        # EVENTO DE RATÓN: Doble clic para completar
        self.lista_tareas.bind("<Double-1>", lambda event: self._handle_completar())

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
            indice = seleccion[0]
            self.servicio.marcar_completada(indice)
            self._refrescar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea primero.")

    def _handle_eliminar(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.servicio.eliminar_tarea(indice)
            self._refrescar_lista()

    def _refrescar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.servicio.obtener_todas():
            texto = f"{tarea.descripcion} {'[Hecho]' if tarea.completada else ''}"
            self.lista_tareas.insert(tk.END, texto)

            # Feedback visual: Color gris si está completada
            if tarea.completada:
                self.lista_tareas.itemconfig(tk.END, {'fg': 'gray'})