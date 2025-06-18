edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

edades.sort()
edadmin = min(edades)
edadmax = max(edades)

# 2. Añadir nuevamente las edades minima y maxima
edades.append(edadmin)
edades.append(edadmax)

# 3. Encontrar la edad media
n = len(edades)
if n % 2 == 0:
    edad_media = (edades[n // 2 - 1] + edades[n // 2]) / 2
else:
    edad_media = edades[n // 2]

# 4. Encontrar la edad promedio
edad_prom = sum(edades) / len(edades)

# 5. Rango de las edades
rangoE = edadmax - edadmin

# 6. Comparar los valores (min - average) y (max - average), usar abs()
minProm = abs(edadmin - edad_prom)
maxProm = abs(edadmax - edad_prom)

# 7. Lista de paises
paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# 8. Encontrar el país que está a la mitad de la lista
n_paises = len(paises)
if n_paises % 2 == 0:
    mitadPa = paises[n_paises // 2 - 1:n_paises // 2 + 1]
else:
    mitadPa = paises[n_paises // 2]

# 9. Dividir la lista en dos listas iguales
if n_paises % 2 == 0:
    PrimeraMitad = paises[:n_paises // 2]
    SegundaMitad = paises[n_paises // 2:]
else:
    PrimeraMitad = paises[:n_paises // 2 + 1]
    SegundaMitad = paises[n_paises // 2 + 1:]

# 10. Desenlistar los primeros 3 paises y los demás paises escandicos
primer_pais, segundo_pais, tercer_pais, *scandic_paises = paises

# Imprimir los resultados
print("Acomodar edades:", edades)
print("edad minima:", edadmin)
print("edad máxima:", edadmax)
print("Edad media:", edad_media)
print("Edad promedio:", edad_prom)
print("Rango de edades:", rangoE)
print("Diferencia del promedio minimo:", minProm)
print("Diferencia del promedio maximo:", maxProm)
print("Pais(es) en la mitad:", mitadPa)
print("Primera mitad de la lista:", PrimeraMitad)
print("Segunda mitad de la lista:", SegundaMitad)
print("Primer país:", primer_pais)
print("Segundo país:", segundo_pais)
print("Tercer país:", tercer_pais)
print("Paises escándicos:", scandic_paises)
