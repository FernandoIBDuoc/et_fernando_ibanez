#  Iniciamos con el diccionario de las prendas.
# nombre, categoria, talla, color, material, es_unisex
prendas = {
'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
'S002': ['Jeans Slim', 'pantalon', 'L', 'azul','denim', False],
'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False]
}

# Diccionario de bodega.
# precio, unidades.
bodega = {
'S001': [7990, 12],
'S002': [19990, 0],
'S003': [29990, 3],
'S004': [24990, 6],
'S005': [17990, 8],
'S006': [14990, 2]
}
    
# Opción 1:
def unidades_categoria(categoria):
    global prendas
    global bodega
    acumulador=0
    for prendas in categoria:
        for bodega in bodega:
            acumulador+=1
        
    print(f"El total de unidades disponibles es: {acumulador-2}")


# Opción 2:
def busqueda_precio(p_min, p_max):
    print("")

# Opción 3:
def buscar_codigo(codigo):
    print("")
def actualizar_precio(codigo, nuevo_precio):
    print("")

# Opción 4:
def agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades):
    print("")

# Opción 5:
def eliminar_prenda(codigo):
    print("")


def leer_opcion():
    try:
        print('''
========== MENÚ PRINCIPAL ==========
1. Unidades por categoría
2. Búsqueda de prendas por rango de precio
3. Actualizar precio de prenda
4. Agregar prenda
5. Eliminar prenda
6. Salir
=====================================
''')
        opcion=int(input("Ingrese opción: "))
        if opcion==1:
            return opcion
        elif opcion==2:
            return opcion
        elif opcion==3:
            return opcion
        elif opcion==4:
            return opcion
        elif opcion==5:
            return opcion
        elif opcion==6:
            return opcion
        else:
            print("Opción no válida, seleccione una opción correcta.")
            return None
    except ValueError:
        print("Error: ingrese un número entero.")
        return None

while True:
    opt=leer_opcion()
    if opt==1:
        unidades_categoria(categoria=(input("Ingrese categoría a consultar: ").lower()))
    elif opt==2:
        print("")
    elif opt==3:
        print("")
    elif opt==4:
        print("")
    elif opt==6:
        print("")