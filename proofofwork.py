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
