from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Clase de servicio que administra las listas de productos y clientes."""

    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante: str = nombre_restaurante
        # Uso de listas como tipo de dato compuesto para almacenar objetos
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> None:
        """Agrega un nuevo objeto Producto a la lista del restaurante."""
        self.lista_productos.append(producto)

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Agrega un nuevo objeto Cliente a la lista del restaurante."""
        self.lista_clientes.append(cliente)

    def mostrar_inventario(self) -> None:
        """Muestra en consola todos los productos registrados."""
        print(f"\n--- INVENTARIO DE {self.nombre_restaurante.upper()} ---")
        if not self.lista_productos:
            print("No hay productos registrados.")
        for producto in self.lista_productos:
            print(producto)  # Invoca automáticamente al método __str__()

    def mostrar_clientes(self) -> None:
        """Muestra en consola todos los clientes registrados."""
        print(f"\n--- CLIENTES REGISTRADOS EN {self.nombre_restaurante.upper()} ---")
        if not self.lista_clientes:
            print("No hay clientes registrados.")
        for cliente in self.lista_clientes:
            print(cliente)  # Invoca automáticamente al método __str__()