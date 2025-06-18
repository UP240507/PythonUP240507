# 1. Declarar una lista vacía
listaV = []

# 2. Declarar una lista con más de 5 items
lista = [1, 2, 3, 4, 5, 6]

# 3. Encontrar el tamaño de la lista
tamañoLista = len(lista)
print(tamañoLista)

# 4. Tomar el primer item, el de en medio y el ultimo de la lista
primerI = lista[0]
ItemMi = lista[len(lista) // 2]
UltimoI = lista[-1]

# 5. Declarar una lista mixta
mixed_data_types = ["Christopher", 24, 1.80, "Soltero", "Zona Centro"]

# 6. Declarar una lista de compañias
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Imprimir la lista
print(it_companies)

# 8. Imprimir la cantidad de compañias
print(len(it_companies))

# 9. Imprimir la primera, la de en medio y la ultima compañia
PrimerEm = it_companies[0]
EmpresaEn = it_companies[len(it_companies) // 2]
UltimaEm = it_companies[-1]
print(PrimerEm)
print(EmpresaEn)
print(UltimaEm)

# 10. Imprimir la lista despues de modificarla
it_companies[0] = "Meta"  # Changing Facebook to Meta
print(it_companies)

# 11. Agregar otra empresa a it_companies
it_companies.append("Tesla")

# 12. Insertar una empresa enmedio de la lista
it_companies.insert(len(it_companies) // 2, "Nvidia")

# 13. Cambiar uno de los nombres de las empresas a mayuscula
for i in range(len(it_companies)):
    if it_companies[i] != "IBM":
        it_companies[i] = it_companies[i].upper()

# 14. Ingresar it_companies con '#;  '
joined_companies = '#;  '.join(it_companies)

# 15. Checar si alguna empresa está dentro de it_companies
EmpresaEx = "Google" in it_companies

# 16. Clasificar la lista
it_companies.sort()

# 17. Poner la lista de manera descendente
it_companies.reverse()

# 18. Cortar los primeros 3 elementos de la lista
Primeros3 = it_companies[:3]

# 19. Cortar los ultimos 3 elementos de la lista
Ultimos3 = it_companies[-3:]

# 20. Cortar la mitad de las empresas de la lista
mitad = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    mitadE = it_companies[mitad - 1:mitad + 1]
else:
    mitadE = it_companies[mitad:mitad + 1]

# 21. Quitar la primer empresa de la lista
it_companies.pop(0)

# 22. Quitar la empresa que esté a la mitad de lista
if len(it_companies) % 2 == 0:
    it_companies.pop(mitad - 1) 
    it_companies.pop(mitad - 1) 
else:
    it_companies.pop(mitad)

# 23. Quitar la ultima empresa
it_companies.pop()

# 24. Limpiar la lista
it_companies.clear()

# 25. Borrar la lista
del it_companies

# 26. Ingresar las siguientes listas
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end

# 27. Insertar Python y SQL despues Redux
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')

# Imprimir la lista
print(full_stack)