from libro import Libro
from carroCompra import carroCompra
class TiendaVirtual:
    def __init__(self):
        self.productos=[]
    def llenarProductos(self):
        libro1 = Libro("Biblia", "religion" , 30000, 50000, 50)
        libro2 = Libro("quijote", "aventura", 25000, 45000, 50)
        libro3 = Libro("Corán", "religion", 28000, 48000, 50)
        libro4 = Libro("Libro de Mormón", "religion", 26000, 47000, 50)
        libro5 = Libro("Bagavad Gita", "religion", 27000, 46000, 50)
        libro6 = Libro("Cien Años de Soledad", "ficcion", 35000, 60000, 50)
        
        self.productos.append(libro1)
        self.productos.append(libro2)
        self.productos.append(libro3)
        self.productos.append(libro4)
        self.productos.append(libro5)
        self.productos.append(libro6)
    def mostrarProductos(self):
        for producto in self.productos:
            print(f"""
                  Libro     : {producto.nombre}
                  Tipo      : {producto.categoria}
                  Precio    : {producto.precioVenta}
                  Disponible: {producto.cantidadBodega} unidades.
                  """)
            
    def catalogoLibros(self):
        for prod in self.productos:
            if isinstance(prod, Libro):
                    print(f"""
                  Libro     : {prod.nombre}
                  """)  
                      
    def mostrarProducto(self,producto):
        for prod in self.productos:
            if isinstance(prod, Libro):
                if prod.nombre==producto:
                    print(f"""
                  Libro     : {prod.nombre}
                  Tipo      : {prod.categoria}
                  Precio    : {prod.precioVenta}
                  Disponible: {prod.cantidadBodega} unidades.
                  """)
    
    def consultar_producto(self, producto):
        for prod in self.productos:
            if isinstance(prod, Libro):
                if prod.nombre==producto:
                    return prod.cantidadBodega 
        return False
                      
            
    # Dentro de la función realizar_venta
    def realizar_venta(self):
        # Crear un carro de compra para el cliente
        carro_compra = carroCompra()

        while True:
            resp = input("Desea agregar productos al carro de compra? (si/no): ").lower()

            if resp == "no":
                break
            elif resp == "si":
                producto_nombre = input("Digite el nombre del producto que desea agregar: ").lower()
                cantidad = int(input("Digite la cantidad que desea comprar: "))

                # Buscar el producto en la lista de productos
                producto_en_bodega = None
                for prod in self.productos:
                    if isinstance(prod, Libro) and prod.nombre.lower() == producto_nombre:
                        producto_en_bodega = prod
                        break

                if producto_en_bodega:
                    cantidad_disponible = producto_en_bodega.cantidadBodega

                    if cantidad <= cantidad_disponible:
                        producto_en_bodega.cantidadBodega -= cantidad
                        precio_venta = producto_en_bodega.precioVenta * cantidad
                        #carro_compra.agregar_producto(producto_en_bodega, cantidad, precio_venta)
                    else:
                        print(f"No hay suficientes unidades en bodega para {producto_nombre}")
                else:
                    print(f"El producto {producto_nombre} no existe en la tienda")

        # Lógica adicional para finalizar la venta, imprimir recibo, etc.

                    
                    
                
                
                
                
                
                
                
                # (puedes llamar al método agregar_item en el objeto carro_compra)
                ###carro_compra.agregarAlCarro(producto, cantidad)
                # Calcular el total de la compra
                ###total_compra = carro_compra.calcularTotal()

                # Lógica adicional (procesar pago, generar pedido, etc.)
                # Aquí es donde restarías la cantidad de libros de la bodega

                # Reducir la cantidad en bodega de cada libro vendido
                

                    # Verificar si hay suficientes libros en la bodega

        