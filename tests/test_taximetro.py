# Importamos el módulo unittest para crear pruebas automáticas
import unittest

# Importamos la función que vamos a probar del módulo taximetro
from taximetro import calcular_tarifa, iniciar_trayecto, ejecutar_taximetro

class TestTaximetro(unittest.TestCase):

    # --------------------------
    # TESTS para calcular_tarifa
    # --------------------------

    def test_tarifa_movimiento(self):
        print("\n Test 1: 10s en movimiento (esperado: 0.50€)")
        resultado = calcular_tarifa(10, True)
        self.assertAlmostEqual(resultado, 0.5, places=2)

    def test_tarifa_parado(self):
        print(" Test 2: 10s parado (esperado: 0.20€)")
        resultado = calcular_tarifa(10, False)
        self.assertAlmostEqual(resultado, 0.2, places=2)

    def test_duracion_cero(self):
        print(" Test 3: Duración 0s (esperado: 0.00€)")
        resultado = calcular_tarifa(0, True)
        self.assertEqual(resultado, 0.0)

    def test_duracion_negativa(self):
        print(" Test 4: Duración negativa (esperado: 0.00€)")
        resultado = calcular_tarifa(-5, True)
        self.assertEqual(resultado, 0.0)

    def test_duracion_texto(self):
        print(" Test 5: Duración como texto (esperado: error o 0.00€)")
        try:
            resultado = calcular_tarifa("diez", True)
            self.assertEqual(resultado, 0.0)
        except Exception as e:
            print(f" Se capturó un error como se esperaba: {e}")

    def test_duracion_lista(self):
        print(" Test 6: Duración como lista (esperado: error o 0.00€)")
        try:
            resultado = calcular_tarifa([5], True)
            self.assertEqual(resultado, 0.0)
        except Exception as e:
            print(f"  Se capturó un error como se esperaba: {e}")

    # --------------------------
    # TESTS básicos de existencia
    # --------------------------

    def test_iniciar_trayecto_funcion(self):
        print("\n Test 7: Comprobando que iniciar_trayecto() existe y es ejecutable.")
        self.assertTrue(callable(iniciar_trayecto))

    def test_ejecutar_taximetro_funcion(self):
        print(" Test 8: Comprobando que ejecutar_taximetro() existe y es ejecutable.")
        self.assertTrue(callable(ejecutar_taximetro))

# Ejecutamos los tests si se lanza el archivo directamente
if __name__ == '__main__':
    print(" Ejecutando test unitarios del taxímetro...\n")
    unittest.main(verbosity=2)


