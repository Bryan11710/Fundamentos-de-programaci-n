# Escritura de Archivo de Texto

# Crea un nuevo archivo llamado my_notes.txt
with open('my_notes.txt', 'w') as file:  # Abre el archivo en modo escritura
    # Escribe al menos tres líneas de notas personales en el archivo
    file.write("Nota 1: Recoger la ropa de la lavandería.\n")  # Primera nota
    file.write("Nota 2: Comprar ingredientes para la cena.\n")  # Segunda nota
    file.write("Nota 3: Llamar a mamá.\n")  # Tercera nota

# Lectura de Archivo de Texto

# Abre el archivo my_notes.txt
with open('my_notes.txt', 'r') as file:  # Abre el archivo en modo lectura
    # Lee el contenido del archivo línea por línea
    for line in file:  # Itera sobre cada línea del archivo
        print(line.strip())  # Muestra cada línea leída en la consola, eliminando espacios en blanco


# El archivo se cierra automáticamente al salir del bloque 'with'
