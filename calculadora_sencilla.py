number1=int(input("Ingresa el primer numero: "))
number2=int(input("Ingresa el segundo numero: "))

eleccion = 0

while eleccion != 6:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. reingresar valores")
    print("6. reingresar valores")

    eleccion=int(input("Elige una opcion: "))
    
    if eleccion == 1:
        print("\nLa suma de los dos numeros es: ", number1 + number2)
    elif eleccion == 2:
        print("\nLa resta de los dos numeros es: ", number1 - number2)
    elif eleccion == 3:
            print("\nLa multiplicacion de los dos numeros es: ", number1 * number2)
    elif eleccion == 4:
        print("\nLa division de los dos numeros es: ", number1 / number2)
    elif eleccion == 5:
        number1=int(input("Ingresa el primer numero: "))
        number2=int(input("Ingresa el segundo numero: "))
        print("Gracias por usar el calculadora")
    elif eleccion == 6:
        print("Gracias por usar el calculadora")
        exit
    else:
        print("Eleccion incorrecta")



