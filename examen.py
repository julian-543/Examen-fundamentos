productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'], 
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'], 
            'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'], 
            'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'], 
            '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'], 
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
                           } 

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7], 
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
                 } 

def stock_marca(marca):
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            total += stock.get(modelo)[1]
    print(f"el stock es {total}")

def busqueda_precio(p_min, p_max):
    resultado_busqueda = []
    for modelo, datos in stock.items():
        precio, unidades = datos
        if p_min <= precio <= p_max and unidades > 0:
            marca = productos[modelo][0]
            resultado_busqueda.append(f"{marca}--{modelo}")
    if resultado_busqueda:
        resultado_busqueda.sort()
        print(f"los notebooks entre los precios consultas son: {resultado_busqueda}")
    else:
        print("no hay notebooks en ese rango de precios")

def eliminar_producto(modelo):
    if modelo in productos:
        productos[modelo].remove
        return True
    return False

opcion = 0

while opcion !=4:

    print("menu principal")
    print("1. Stock marca")
    print("2. Busqueda por precio")
    print("3. Eliminar producto")
    print("4. Salir")
    opcion = int(input("ingrese su opcion: "))
    match opcion:
        case 1:
            marca = input("ingrese la marca a consultar: ")
            stock_marca(marca)
        case 2:
            try:
                p_min = int(input("ingrese precio minimo: $"))
                p_max = int(input("ingrese precio maximo: $"))
                busqueda_precio(p_min, p_max)
            except ValueError:
                print("debe ingresar valores enteros")
        case 3:
            continuar = "si"
            while continuar == "si":
                modelo = input("ingrese modelo a actualizar: ")
                resultado = eliminar_producto(modelo)
                if resultado == True:
                    print("producto eliminado")
                    continuar = input("desea eliminar otro producto (si/no)?:").lower()
                else:
                    print("el modelo no existe")
                    continuar = input("desea eliminar otro producto (si/no)?: ").lower()
        case 4:
            print("programa finalizado")
        case _:
            print("debe ingresar una opcion valida")
            