# Sistema de Gestión de Restaurante (POO en Python)

## Información del Estudiante
* **Nombre Completo:** Richard Arturo Tirira Díaz
* **Institución:** Universidad Estatal Amazónica (UEA)
* **Carrera:** Tecnologías de la Información
* **Asignatura:** Programación Orientada a Objetos
* **Semana:** Semana 5

## Descripción del Sistema
Este proyecto consiste en un sistema básico de gestión interna para un restaurante desarrollado bajo el paradigma de **Programación Orientada a Objetos (POO)** en Python. El sistema ha sido estructurado de forma completamente modular, distribuyendo las responsabilidades en paquetes específicos para asegurar un código limpio, mantenible y escalable. 

El objetivo principal es demostrar el uso correcto de clases, constructores, atributos con tipado explícito, métodos de administración de datos y la implementación de colecciones dinámicas (listas) para simular la persistencia en memoria, evitando deliberadamente el uso de interfaces complejas o menús interactivos según los requerimientos de la cátedra.

## Estructura del Proyecto
El repositorio respeta estrictamente la arquitectura modular solicitada por el docente:

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
