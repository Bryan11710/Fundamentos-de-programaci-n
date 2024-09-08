
ciudades = ['Ciudad1', 'Ciudad2', 'Ciudad3']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 3


np.random.seed(0)
temperaturas = np.random.randint(15, 35, size=(len(ciudades), len(dias_semana), semanas))


promedios = {}


for i, ciudad in enumerate(ciudades):
    promedios[ciudad] = []
    for semana in range(semanas):
        promedio_semana = np.mean(temperaturas[i, :, semana])
        promedios[ciudad].append(promedio_semana)


for ciudad, promedios_semanas in promedios.items():
    print(f"{ciudad}:")
    for semana, promedio in enumerate(promedios_semanas, start=1):
        print(f"  Semana {semana}: {promedio:.2f}°C")
