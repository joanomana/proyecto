import logic.record_expensesLogic as logic
import json
def record_expense():
    print("""
        =============================================
                  Registrar Nuevo Gasto
        =============================================
        Ingrese la información del gasto:
""")
    valor = int(input("Monto del gasto: "))
    
    fecha=str(input("Ingrese la fecha en formato YYYY-MM-DD: "))
    route ="database/expense_system.json"
    with open (route,"r")as file:
        data = json.load(file)
    categorias = [item["Categoria"] for item in data]
    print("Categorias disponibles:")
    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categorias}")
    categoria = str(input("Categoria del gasto: ")).capitalize()
    descripcion = str(input("Descripcion (opcional): "))
    if descripcion == "":
        descripcion1 = "Nada"
    else:
        descripcion1 = descripcion.capitalize()
    print("""  
        =============================================      
        Ingrese 'S' para guardar o 'C' para cancelar.
        =============================================""")
    option = str(input("")).upper()
    if option == 'S':
        logic.save_expense(valor,fecha,categoria,descripcion1)
    elif option == 'C':
        print("Operación cancelada.")
        return
    else:
        print("Opción inválida. Intente nuevamente.")
        record_expense()

def list_expenses():
    while True:
        print("""
=============================================
                Listar Gastos
=============================================
Seleccione una opción para filtrar los gastos:

1. Ver todos los gastos
2. Filtrar por categoría
3. Filtrar por rango de fechas
4. Regresar al menú principal
=============================================
""")
        option = int(input("Ingrese la opción: "))
        if option == 1:
            print("Expenses:")
            logic.list_all_expenses()
        elif option == 2:
            categorias = [item["Categoria"] for item in logic.read_expense()]
            print("Categorias disponibles:")
            for i, categoria in enumerate(categorias, start=1):
                print(f"{i}. {categorias}")
            categoria = str(input("Ingrese la categoría deseada: ")).capitalize()
            logic.search_by_category(categoria)
            