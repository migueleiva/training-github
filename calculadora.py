# Función para sumar dos números
def sumar(x, y):
    return x + y

# Función para restar dos números
def restar(x, y):
    return x - y

# Función para multiplicar dos números
def multiplicar(x, y):
    return x * y

# Función para dividir dos números
def dividir(x, y):
    if y == 0:
        return "División por cero no permitida"
    return x / y

# Función principal de la calculadora
def calculadora():
    print("Selecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        # Obtener la entrada del usuario
        opcion = input("Ingresa una opción (1/2/3/4): ")

        # Verificar si la opción es válida
        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            elif opcion == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")

            # Preguntar si el usuario quiere realizar otra operación
            siguiente = input("¿Quieres realizar otra operación? (s/n): ")
            if siguiente.lower() != 's':
                break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

# Ejecutar la calculadora
calculadora()
