# cli.py
from procesos import GestorProcesos
from recursos import RecursosSistema

gestor = GestorProcesos()
recursos = RecursosSistema()

while True:

    comando = input("\nIngrese un comando: ")

    if comando == "crear_proceso":

        nombre = input("Nombre del proceso: ")
        memoria = int(input("Memoria requerida (MB): "))
        cpu = int(input("CPU requerida (%): "))

        exito, mensaje = recursos.asignar_recursos(memoria, cpu)

        if exito:
            proceso = gestor.crear_proceso(nombre, memoria, cpu)
            print("Proceso creado:")
            print(proceso)
        else:
            print(mensaje)

    elif comando == "listar_procesos":

        procesos = gestor.listar_procesos()

        if not procesos:
            print("No hay procesos activos")
        else:
            for p in procesos:
                print(p)

    elif comando == "ver_memoria":

        estado = recursos.ver_estado()

        print("\nEstado del sistema")
        for clave, valor in estado.items():

            if "RAM" in clave:
                print(f"{clave}: {valor} MB")
            else:
                print(f"{clave}: {valor}%")

    elif comando == "salir":
        print("Saliendo del sistema...")
        break

    else:
        print("Comando no reconocido")