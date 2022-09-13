#Calculadora creada por Aliro Piña.

#Esta función suma dos valores.
def suma(x,y):
    return x + y

#Esta función resta dos valores.
def resta(x,y):
    return x - y

#Esta función multiplica dos valores.
def multiplicacion(x,y):
    return x * y

#Esta función divide dos valores.
def division(x,y):
    return x / y
    
#Este es el menú que da la bienvenida al usuario y en el cual le pregunta que operación desea realizar.
while True:
        print("*" * 39)
        print("*" * 5,"Bienvenido a mi calculadora","*" * 5)
        print("*" * 39)
        print("(1)-Suma")
        print("(2)-Resta")
        print("(3)-Multiplicación")
        print("(4)-División", "\n")

        #Aquí es donde el usuario es donde debe ingresar los valor que el escoja.
        try:
            seleccionOperatoria = input("Seleccione alguna operatoria(1,2,3,4): ")
            valor1 = float(input("Ingrese el primer valor: "))
            valor2 = float(input("Ingrese el segundo valor: "))
        except ValueError as m:
            print("Valor desconocido.")
            break

        #Aquí es donde la maquina interpreta las acciones a realizar según lo que el usuario escoja.
        if seleccionOperatoria == "1":
            print("El resultado es: ",suma(valor1,valor2))

        elif seleccionOperatoria == "2":
            print("El resultado es: ",resta(valor1,valor2))

        elif seleccionOperatoria == "3":
            print("El resultado es: ",multiplicacion(valor1,valor2))

        elif seleccionOperatoria == "4":
            print("El resultado es: ",division(valor1,valor2))
            
        #Aquí se le pregunta al usuario si es que desea realizar otra operatoria.    
        otraOperatoria = input("Le gustaría realizar otra operatoria? (si / no): ")
        if otraOperatoria == "no":
            print("Hasta luego.")
            break