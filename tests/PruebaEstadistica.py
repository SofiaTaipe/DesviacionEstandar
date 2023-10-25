import unittest
from src.logica.Estadistica import Estadistica, ExceptionDatos

class PruebaEstadistica(unittest.TestCase):
    def setUp(self):
        self.estadistica = Estadistica([])

    def tearDown(self):
        self.estadistica = None

    def test_media_listaVacia_retornaExcepcion(self):
        self.estadistica.numeros = []
        with self.assertRaises(ExceptionDatos):
            self.estadistica.media()

    def test_media_unDato_retornaMedia(self):
        # Arrange
        self.estadistica.numeros = [3.5]
        resultadoEsperado = 3.500

        # Do
        resultadoActual = self.estadistica.media()

        # Assert
        self.assertAlmostEqual(resultadoEsperado, resultadoActual, 3)

    def test_media_noNumero_retornaExcepcion(self):
        self.estadistica.numeros = [8, "a"]
        with self.assertRaises(ExceptionDatos):
            self.estadistica.media()

# Casos de prueba
    def test_DesviacionEstandar_DatosIguales_retornaDesviacionEStandar(self):
        # Arrange
        self.estadistica.numeros = [5, 5, 5, 5, 5]
        resultadoEsperado = 0.000

        # Do
        resultadoActual = self.estadistica.DesviacionEstandar()

        # Assert
        self.assertAlmostEqual(resultadoEsperado, resultadoActual, 3)

    def test_DesviacionEstandar_diferentesDatos_retornaDesviacionEStandar(self):
        # Arrange
        self.estadistica.numeros = [1, 2, 3, 4, 5]
        resultadoEsperado = 1.58

        # Do
        resultadoActual = self.estadistica.DesviacionEstandar()

        # Assert
        self.assertAlmostEqual(resultadoEsperado, resultadoActual, 2)

    def test_DesviacionEstandar_unDato_retornaDesviacionEStandar(self):
        # Arrange
        self.estadistica.numeros = [1]
        resultadoEsperado = 0.000

        # Do
        resultadoActual = self.estadistica.DesviacionEstandar()

        # Assert
        self.assertAlmostEqual(resultadoEsperado, resultadoActual, 3)


