from datetime import datetime

# Función para calcular la edad
def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    edad = hoy.year - fecha_nacimiento.year
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return edad

# Función para obtener la primera consonante de un nombre
def primera_consonante(nombre):
    consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
    for letra in nombre:
        if letra in consonantes:
            return letra.upper()
    return ''  # En caso de no encontrar consonantes

# Función para obtener la suma ASCII de las letras de una palabra
def suma_ascii(palabra):
    return sum(ord(c) for c in palabra if c.isalpha())

# Función para obtener la posición de una letra en el alfabeto
def posicion_alfabeto(letra):
    letra = letra.lower()
    if letra.isalpha():
        return ord(letra) - ord('a') + 1
    return 0

# Solicitar datos al usuario
nombre = input("Introduce tu nombre: ")
ape1 = input("Introduce tu primer apellido: ")
ape2 = input("Introduce tu segundo apellido: ")
nia = input("Introduce tu NIA o DNI: ")
fecha_str = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
fecha_nac = datetime.strptime(fecha_str, "%d/%m/%Y")

# Solicitar mínimo 5 aficiones
aficiones = []
print("Introduce al menos 5 aficiones:")
while len(aficiones) < 5:
    aficion = input(f"Afición #{len(aficiones)+1}: ")
    if aficion.strip():
        aficiones.append(aficion.strip())

edad = calcular_edad(fecha_nac)
dia_actual = datetime.today().day

# Parte de la contraseña
binario_letras_ape1 = bin(len(ape1))[2:]  # Número de letras en binario
if dia_actual % 2 == 0:
    parte2 = primera_consonante(nombre)
else:
    parte2 = str(suma_ascii(ape1))
parte3 = str(posicion_alfabeto(nombre.split()[0][-1]))

# Contraseña generada
contrasena = f"{binario_letras_ape1}{parte2}####tr3dF{parte3}11"

# Salida
print(f"\nHola {nombre}, he captado tus datos personales:\n")
print(f"NOMBRE: {nombre} {ape1} {ape2}")
print(f"NIA: {nia}")
print(f"Fecha de nacimiento: {fecha_str} por lo que tienes {edad} años")
print("\nTus aficiones son:")
for a in aficiones:
    print(a)

print(f"\nA continuación te ofrezco tu contraseña personal: {contrasena}")
