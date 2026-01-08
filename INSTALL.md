# 📦 Guía de Instalación y Ejecución

Esta guía te ayudará a instalar y ejecutar el juego de laberinto en diferentes plataformas.

## 🖥️ Instalación en PC (Windows, macOS, Linux)

### Opción 1: Instalación Rápida

```bash
# 1. Clonar el repositorio
git clone https://github.com/mgodoyvargas20/pygame-laberinto.git
cd pygame-laberinto

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar el juego
python main.py
```

### Opción 2: Usando Entorno Virtual (Recomendado)

#### Windows
```bash
# 1. Clonar y entrar al directorio
git clone https://github.com/mgodoyvargas20/pygame-laberinto.git
cd pygame-laberinto

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
venv\Scripts\activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar el juego
python main.py
```

#### macOS/Linux
```bash
# 1. Clonar y entrar al directorio
git clone https://github.com/mgodoyvargas20/pygame-laberinto.git
cd pygame-laberinto

# 2. Crear entorno virtual
python3 -m venv venv

# 3. Activar entorno virtual
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar el juego
python main.py
```

## 📱 Instalación en Dispositivos Móviles

### Android (Usando Pydroid 3)

1. **Instalar Pydroid 3** desde Google Play Store
2. **Abrir Pydroid 3** y acceder al menú
3. **Instalar Pygame**:
   - Ir a "Pip" en el menú
   - Buscar "pygame"
   - Instalar
4. **Descargar los archivos**:
   - Descargar `main.py` desde el repositorio
   - Guardar en la carpeta de Pydroid 3
5. **Ejecutar**:
   - Abrir `main.py` en Pydroid 3
   - Presionar el botón "Play"

### iOS (Usando Pythonista)

1. **Instalar Pythonista** desde App Store (aplicación de pago)
2. **Instalar Pygame**:
   - Abrir Pythonista
   - Instalar pygame usando StaSh o el gestor de paquetes
3. **Importar el código**:
   - Crear un nuevo archivo llamado `main.py`
   - Copiar el contenido del repositorio
4. **Ejecutar el juego**

> **Nota**: El rendimiento en iOS puede variar dependiendo de las limitaciones de Pythonista.

## 🧪 Ejecutar las Pruebas

```bash
# Ejecutar todas las pruebas
python test_main.py

# Ejecutar con más detalle
python test_main.py -v
```

## 🔧 Solución de Problemas Comunes

### Error: "No module named 'pygame'"
**Solución**: Instalar pygame
```bash
pip install pygame
```

### Error: "python: command not found" (Linux/macOS)
**Solución**: Usar python3
```bash
python3 main.py
```

### Error: "Permission denied" (Linux/macOS)
**Solución**: Hacer el archivo ejecutable
```bash
chmod +x main.py
./main.py
```

### El juego va muy lento
**Soluciones**:
- Cerrar otras aplicaciones
- Reducir el tamaño de la ventana
- Actualizar los drivers gráficos

### Los botones táctiles no responden (móvil)
**Soluciones**:
- Asegurarse de tocar directamente sobre los botones
- Verificar que el toque esté habilitado en Pygame
- Reiniciar la aplicación

## 📊 Requisitos del Sistema

### Mínimos
- Python 3.7 o superior
- 50 MB de espacio libre
- Resolución mínima: 320x480

### Recomendados
- Python 3.9 o superior
- 100 MB de espacio libre
- Resolución recomendada: 800x600 o superior

## 🎮 Controles

### En PC/Laptop
- **Flechas del teclado**: Mover al jugador
- **R**: Reiniciar después de ganar

### En Dispositivos Móviles
- **Botones en pantalla**: Tocar los botones direccionales
- **R en teclado virtual**: Reiniciar después de ganar

## 📞 Soporte

Si encuentras algún problema:

1. Revisa esta guía de instalación
2. Consulta el README.md principal
3. Verifica que tengas la última versión de Python y Pygame
4. Abre un issue en el repositorio de GitHub

## 🚀 ¡Listo para Jugar!

Una vez instalado, simplemente ejecuta:
```bash
python main.py
```

¡Disfruta del juego! 🎮
