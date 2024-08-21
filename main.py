import os
import json

class Blockchain:
    def __init__(self):
        self.cadena = [self.crear_bloque_genesis()]
        self.dificultad = 4  # Dificultad del Proof of Work

    def crear_bloque_genesis(self):
        return Bloque(0, "Bloque Génesis", time.time(), "0")

    def obtener_ultimo_bloque(self):
        return self.cadena[-1]

    def agregar_bloque(self, nuevas_transacciones):
        ultimo_bloque = self.obtener_ultimo_bloque()
        nuevo_bloque = Bloque(len(self.cadena), nuevas_transacciones, time.time(), ultimo_bloque.hash)
        nuevo_bloque.minar_bloque(self.dificultad)
        self.cadena.append(nuevo_bloque)

    def es_valida(self):
        for i in range(1, len(self.cadena)):
            bloque_actual = self.cadena[i]
            bloque_anterior = self.cadena[i - 1]
            
            if bloque_actual.hash != bloque_actual.calcular_hash():
                return False
            
            if bloque_actual.hash_anterior != bloque_anterior.hash:
                return False
            
        return True

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

