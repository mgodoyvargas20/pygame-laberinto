#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias para el juego de laberinto
"""

import unittest
import sys
import os

# Configurar el entorno para pruebas sin display
# SDL_VIDEODRIVER y SDL_AUDIODRIVER en modo 'dummy' permiten ejecutar
# Pygame en entornos sin interfaz gráfica (headless) como servidores CI/CD
os.environ['SDL_VIDEODRIVER'] = 'dummy'
os.environ['SDL_AUDIODRIVER'] = 'dummy'

# Importar después de configurar el entorno
import pygame
from main import (
    Jugador, BotonTactil, LABERINTO, JUGADOR_INICIO,
    BLANCO, NEGRO, AZUL
)


class TestJugador(unittest.TestCase):
    """Pruebas para la clase Jugador"""
    
    def setUp(self):
        """Configuración antes de cada prueba"""
        self.jugador = Jugador(*JUGADOR_INICIO)
    
    def test_posicion_inicial(self):
        """Verifica que el jugador inicie en la posición correcta"""
        self.assertEqual(self.jugador.x, JUGADOR_INICIO[0])
        self.assertEqual(self.jugador.y, JUGADOR_INICIO[1])
    
    def test_movimiento_valido(self):
        """Verifica que el jugador se mueva correctamente en caminos válidos"""
        pos_inicial_x = self.jugador.x
        pos_inicial_y = self.jugador.y
        
        # Mover hacia la derecha (debe ser un camino válido)
        victoria = self.jugador.mover(1, 0, LABERINTO)
        
        # El jugador debe haberse movido
        self.assertEqual(self.jugador.x, pos_inicial_x + 1)
        self.assertEqual(self.jugador.y, pos_inicial_y)
        self.assertFalse(victoria)  # No debe haber llegado a la meta
    
    def test_movimiento_bloqueado_por_pared(self):
        """Verifica que el jugador no pueda atravesar paredes"""
        # Mover hacia arriba (debe ser una pared)
        pos_inicial_x = self.jugador.x
        pos_inicial_y = self.jugador.y
        
        self.jugador.mover(0, -1, LABERINTO)
        
        # El jugador NO debe haberse movido
        self.assertEqual(self.jugador.x, pos_inicial_x)
        self.assertEqual(self.jugador.y, pos_inicial_y)
    
    def test_movimiento_fuera_de_limites(self):
        """Verifica que el jugador no pueda salir del laberinto"""
        # Intentar mover fuera de los límites
        jugador_esquina = Jugador(0, 0)
        pos_inicial_x = jugador_esquina.x
        pos_inicial_y = jugador_esquina.y
        
        jugador_esquina.mover(-1, 0, LABERINTO)  # Izquierda fuera de límites
        
        # El jugador NO debe haberse movido
        self.assertEqual(jugador_esquina.x, pos_inicial_x)
        self.assertEqual(jugador_esquina.y, pos_inicial_y)
    
    def test_detectar_victoria(self):
        """Verifica que se detecte cuando el jugador llega a la salida"""
        # Colocar jugador cerca de la salida (posición 8, 8)
        jugador_cerca = Jugador(8, 8)
        
        # Mover hacia la salida (posición 9, 8)
        victoria = jugador_cerca.mover(1, 0, LABERINTO)
        
        # Debe detectar victoria
        self.assertTrue(victoria)


class TestBotonTactil(unittest.TestCase):
    """Pruebas para la clase BotonTactil"""
    
    def setUp(self):
        """Configuración antes de cada prueba"""
        pygame.init()
        self.boton = BotonTactil(100, 100, 50, 50, "↑", (0, -1))
    
    def test_creacion_boton(self):
        """Verifica que el botón se cree correctamente"""
        self.assertEqual(self.boton.texto, "↑")
        self.assertEqual(self.boton.direccion, (0, -1))
        self.assertFalse(self.boton.presionado)
    
    def test_verificar_click_dentro(self):
        """Verifica que se detecte un click dentro del botón"""
        # Click en el centro del botón
        click_detectado = self.boton.verificar_click((125, 125))
        self.assertTrue(click_detectado)
    
    def test_verificar_click_fuera(self):
        """Verifica que no se detecte un click fuera del botón"""
        # Click fuera del botón
        click_detectado = self.boton.verificar_click((200, 200))
        self.assertFalse(click_detectado)


class TestLaberinto(unittest.TestCase):
    """Pruebas para la estructura del laberinto"""
    
    def test_laberinto_rectangular(self):
        """Verifica que el laberinto sea rectangular"""
        filas = len(LABERINTO)
        self.assertGreater(filas, 0)
        
        # Todas las filas deben tener la misma longitud
        columnas = len(LABERINTO[0])
        for fila in LABERINTO:
            self.assertEqual(len(fila), columnas)
    
    def test_laberinto_tiene_paredes(self):
        """Verifica que el laberinto tenga paredes (valor 1)"""
        tiene_paredes = any(1 in fila for fila in LABERINTO)
        self.assertTrue(tiene_paredes)
    
    def test_laberinto_tiene_caminos(self):
        """Verifica que el laberinto tenga caminos (valor 0)"""
        tiene_caminos = any(0 in fila for fila in LABERINTO)
        self.assertTrue(tiene_caminos)
    
    def test_laberinto_tiene_salida(self):
        """Verifica que el laberinto tenga una salida (valor 2)"""
        tiene_salida = any(2 in fila for fila in LABERINTO)
        self.assertTrue(tiene_salida)
    
    def test_posicion_inicial_es_camino(self):
        """Verifica que la posición inicial del jugador sea un camino válido"""
        x, y = JUGADOR_INICIO
        self.assertEqual(LABERINTO[y][x], 0, 
                        "La posición inicial debe ser un camino (0)")


def run_tests():
    """Ejecuta todas las pruebas"""
    # Crear suite de pruebas
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Añadir todas las pruebas
    suite.addTests(loader.loadTestsFromTestCase(TestJugador))
    suite.addTests(loader.loadTestsFromTestCase(TestBotonTactil))
    suite.addTests(loader.loadTestsFromTestCase(TestLaberinto))
    
    # Ejecutar pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Retornar código de salida
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_tests())
