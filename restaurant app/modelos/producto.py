class Producto:
    """Clase que representa un plato o bebida disponible en el restaurante."""

    def __init__(self, nombre: str, precio: float, stock: int, disponible: bool):
        # Atributos con identificadores descriptivos y tipos de datos básicos
        self.nombre: str = nombre
        self.precio: float = precio
        self.stock: int = stock
        self.disponible: bool = disponible

    def __str__(self) -> str:
        # Representación en texto del objeto Producto
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock} uds | Estado: {estado}"