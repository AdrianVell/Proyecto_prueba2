from Practica_1 import sumar_numeros

def test_suma_numeros(capsys):
    # Ejecutar la función que suma 5 y 12
    sumar_numeros()
    # Capturar la salida impresa por la función
    captured = capsys.readouterr()
    # Aserción de igualdad (verifica si la salida es correcta)
    assert captured.out == "La suma de 5 y 12 es: 17\n"
    # Aserción de desigualdad (verifica que el resultado no sea incorrecto)
    assert captured.out != "La suma de 5 y 12 es: 20\n"
    # Aserción de verdad (verifica si se imprimió algo no vacío)
    assert bool(captured.out) == True  # Verifica que la salida no esté vacía
    # Aserción de no nulo (verifica que el resultado no sea nulo)
    assert captured.out is not None
def test_suma_verdadera():
    # Verificar que la suma de 5 y 12 sea correcta sin usar la salida de impresión
    resultado = 5 + 12
    # Aserción de igualdad (verifica que la suma es correcta)
    assert resultado == 17
    # Aserción de verdad (verifica si el resultado es verdadero)
    assert resultado
    # Aserción de desigualdad (verifica que la suma no es incorrecta)
    assert resultado != 20
    # Aserción de no nulo (verifica que el resultado no es nulo)
    assert resultado is not None
