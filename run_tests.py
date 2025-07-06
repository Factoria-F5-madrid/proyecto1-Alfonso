import unittest

print("\n🔍 Ejecutando tests unitarios del proyecto Taxímetro Digital...")
print("------------------------------------------------------------\n")

# Carga todos los tests desde el directorio 'tests'
loader = unittest.TestLoader()
suite = loader.discover('tests')

# Ejecuta los tests con mayor nivel de detalle
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

print("\n✅ Todos los tests han sido ejecutados.")
if result.wasSuccessful():
    print("🎉 Resultado: Todos los tests pasaron correctamente.")
else:
    print("❌ Resultado: Algunos tests fallaron. Revisa los errores arriba.")
