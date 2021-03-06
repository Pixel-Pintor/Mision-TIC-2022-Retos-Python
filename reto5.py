
productos = {
    1: ['Manzanas', 6000.0, 97],
    2: ['Limones', 2600.0, 45],
    3: ['Peras', 2700.0, 55],
    4: ['Arandanos', 7300.0, 44],
    5: ['Tomates', 8100.0, 42],
    6: ['Fresas', 9100.0, 99],
    7: ['Helado', 4500.0, 41],
    8: ['Galletas', 600.0, 18],
    9: ['Chocolates', 4500.0, 990],
    10: ['Jamon', 18000.0, 55],
}
print(productos)


def BORRAR(codigo, nombre, precio, inventario):
    '''Esta funcion elimina por completo un producto a partir
    del valor de su codigo clave'''
    del productos[codigo]


BORRAR(5, 'no importa', 3400.0, 32)

print(productos)


# este codigo busca un codigo en las llaves del diccionario para saber si ya esta presente
codigo = 10
if codigo not in productos.keys():
    print('no esta')
else:
    print('si esta')

# for valor in productos[1]:
#     print(f'valor: {valor}')
# valor: Manzanas
# valor: 6000.0
# valor: 97

# for codigo, caracteristicas in productos.items():
#     print(f'\nEl codigo {codigo} tiene los valores:')
#     for caracter in caracteristicas:
#         print(f'Valor: {caracter}')

# El codigo 1 tiene los valores:
# Valor: Manzanas
# Valor: 6000.0
# Valor: 97

sumador = 0
for codigo, caracteristicas in productos.items():
    # print(caracteristicas[1]) <= este codigo accede al valor de precio de la lista anidada
    # este codigo suma perfectamente todos los productos
    sumador += caracteristicas[1]

# Este codigo calcula perfectamente el promedio de precios de la base de datos
promedioPrecios = sumador / 10
print(
    f'El promedio de precios del total {sumador} es igual a {promedioPrecios}...')

# Este codigo calcula perfectamente el articulo que tiene el precio mayor en la base de datos
precioMayor = 0
for codigo, caracteristicas in productos.items():
    if caracteristicas[1] > precioMayor:
        articuloMayor = caracteristicas[0]
        precioMayor = caracteristicas[1]
print(articuloMayor)


# Este codigo calcula perfectamente el articulo que tiene el precio menor en la base de datos
precioMenor = precioMayor
for codigo, caracteristicas in productos.items():
    if caracteristicas[1] < precioMenor:
        articuloMenor = caracteristicas[0]
        precioMenor = caracteristicas[1]

print(articuloMenor)

# Este codigo calcula perfectamente el total del inventario
# multiplicando cada precio por la cantidad de productos
listaPrecios = []
for codigo, caracteristicas in productos.items():
    inventario = caracteristicas[1] * caracteristicas[2]
    print(inventario)
    listaPrecios.append(inventario)

sumaInventario = 0
for precio in listaPrecios:
    sumaInventario += precio

print(sumaInventario)
