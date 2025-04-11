def obtener_temperaturas():
    """Solicita al usuario ingresar las temperaturas diarias una por una."""
    temperaturas = []
    print("Ingrese las temperaturas diarias (7 días):")
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Día {i + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas

def calcular_promedio(lista):
    """Calcula y retorna el promedio de una lista de temperaturas."""
    return sum(lista) / len(lista)

def encontrar_max_min(lista):
    """Encuentra y retorna la temperatura máxima, mínima y sus días correspondientes."""
    temp_max = max(lista)
    dia_max = lista.index(temp_max) + 1
    temp_min = min(lista)
    dia_min = lista.index(temp_min) + 1
    return temp_max, dia_max, temp_min, dia_min

def mostrar_alertas(lista):
    """Genera alertas si hay temperaturas extremas (mayores a 40°C o menores a 0°C)."""
    alertas = []
    for i, temp in enumerate(lista):
        if temp > 40:
            alertas.append(f"Día {i + 1}: Temperatura extrema alta ({temp}°C)")
        elif temp < 0:
            alertas.append(f"Día {i + 1}: Temperatura extrema baja ({temp}°C)")
    return alertas

def analizar_temperaturas():
    """Analiza las temperaturas ingresadas y muestra los resultados."""
    temperaturas = obtener_temperaturas()
    promedio = calcular_promedio(temperaturas)
    temp_max, dia_max, temp_min, dia_min = encontrar_max_min(temperaturas)
    dias_sobre_promedio = [i + 1 for i, temp in enumerate(temperaturas) if temp > promedio]
    alertas = mostrar_alertas(temperaturas)

    print(f"Temperatura máxima: {temp_max}°C (Día {dia_max})")
    print(f"Temperatura mínima: {temp_min}°C (Día {dia_min})")
    print(f"Promedio semanal: {promedio:.2f}°C")
    print(f"Días con temperatura por encima del promedio: {dias_sobre_promedio}")
    if alertas:
        print("Alertas de temperaturas extremas:")
        for alerta in alertas:
            print(alerta)
    else:
        print("No hubo temperaturas extremas.")

analizar_temperaturas()