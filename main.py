#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Juego de Laberinto con Pygame
Optimizado para dispositivos móviles con controles táctiles
"""

import pygame
import sys
from typing import Tuple, List

# Inicializar Pygame
pygame.init()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 120, 200)
VERDE = (50, 200, 50)
ROJO = (200, 50, 50)
GRIS = (100, 100, 100)
GRIS_CLARO = (180, 180, 180)

# Configuración del laberinto (1 = pared, 0 = camino, 2 = salida)
LABERINTO = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Posición inicial del jugador
JUGADOR_INICIO = (1, 1)


class BotonTactil:
    """Clase para manejar botones táctiles en pantalla"""
    
    def __init__(self, x: int, y: int, ancho: int, alto: int, texto: str, direccion: Tuple[int, int]):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.direccion = direccion
        self.presionado = False
        self.color_normal = GRIS_CLARO
        self.color_presionado = AZUL
    
    def dibujar(self, pantalla: pygame.Surface, fuente: pygame.font.Font):
        """Dibuja el botón en la pantalla"""
        color = self.color_presionado if self.presionado else self.color_normal
        pygame.draw.rect(pantalla, color, self.rect, border_radius=10)
        pygame.draw.rect(pantalla, NEGRO, self.rect, 3, border_radius=10)
        
        texto_surface = fuente.render(self.texto, True, NEGRO)
        texto_rect = texto_surface.get_rect(center=self.rect.center)
        pantalla.blit(texto_surface, texto_rect)
    
    def verificar_click(self, pos: Tuple[int, int]) -> bool:
        """Verifica si el botón fue clickeado"""
        return self.rect.collidepoint(pos)


class Jugador:
    """Clase para el jugador"""
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def mover(self, dx: int, dy: int, laberinto: List[List[int]]) -> bool:
        """Intenta mover al jugador. Retorna True si llegó a la meta"""
        nueva_x = self.x + dx
        nueva_y = self.y + dy
        
        # Verificar límites
        if 0 <= nueva_y < len(laberinto) and 0 <= nueva_x < len(laberinto[0]):
            # Verificar si no es una pared
            if laberinto[nueva_y][nueva_x] != 1:
                self.x = nueva_x
                self.y = nueva_y
                # Verificar si llegó a la salida
                return laberinto[nueva_y][nueva_x] == 2
        return False


class JuegoLaberinto:
    """Clase principal del juego"""
    
    def __init__(self):
        # Configuración de pantalla adaptable
        info = pygame.display.Info()
        self.ancho_pantalla = min(info.current_w, 800)
        self.alto_pantalla = min(info.current_h, 800)
        
        self.pantalla = pygame.display.set_mode(
            (self.ancho_pantalla, self.alto_pantalla),
            pygame.RESIZABLE
        )
        pygame.display.set_caption("Laberinto Móvil")
        
        self.reloj = pygame.time.Clock()
        self.jugando = True
        self.victoria = False
        
        # Calcular dimensiones del laberinto
        self.filas = len(LABERINTO)
        self.columnas = len(LABERINTO[0])
        
        # Calcular tamaño de celda basado en el tamaño de pantalla
        self.calcular_dimensiones()
        
        # Crear jugador
        self.jugador = Jugador(*JUGADOR_INICIO)
        
        # Crear botones táctiles
        self.crear_botones()
        
        # Fuentes
        self.fuente_botones = None
        self.fuente_mensaje = None
        self.actualizar_fuentes()
    
    def calcular_dimensiones(self):
        """Calcula las dimensiones adaptables del juego"""
        # Reservar espacio para los controles (30% de la altura)
        espacio_controles = int(self.alto_pantalla * 0.3)
        espacio_laberinto = self.alto_pantalla - espacio_controles
        
        # Calcular tamaño de celda para que el laberinto quepa
        tamano_celda_alto = espacio_laberinto // self.filas
        tamano_celda_ancho = self.ancho_pantalla // self.columnas
        
        self.tamano_celda = min(tamano_celda_alto, tamano_celda_ancho)
        
        # Calcular offset para centrar el laberinto
        self.laberinto_ancho = self.columnas * self.tamano_celda
        self.laberinto_alto = self.filas * self.tamano_celda
        self.offset_x = (self.ancho_pantalla - self.laberinto_ancho) // 2
        self.offset_y = 20
        
        # Posición de los controles
        self.controles_y = self.offset_y + self.laberinto_alto + 20
    
    def actualizar_fuentes(self):
        """Actualiza el tamaño de las fuentes según el tamaño de pantalla"""
        tamano_fuente_botones = max(16, int(self.tamano_celda * 0.4))
        tamano_fuente_mensaje = max(24, int(self.tamano_celda * 0.8))
        
        self.fuente_botones = pygame.font.Font(None, tamano_fuente_botones)
        self.fuente_mensaje = pygame.font.Font(None, tamano_fuente_mensaje)
    
    def crear_botones(self):
        """Crea los botones de control táctil"""
        tamano_boton = min(80, int(self.ancho_pantalla * 0.15))
        espacio = 10
        
        # Calcular posición central para los botones
        centro_x = self.ancho_pantalla // 2
        centro_y = self.controles_y + 50
        
        # Crear botones en disposición de cruz
        self.botones = [
            BotonTactil(
                centro_x - tamano_boton // 2,
                centro_y - tamano_boton - espacio,
                tamano_boton, tamano_boton, "↑", (0, -1)
            ),  # Arriba
            BotonTactil(
                centro_x - tamano_boton // 2,
                centro_y + espacio,
                tamano_boton, tamano_boton, "↓", (0, 1)
            ),  # Abajo
            BotonTactil(
                centro_x - tamano_boton - espacio - tamano_boton // 2,
                centro_y - tamano_boton // 2,
                tamano_boton, tamano_boton, "←", (-1, 0)
            ),  # Izquierda
            BotonTactil(
                centro_x + espacio + tamano_boton // 2,
                centro_y - tamano_boton // 2,
                tamano_boton, tamano_boton, "→", (1, 0)
            ),  # Derecha
        ]
    
    def dibujar_laberinto(self):
        """Dibuja el laberinto en la pantalla"""
        for fila in range(self.filas):
            for columna in range(self.columnas):
                x = self.offset_x + columna * self.tamano_celda
                y = self.offset_y + fila * self.tamano_celda
                
                celda = LABERINTO[fila][columna]
                
                if celda == 1:  # Pared
                    pygame.draw.rect(
                        self.pantalla, NEGRO,
                        (x, y, self.tamano_celda, self.tamano_celda)
                    )
                elif celda == 2:  # Salida
                    pygame.draw.rect(
                        self.pantalla, VERDE,
                        (x, y, self.tamano_celda, self.tamano_celda)
                    )
                else:  # Camino
                    pygame.draw.rect(
                        self.pantalla, BLANCO,
                        (x, y, self.tamano_celda, self.tamano_celda)
                    )
                
                # Dibujar borde de la celda
                pygame.draw.rect(
                    self.pantalla, GRIS,
                    (x, y, self.tamano_celda, self.tamano_celda),
                    1
                )
    
    def dibujar_jugador(self):
        """Dibuja el jugador en la pantalla"""
        x = self.offset_x + self.jugador.x * self.tamano_celda
        y = self.offset_y + self.jugador.y * self.tamano_celda
        
        # Dibujar círculo para el jugador con margen
        margen = self.tamano_celda // 8
        radio = (self.tamano_celda - 2 * margen) // 2
        centro_x = x + self.tamano_celda // 2
        centro_y = y + self.tamano_celda // 2
        
        pygame.draw.circle(self.pantalla, AZUL, (centro_x, centro_y), radio)
    
    def dibujar_controles(self):
        """Dibuja los controles táctiles"""
        for boton in self.botones:
            boton.dibujar(self.pantalla, self.fuente_botones)
    
    def dibujar_victoria(self):
        """Dibuja mensaje de victoria"""
        overlay = pygame.Surface((self.ancho_pantalla, self.alto_pantalla))
        overlay.set_alpha(200)
        overlay.fill(BLANCO)
        self.pantalla.blit(overlay, (0, 0))
        
        texto = self.fuente_mensaje.render("¡GANASTE!", True, VERDE)
        texto_rect = texto.get_rect(center=(self.ancho_pantalla // 2, self.alto_pantalla // 2))
        self.pantalla.blit(texto, texto_rect)
        
        texto_reinicio = self.fuente_botones.render("Presiona R para reiniciar", True, NEGRO)
        texto_reinicio_rect = texto_reinicio.get_rect(
            center=(self.ancho_pantalla // 2, self.alto_pantalla // 2 + 50)
        )
        self.pantalla.blit(texto_reinicio, texto_reinicio_rect)
    
    def manejar_eventos(self):
        """Maneja los eventos del juego"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.jugando = False
            
            elif evento.type == pygame.VIDEORESIZE:
                self.ancho_pantalla = evento.w
                self.alto_pantalla = evento.h
                self.pantalla = pygame.display.set_mode(
                    (self.ancho_pantalla, self.alto_pantalla),
                    pygame.RESIZABLE
                )
                self.calcular_dimensiones()
                self.crear_botones()
                self.actualizar_fuentes()
            
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r and self.victoria:
                    self.reiniciar()
                elif not self.victoria:
                    dx, dy = 0, 0
                    if evento.key == pygame.K_UP:
                        dy = -1
                    elif evento.key == pygame.K_DOWN:
                        dy = 1
                    elif evento.key == pygame.K_LEFT:
                        dx = -1
                    elif evento.key == pygame.K_RIGHT:
                        dx = 1
                    
                    if dx != 0 or dy != 0:
                        self.victoria = self.jugador.mover(dx, dy, LABERINTO)
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if not self.victoria:
                    pos = pygame.mouse.get_pos()
                    for boton in self.botones:
                        if boton.verificar_click(pos):
                            boton.presionado = True
                            dx, dy = boton.direccion
                            self.victoria = self.jugador.mover(dx, dy, LABERINTO)
            
            elif evento.type == pygame.MOUSEBUTTONUP:
                for boton in self.botones:
                    boton.presionado = False
            
            # Soporte para eventos táctiles (touch)
            elif evento.type == pygame.FINGERDOWN:
                if not self.victoria:
                    # Convertir coordenadas normalizadas a píxeles
                    pos = (int(evento.x * self.ancho_pantalla), 
                           int(evento.y * self.alto_pantalla))
                    for boton in self.botones:
                        if boton.verificar_click(pos):
                            boton.presionado = True
                            dx, dy = boton.direccion
                            self.victoria = self.jugador.mover(dx, dy, LABERINTO)
            
            elif evento.type == pygame.FINGERUP:
                for boton in self.botones:
                    boton.presionado = False
    
    def reiniciar(self):
        """Reinicia el juego"""
        self.jugador = Jugador(*JUGADOR_INICIO)
        self.victoria = False
    
    def actualizar(self):
        """Actualiza el estado del juego"""
        pass
    
    def dibujar(self):
        """Dibuja todos los elementos del juego"""
        self.pantalla.fill(BLANCO)
        
        self.dibujar_laberinto()
        self.dibujar_jugador()
        self.dibujar_controles()
        
        if self.victoria:
            self.dibujar_victoria()
        
        pygame.display.flip()
    
    def ejecutar(self):
        """Bucle principal del juego"""
        while self.jugando:
            self.manejar_eventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()


def main():
    """Función principal"""
    juego = JuegoLaberinto()
    juego.ejecutar()


if __name__ == "__main__":
    main()
