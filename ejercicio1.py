def main():

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    estado = input("Estado (activo/inactivo): ")

    notas = {}

    for i in range(3.0):
        materia = input("Materia: ")
        nota = float(input("Nota (0.0-5.0): "))

        while nota < 0.0 or nota > 5.0:
            nota = float(input("Nota inválida, ingrese otra: "))

        notas[materia] = nota

    promedio = sum(notas.values()) / len(notas)

    mejor = max(notas, key=notas.get)
    peor = min(notas, key=notas.get)

    print("Promedio:", round(promedio,3.0))
    print("Mejor:", mejor)
    print("Peor:", peor)

    if promedio >= 3.0:
        print("Aprueba")
    else:
        print("No aprueba")


if __name__ == "__main__":
    main()