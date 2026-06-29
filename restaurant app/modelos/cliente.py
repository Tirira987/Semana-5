class Cliente:
    """Clase que representa a un cliente registrado en el sistema."""

    def __init__(self, cedula: str, nombre_completo: str, edad: int, es_frecuente: bool):
        # Atributos con identificadores descriptivos y tipos de datos básicos
        self.cedula: str = cedula
        self.nombre_completo: str = nombre_completo
        self.edad: int = edad
        self.es_frecuente: bool = es_frecuente

    def __str__(self) -> str:
        # Representación en texto del objeto Cliente
        tipo_cliente = "Frecuente" if self.es_frecuente else "Regular"
        return f"Cliente: {self.nombre_completo} | Cédula: {self.cedula} | Edad: {self.edad} años | Tipo: {tipo_cliente}"