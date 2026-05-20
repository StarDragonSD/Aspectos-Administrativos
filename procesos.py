# procesos.py
class Proceso:
    contador_id = 1

    def __init__(self, nombre, memoria, cpu):
        self.id = Proceso.contador_id
        Proceso.contador_id += 1

        self.nombre = nombre
        self.memoria = memoria
        self.cpu = cpu
        self.estado = "Listo"

    def __str__(self):
        return f"[{self.id}] {self.nombre} | RAM: {self.memoria}MB | CPU: {self.cpu}% | Estado: {self.estado}"


class GestorProcesos:
    def __init__(self):
        self.procesos = []

    def crear_proceso(self, nombre, memoria, cpu):
        proceso = Proceso(nombre, memoria, cpu)
        self.procesos.append(proceso)
        return proceso

    def listar_procesos(self):
        return self.procesos