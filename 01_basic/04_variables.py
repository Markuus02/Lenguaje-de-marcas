###
# 04_variables
# Las variables sirven para guardas datos en memoria.
# Python es un lenguaje de tipado dinamico y de tipado fuerte.
###

# Asignacion de variables
# solo hace falta poner esto
my_name = "Markuus"
# print(my_name)

age = 18
# print(age)

#age = 19
#print(age)

#Tipado dinamico: el tipo de dato se deremine en tiempo de ejcución
# que no tienes que decalrarlo explicitamente

name = "Markuus"
print(type(name))

name = 18
print(type(name))

print(f"Hola {my_name}, tengo {age + 5} años")

# No recomendada forma de asignar variables
name, age, city = "Markuus", 18, "Valencia"


# Conversación de nombres de variables
mi_nombre_de_variable = "ok"
nombre = "ok"
# No recomendado
# MiNombreDeVariable = "ko"
# minonbredevariable = "ko"

mi_nombre_de_variable_123 = "ok"

MI_CONTANTE = 3.1416

# Nombre de variables no permitidos
# 123_variable = "error"
# mi-variable = "error"
# mi variable = "error"

#true = false

# Palabras reservadas
# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

is_user_logged_in: bool = True
print(is_user_logged_in)

is_user_logged_in = 42
print(is_user_logged_in)

name: str = "midudev"