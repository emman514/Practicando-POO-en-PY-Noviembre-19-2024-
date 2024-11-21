print("")#espacio en blanco
print("castruita soto emmanuel 3w 1176")#implime nombre 
print("")#espacio en blanco 
class Estudiante():
    def __init__(self , nombre , nota):
        self.nombre = nombre  # Se asigna el nombre del estudiante al atributo 'nombre'
        self.nota = nota      # Se asigna la calificación del estudiante al atributo 'nota'

    def imprimir(self):
        # Esta función imprime el nombre y la nota del estudiante
        print(f"Nombre:{self.nombre} \nNota: {self.nota}")

    def resultados(self):
        # Esta función determina si el estudiante ha aprobado o reprobado basado en la nota
        if self.nota >= 7:
            print("Has APROBADO!")  # Si la nota es mayor o igual a 7, el estudiante aprueba
        else:
            print("Has REPROBADO!")  # Si la nota es menor a 7, el estudiante reprueba

# Crear una instancia de la clase Estudiante con el nombre "Pedro" y la nota 5
estudiante1 = Estudiante("Pedro", 5)
estudiante1.imprimir()  # Llama al método 'imprimir' para mostrar la información de estudiante1
estudiante1.resultados()  # Llama al método 'resultados' para mostrar si aprobó o reprobó

# Crear una instancia de la clase Estudiante con el nombre "Elizabeth" y la nota 7
estudiante2 = Estudiante("Elizabeth", 7)
estudiante2.imprimir()  # Llama al método 'imprimir' para mostrar la información de estudiante2
estudiante2.resultados()  # Llama al método 'resultados' para mostrar si aprobó o reprobó
