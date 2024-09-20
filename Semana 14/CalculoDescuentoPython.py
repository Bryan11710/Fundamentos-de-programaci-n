def calcular_descuento(monto_total, porcentaje_descuento=10):

    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento
# Programa principal
if __name__ == "__main__":

    monto1 = 1000  # Ejemplo de monto total
    descuento1 = calcular_descuento(monto1)
    total_final1 = monto1 - descuento1

    print(f"Monto total: {monto1} $")
    print(f"Monto del descuento (10%): {descuento1:.2f} $")
    print(f"Monto final a pagar: {total_final1:.2f} $\n")


    monto2 = 500
    porcentaje_descuento2 = 20
    descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
    total_final2 = monto2 - descuento2

    print(f"Monto total: {monto2} $")
    print(f"Monto del descuento (20%): {descuento2:.2f} $")
    print(f"Monto final a pagar: {total_final2:.2f} $")
