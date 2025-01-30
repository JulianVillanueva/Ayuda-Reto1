"""
Opcion 1: If anidados

matricula_Fecha = input("Ingrese la fecha de matricula (DD/MM/AAAA): ")

dia, mes, anio = matricula_Fecha.split("/")

if len(dia) == 2 and len(mes) == 2 and len(anio) == 4: # Cantidad exacta de digitos
    if dia.isdigit() and mes.isdigit() and anio.isdigit(): # Validar si por terminal nos entregan NUMEROS
        # Validar rangos de dia mes y año. Evitando numeros negativos y mayores a los estipulados
        if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(anio) <= 2025: 
            print("Fecha valida.")
        else:
            print("Fecha INVALIDA. El dia, mes o año es invalido")
    else:        
        print("Fecha INVALIDA. Los valores de la fecha no son numericos")
else:
    print("fecha INVALIDA. Fuera del rango de las fechas")

print(matricula_Fecha)"""

# Como funciona la funcion .split --------------------

fecha = "20/01/2010" # Le ingresamos por consola la fecha (Sera un texto, gracias a 'input')
listaFecha = fecha.split('/') # Con .split se divide el texto usando como separador los slash '/' en una lista 
print("Asi queda la fecha con .split", listaFecha)
 
# -----------------------------------------------------
 
# Otra opcion posible, en forma de funcion y mas corta 
def validar_fecha(fecha):
    """
    Esta función valida una fecha en el formato DD/MM/AAAA.
    """
    
    # Dividimos los valores de la fecha en: dia, mes y año
    dia, mes, anio = fecha.split("/")

    # Verificamos la longitud de la fecha
    if len(fecha) != 10:
        return "Fecha invalida. Formato incorrecto"

    # Verificamos si los valores de la fecha son numéricos
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        return "Fecha invalida. Los valores de la fecha no son numéricos"

    # Convertimos cada valor de la fecha a enteros
    dia, mes, anio = int(dia), int(mes), int(anio)

    # Verificamos si el día, mes y año están dentro de los rangos válidos
    if not (1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= anio <= 2025):
        return "Fecha invalida. El día, mes o año es incorrecto"

    return "Fecha válida"

# Pedimos al usuario que ingrese la fecha de matrícula
matricula_fecha = input("Ingrese la fecha de matricula (DD/MM/AAAA): ")

# Validamos la fecha y guardamos el resultado
resultado = validar_fecha(matricula_fecha)

print(resultado)