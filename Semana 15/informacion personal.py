# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Carlos Fernández",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

# Modificar la ciudad
informacion_personal["ciudad"] = "Barcelona"

# Verificar existencia de claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "612-345-678"

# Eliminar una clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
