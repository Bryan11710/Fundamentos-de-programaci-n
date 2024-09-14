def obtener_promedio_temperaturas(ciudades_datos):


    # Diccionario donde almacenaremos el promedio de cada ciudad
    promedio_ciudades = {}

    # Iteramos por cada ciudad y sus respectivas temperaturas semanales
    for ciudad, semanas in ciudades_datos.items():
        # 'ciudad' representa el nombre de la ciudad, 'semanas' es una lista con las temperaturas semanales

        # Convertimos las listas de temperaturas semanales en una sola lista con todas las temperaturas
        temperaturas_totales = [temp for semana in semanas for temp in semana]

        # Calculamos el promedio dividiendo la suma total de las temperaturas por la cantidad de datos
        promedio = sum(temperaturas_totales) / len(temperaturas_totales)

        # Guardamos el promedio en el diccionario 'promedio_ciudades'
        promedio_ciudades[ciudad] = promedio

    # Retornamos el diccionario con los promedios de cada ciudad
    return promedio_ciudades


# Ejemplo de uso:
datos_ciudades = {
    "CiudadA": [[25, 27, 26], [24, 26, 28], [27, 29, 30], [25, 24, 26]],
    "CiudadB": [[18, 20, 19], [17, 18, 21], [19, 20, 22], [18, 19, 20]],
    "CiudadC": [[30, 32, 31], [29, 31, 33], [31, 32, 34], [30, 29, 31]]
}

# Llamada a la función para calcular los promedios
promedios = obtener_promedio_temperaturas(datos_ciudades)

# Mostramos el resultado para cada ciudad
for ciudad, promedio in promedios.items():
    # Formateamos para que solo se muestren dos decimales
    print(f"El promedio de temperatura en {ciudad} es {promedio:.2f}°C")

