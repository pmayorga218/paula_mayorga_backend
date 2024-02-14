def main():
    try:
        # Solicitar al usuario que ingrese dos números
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        # Sumar los dos números
        suma = num1 + num2
        print("La suma de", num1, "y", num2, "es:", suma)
        
        # Dividir el primer número por el segundo número
        if num2 != 0:
            division = num1 / num2
            print("El resultado de dividir", num1, "por", num2, "es:", division)
        else:
            print("No se puede dividir entre cero.")
    
    except ValueError:
        print("Error: Ingresa solo números.")

if __name__ == "__main__":
    main()
