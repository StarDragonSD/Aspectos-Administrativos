# recursos.py
class RecursosSistema:
    def __init__(self, memoria_total=8000, cpu_total=100):
        self.memoria_total = memoria_total
        self.cpu_total = cpu_total

        self.memoria_usada = 0
        self.cpu_usado = 0

    def asignar_recursos(self, memoria, cpu):

        if self.memoria_usada + memoria > self.memoria_total:
            return False, "Error: Memoria insuficiente"

        if self.cpu_usado + cpu > self.cpu_total:
            return False, "Error: CPU insuficiente"

        self.memoria_usada += memoria
        self.cpu_usado += cpu

        return True, "Recursos asignados correctamente"

    def ver_estado(self):

        memoria_libre = self.memoria_total - self.memoria_usada
        cpu_libre = self.cpu_total - self.cpu_usado

        return {
            "RAM Total": self.memoria_total,
            "RAM Usada": self.memoria_usada,
            "RAM Libre": memoria_libre,
            "CPU Usado": self.cpu_usado,
            "CPU Libre": cpu_libre
        }