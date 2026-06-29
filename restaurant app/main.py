# Punto de arranque de la aplicación modular
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def ejecutar_sistema():
    # 1. Instanciar el servicio principal del restaurante
    mi_restaurante = Restaurante("Amazonas Gourmet")

    # 2. Crear al menos dos objetos del modelo Producto
    producto_uno = Producto("Maito de Pescado", 8.50, 15, True)
    producto_dos = Producto("Chicha de Chonta", 2.00, 40, True)
    producto_tres = Producto("Ayampaco", 7.00, 0, False) # Ejemplo agotado

    # 3. Crear al menos dos objetos del modelo Cliente
    cliente_uno = Cliente("1600123456", "Carlos Morocho", 28, True)
    cliente_dos = Cliente("1700987654", "Ana María Aguinda", 22, False)

    # 4. Agregar los objetos creados a las listas administradas por el servicio
    mi_restaurante.registrar_producto(producto_uno)
    mi_restaurante.registrar_producto(producto_dos)
    mi_restaurante.registrar_producto(producto_tres)

    mi_restaurante.registrar_cliente(cliente_uno)
    mi_restaurante.registrar_cliente(cliente_dos)

    # 5. Mostrar la información registrada de forma organizada en la consola
    print("====================================================")
    print(f"  SISTEMA DE GESTIÓN: {mi_restaurante.nombre_restaurante}")
    print("====================================================")
    
    mi_restaurante.mostrar_inventario()
    mi_restaurante.mostrar_clientes()
    
    print("\n====================================================")

if __name__ == "__main__":
    ejecutar_sistema()