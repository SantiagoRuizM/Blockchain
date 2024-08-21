import os
import json

class Tarea:
    def __init__(self, nombre, completada=False):
        self.nombre = nombre
        self.completada = completada

    def __str__(self):
        estado = "✔️" if self.completada else "❌"
        return f"{estado} {self.nombre}"

class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        self.tareas = []
        self.archivo = archivo
        self.cargar_tareas()

    def agregar_tarea(self, nombre):
        nueva_tarea = Tarea(nombre)
        self.tareas.append(nueva_tarea)
        print(f"Tarea '{nombre}' agregada.")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            tarea_eliminada = self.tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada.nombre}' eliminada.")
        else:
            print("Índice inválido.")

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
            print(f"Tarea '{self.tareas[indice].nombre}' marcada como completada.")
        else:
            print("Índice inválido.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i}. {tarea}")

    def guardar_tareas(self):
        with open(self.archivo, "w") as file:
            json.dump([tarea.__dict__ for tarea in self.tareas], file)
        print("Tareas guardadas en el archivo.")

    def cargar_tareas(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as file:
                tareas_cargadas = json.load(file)
                self.tareas = [Tarea(**tarea) for tarea in tareas_cargadas]
                print("Tareas cargadas desde el archivo.")
        else:
            print("No se encontró un archivo de tareas previo.") 

