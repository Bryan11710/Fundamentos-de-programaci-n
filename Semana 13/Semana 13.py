def obtener_temperaturas(ciudad):

    temperaturas = {
        'Oslo': [5.2, 7.1, 6.5],
        'Bergen': [8.0, 9.3, 7.9],
        'Stavanger': [6.8, 7.2, 6.9]
    }
    return temperaturas.get(ciudad, [None, None, None])


def main():
    ciudades_noruega = ['Oslo', 'Bergen', 'Stavanger']

    # Seleccionar ciudad
    print("Seleccione una ciudad de Noruega:")
    for i, ciudad in enumerate(ciudades_noruega, 1):
        print(f"{i}. {ciudad}")

    opcion = int(input("Ingrese el número de la ciudad: "))

    if 1 <= opcion <= len(ciudades_noruega):
        ciudad_seleccionada = ciudades_noruega[opcion - 1]
        print(f"Ha seleccionado: {ciudad_seleccionada}")

        # Obtener y mostrar temperaturas
        temperaturas = obtener_temperaturas(ciudad_seleccionada)
        print("\nTemperaturas para las semanas 1, 2 y 3:")
        print(f"Semana 1: {temperaturas[0]} °C")
        print(f"Semana 2: {temperaturas[1]} °C")
        print(f"Semana 3: {temperaturas[2]} °C")
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()

