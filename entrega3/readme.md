--
title: Gestion de Inventarios

---

# Gestion de Inventarios

## Descripción del Problema

Este proyecto implementa un sistema de inventarios utilizando una estructura de datos de grafo en Python. El sistema permite gestionar productos, sus relaciones y ubicaciones dentro de un almacén o cadena de suministro.

## Funcionalidades Principales

- Inserción de nuevos productos al inventario
- Eliminación de productos del inventario
- Búsqueda de productos en el inventario
- Visualización de relaciones entre productos (por ejemplo, productos complementarios o sustitutos)
- Seguimiento de la ubicación de los productos en el almacén

## Etapas del Proyecto

1. **Análisis inicial del problema**:
   - Definición de los requisitos del sistema de inventarios.
   - Identificación de las operaciones principales necesarias.

2. **Implementación con Listas Enlazadas**:
   - Diseño de la estructura de datos para representar productos y sus relaciones.
   - Implementación de operaciones básicas (inserción, eliminación, búsqueda).
   - Desarrollo de funciones para manejar relaciones entre productos.
   - Pruebas de rendimiento y funcionalidad.

3. **Evaluación de la implementación con Listas Enlazadas**:
   - Análisis de eficiencia en diferentes escenarios.
   - Identificación de limitaciones y áreas de mejora.

4. **Diseño de la estructura del grafo**:
   - Definición de nodos (productos) y aristas (relaciones entre productos).
   - Planificación de la transición de listas enlazadas a grafos.

5. **Implementación basada en Grafos**:
   - Desarrollo de las operaciones fundamentales del grafo (inserción, eliminación, búsqueda).
   - Adaptación de las funcionalidades existentes al nuevo modelo de datos.
   - Implementación de algoritmos específicos para grafos para optimizar la gestión del inventario.



6. **Pruebas comparativas y optimización**:
   - Evaluación del rendimiento de ambas implementaciones (listas enlazadas vs. grafos).
   - Optimización de algoritmos y estructuras de datos.

7. **Documentación y preparación final**:
   - Elaboración del README.
   - Preparación de la presentación final del proyecto.


## Equipo de Desarrollo

- Cristian de Jesús Chavez Choperena - 2182190
- Cristian Eduardo Johnson Acevedo - 2155160
- Juan Pablo Aparicio Torres - 2230048
- Jhoan Sebastian Rey Sánchez - 2210060


## Conclusiones

Tras implementar el sistema de inventarios utilizando tanto listas enlazadas como grafos, hemos llegado a las siguientes conclusiones sobre eficiencia:

1. **Comparación de estructuras**:
   - La implementación con listas enlazadas demostró ser eficiente para operaciones secuenciales y cuando el número de relaciones entre productos es limitado.
   - La implementación basada en grafos ofrece mayor flexibilidad y eficiencia para representar relaciones complejas entre productos.

2. **Eficiencia en búsquedas**:
   - En listas enlazadas, las búsquedas tienen una complejidad de O(n) en el peor caso.
   - Los grafos permiten búsquedas más eficientes, especialmente en inventarios grandes con muchas interconexiones, pudiendo alcanzar O(1) para búsquedas directas con una implementación adecuada.

3. **Manejo de relaciones**:
   - Los grafos son superiores en la representación y navegación de relaciones entre productos (como productos complementarios o sustitutos).
   - Las listas enlazadas requieren estructuras adicionales o búsquedas más complejas para manejar estas relaciones.

4. **Escalabilidad**:
   - La implementación con grafos se adapta mejor al crecimiento del inventario y al aumento en la complejidad de las relaciones entre productos.
   - Las listas enlazadas pueden volverse menos eficientes a medida que el sistema crece.

5. **Uso de memoria**:
   - Las listas enlazadas pueden ser más eficientes en el uso de memoria para inventarios pequeños o con pocas relaciones.
   - Los grafos, aunque pueden requerir más memoria inicial, ofrecen un mejor rendimiento en sistemas de inventario grandes y complejos.

6. **Implementación y mantenimiento**:
   - La implementación con listas enlazadas es más sencilla y puede ser suficiente para sistemas de inventario simples.
   - Los grafos requieren una implementación más compleja, pero ofrecen mayor flexibilidad y potencial de optimización a largo plazo.

En conclusión, para nuestro proyecto, la implementación basada en grafos resulta más eficiente y adecuada, especialmente considerando la necesidad de manejar relaciones complejas entre productos y la escalabilidad futura del sistema. Sin embargo, la elección entre listas enlazadas y grafos dependerá en última instancia del tamaño específico del inventario, la complejidad de las relaciones entre productos y los requisitos de rendimiento del sistema.
