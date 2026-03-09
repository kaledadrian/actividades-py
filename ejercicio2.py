def main():

    valor = float(input("Ingrese el valor: "))

    impuesto = valor * 0.19

    if valor >= 200000:
        descuento = valor * 0.10
    else:
        descuento = 0

    total = valor + impuesto - descuento

    print("Impuesto:", impuesto)
    print("Descuento:", descuento)
    print("Total final:", total)


if __name__ == "__main__":
    main()