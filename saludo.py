def saludar(nombre="mundo"):
    return f"¡Hola, {nombre}!"


if __name__ == "__main__":
    nombre = input("¿Cómo te llamás? ")
    print(saludar(nombre or "mundo"))
