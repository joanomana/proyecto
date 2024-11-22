import menu.record_expenseMenu as menu

while True:
    print("\nBienvenido al sistema de control de gastos")
    print("1. Registrar un gasto")
    print("2. Listar todos los gastos")
    print("3. Calcular total gastos")
    print("4. Generar reporte de gastos")
    print("5. Salir")
    opcion = int(input("Ingrese el número de la opción que desea realizar: "))

    if opcion == 1:
        menu.record_expense()
    elif opcion == 2:
        menu.list_expenses()
        pass
    elif opcion == 3:
        #menu.calculate_total_expenses()
        pass
    elif opcion == 4:
        #funcion reportes
        pass
    elif opcion == 5:
        print("Gracias por utilizar nuestro sistema de control de gastos. Adiós.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
