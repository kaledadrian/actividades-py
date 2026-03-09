def main():

    print("1. Número primo")
    print("2. Factorial")
    print("3. Contar vocales")

    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        n = int(input("Ingrese un número: "))
        primo = True

        for i in range(2, n):
            if n % i == 0:
                primo = False

        if primo:
            print("El número es primo")
        else:
            print("El número no es primo")

    elif opcion == 2:
        n = int(input("Ingrese un número: "))
        factorial = 1

        for i in range(1, n+1):
            factorial *= i

        print("El factorial es:", factorial)

    elif opcion == 3:
        texto = input("Ingrese un texto: ").lower()

        for vocal in "aeiou":
            print(vocal, ":", texto.count(vocal))

    else:
        print("Opción inválida")


if __name__ == "__main__":
    main()