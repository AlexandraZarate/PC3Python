class Producto:
    def __init__(self, nombre, precio, stock, año):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.año = año
        print('Se ha creado el producto:', self.nombre)

    def __str__(self):
        return '{} - Precio: ${} - Stock: {} - Año: {}'.format(self.nombre, self.precio, self.stock, self.año)


class Catalogo:
    productos = []

    def __init__(self, productos=[]):
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def mostrar(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if productos_filtrados:
            print(f"Productos del año {año}:")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No hay productos del año {año} en el catálogo.")


# Crear algunos productos
producto1 = Producto("Laptop", 800, 10, 2021)
producto2 = Producto("Smartphone", 500, 20, 2020)
producto3 = Producto("Tablet", 300, 15, 2019)

# Crear un catálogo de productos
catalogo_productos = Catalogo([producto1, producto2, producto3])

# Mostrar catálogo completo
print("Catálogo completo:")
catalogo_productos.mostrar()

# Agregar un nuevo producto al catálogo
producto_nuevo = Producto("Impresora", 200, 5, 2021)
catalogo_productos.agregar(producto_nuevo)

# Mostrar catálogo actualizado
print("\nCatálogo actualizado:")
catalogo_productos.mostrar()

# Filtrar productos por año
print("\nFiltrando productos por año:")
catalogo_productos.filtrar_por_año(2021)
