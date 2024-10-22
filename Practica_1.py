def sumar_numeros():
    num1 = 5
    num2 = 12
    
    # Verificar si alguno de los números es nulo
    if num1 is None or num2 is None:
        print("Los nulos no son permitidos")
    else:
        # Sumar los números si no son nulos
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")

