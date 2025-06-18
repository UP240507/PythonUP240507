# Concatenar cadenas
print(' '.join(['Thirty', 'Days', 'Of', 'Python']))   # 'Thirty Days Of Python'
print(' '.join(['Coding', 'For', 'All']))             # 'Coding For All'

# Declarar una variable e imprimirla
company = 'Coding For All'
print(company)

# imprimir la longitud de company
print(len(company))

# Mayusculas y minusculas
print(company.upper())
print(company.lower())

# capitalize(), title(), swapcase()
print(company.capitalize())   # Mayusculas solo la primera letra inicial
print(company.title())        # Mayuscula cada primer letra de cada palabra 
print(company.swapcase())     # Mayuscula todo excepeto la primer letra de cada palabra

# Cortar/quitar la primer palabra
print(company[7:])            # 'For All'

# Checar si está la palabra 'Coding'
print(company.find('Coding')) 
print(company.index('Coding'))
print()
print("------------------")
# Remplazar 'Coding' con 'Python'
print(company.replace('Coding', 'Python'))

print()
print("------------------")

# Cambiar 'Python for Everyone' a 'Python for All'
print('Python for Everyone'.replace('All', 'Everyone'))

print()
print("------------------")

# Separar usando espacio
print(company.split())

print()
print("------------------")

# Separar usando coma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

# Caracter en la posicion 0
print(company[0])

# Ultima posicion
print(company[-1])

# Caracter en la posicion 10
print(company[10])

# Acronimo para 'Python For Everyone'
acro1 = ''.join([palabra[0] for palabra in 'Python For Everyone'.split()])
print(acro1)

# Acronimo para 'Coding For All'
acro2 = ''.join([palabra[0] for palabra in company.split()])
print(acro2)

# Posicion de la primera "C" y "F"
print(company.index('C'))
print(company.index('F'))

# Posicion de la ultima 'l' que se repite en 'Coding For All People'
print('Coding For All People'.rfind('l'))

# Oracion con multiples 'because'
oracion = 'You cannot end a sentence with because because because is a conjunction'
print(oracion.find('because'))
print(oracion.rindex('because'))

# Cortar 'because because because'
start = oracion.find('because')
end = oracion.rindex('because') + len('because')
print(oracion[start:end])

# Empieza con 'Coding'?
print(company.startswith('Coding'))

# Termina con 'coding'?
print(company.endswith('coding'))

# Remove los espacios de más
print('   Coding For All      '.strip())

# isidentifier()
print('30DaysOfPython'.isidentifier())       # False
print('thirty_days_of_python'.isidentifier())# True

# Ingresar una lista con espacio y gatito
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

# Salto de linea
print("I am enjoying this challenge.\nI just wonder what is next.")

# Espacio con tab
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# Metodo de formato
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))

# Operaciones matematicas mostrando las operaciones realizadas
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")