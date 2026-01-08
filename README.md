# 🎮 Juego de Laberinto con Pygame

Un juego de laberinto interactivo creado con Pygame, optimizado para dispositivos móviles con controles táctiles intuitivos.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.5.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Descripción

Este proyecto contiene un juego de laberinto creado en Pygame, optimizado para dispositivos móviles. El jugador debe navegar a través de un laberinto desde una posición inicial hasta la salida, evitando las paredes.

## ✨ Características Principales

### 🎯 Controles Táctiles en Pantalla
- **Botones táctiles** diseñados específicamente para dispositivos móviles
- **4 direcciones** de movimiento: arriba, abajo, izquierda, derecha
- **Respuesta visual** cuando se presionan los botones
- **Compatible con mouse y touch** para máxima versatilidad

### 📱 Pantalla Adaptable
- **Ajuste dinámico** de resolución a cualquier tamaño de pantalla
- **Escalado proporcional** de todos los elementos del juego
- **Responsive design** que se adapta a orientación portrait y landscape
- **Redimensionable** en tiempo real sin perder funcionalidad

### 🏰 Laberinto Funcional
- **Posición inicial** predeterminada para el jugador
- **Objetivo claro**: alcanzar la salida (celda verde)
- **Paredes intransitables** que bloquean el paso
- **Detección de colisiones** precisa
- **Sistema de victoria** al alcanzar la meta

### ⚡ Optimización para Móviles
- **Rendimiento fluido** en dispositivos móviles
- **Interfaz minimalista** para priorizar la jugabilidad
- **Recursos optimizados** para menor consumo de batería
- **60 FPS** constantes para una experiencia suave

## 🚀 Instalación

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/mgodoyvargas20/pygame-laberinto.git
   cd pygame-laberinto
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el juego**
   ```bash
   python main.py
   ```

## 🎮 Cómo Jugar

### Objetivo
Navega desde la posición inicial (círculo azul) hasta la salida (celda verde) sin atravesar las paredes (celdas negras).

### Controles

#### Dispositivos Móviles / Táctiles
- Usa los **botones en pantalla** en la parte inferior
- Toca el botón con la flecha correspondiente para mover al jugador

#### Teclado (PC/Laptop)
- **Flecha Arriba** o **↑**: Mover hacia arriba
- **Flecha Abajo** o **↓**: Mover hacia abajo
- **Flecha Izquierda** o **←**: Mover hacia la izquierda
- **Flecha Derecha** o **→**: Mover hacia la derecha
- **R**: Reiniciar el juego después de ganar

### Mecánicas del Juego
- El jugador (círculo azul) comienza en la esquina superior izquierda
- Las celdas blancas son caminos transitables
- Las celdas negras son paredes que no se pueden atravesar
- La celda verde es la salida/meta
- Al alcanzar la salida, aparece un mensaje de victoria
- Presiona **R** para reiniciar y jugar nuevamente

## 🛠️ Personalización

### Modificar el Laberinto

Puedes personalizar el laberinto editando la matriz `LABERINTO` en `main.py`:

```python
LABERINTO = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    # ... más filas
]
```

**Leyenda:**
- `1` = Pared (negro)
- `0` = Camino (blanco)
- `2` = Salida (verde)

### Cambiar Posición Inicial

Modifica la constante `JUGADOR_INICIO` en `main.py`:

```python
JUGADOR_INICIO = (1, 1)  # (columna, fila)
```

### Personalizar Colores

Edita las constantes de color al inicio de `main.py`:

```python
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 120, 200)
VERDE = (50, 200, 50)
# ...
```

## 📂 Estructura del Proyecto

```
pygame-laberinto/
│
├── main.py              # Archivo principal del juego
├── requirements.txt     # Dependencias del proyecto
└── README.md           # Documentación (este archivo)
```

## 🔧 Arquitectura del Código

### Clases Principales

#### `BotonTactil`
Maneja los botones táctiles en pantalla con detección de clicks y eventos touch.

#### `Jugador`
Representa al jugador con lógica de movimiento y detección de colisiones.

#### `JuegoLaberinto`
Clase principal que gestiona:
- Inicialización de Pygame y pantalla
- Bucle principal del juego
- Renderizado de elementos
- Manejo de eventos
- Escalado adaptable

## 🎯 Características Técnicas

- **Arquitectura orientada a objetos** para código mantenible
- **Detección de eventos táctiles** nativos de Pygame
- **Sistema de coordenadas escalable** que se adapta al tamaño de pantalla
- **Manejo eficiente de eventos** para múltiples tipos de entrada
- **Renderizado optimizado** con doble buffer
- **Tipado de Python** para mejor legibilidad del código

## 🐛 Solución de Problemas

### El juego no inicia
- Verifica que Pygame esté instalado: `pip install pygame`
- Comprueba la versión de Python: `python --version` (debe ser 3.7+)

### Los controles no responden
- En dispositivos móviles, asegúrate de tocar directamente los botones
- En PC, usa las flechas del teclado como alternativa

### Rendimiento lento
- Cierra otras aplicaciones para liberar memoria
- Reduce el tamaño de la ventana si es muy grande

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Haz fork del proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Ideas para Mejoras Futuras

- [ ] Múltiples niveles con dificultad creciente
- [ ] Sistema de puntuación basado en tiempo y movimientos
- [ ] Efectos de sonido y música de fondo
- [ ] Animaciones para el movimiento del jugador
- [ ] Generación procedural de laberintos
- [ ] Modo multijugador
- [ ] Sistema de power-ups
- [ ] Guardar récords y puntuaciones

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## 👨‍💻 Autor

**mgodoyvargas20**

## 🙏 Agradecimientos

- Comunidad de Pygame por la excelente biblioteca
- Inspirado en juegos clásicos de laberinto
- Diseñado pensando en la accesibilidad móvil

---

¡Disfruta jugando y aprendiendo con este proyecto! 🎮✨
