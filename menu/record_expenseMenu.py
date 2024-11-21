from logic.record_expensesLogic import save_expense
def menu1():
    valor = int(input("Ingrese el valor del gasto: "))
    categoria = str(input("Ingrese la categoria del gasto: "))
    descripcion = str(input("Ingrese la descripcion: "))
    fecha=input("Ingrese la fecha en formato YYYY-MM-DD: ")
    save_expense(descripcion, categoria, valor, fecha)


    
    


