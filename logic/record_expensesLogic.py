import json
def save_expense(valor,fecha,categoria,descripcion1):
    route = "database/expense_system.json"
    with open (route,"r")as file:
        data = json.load(file)
        gasto ={
            "Valor":valor,
            "Fecha":fecha,
            "Categoria":categoria,
            "Descripcion":descripcion1
        }
        data.append(gasto)
    with open (route,"w") as file:
        json.dump(data,file,indent=4)
    print("Gasto registrado exitosamente.")

def read_expense():
    route = "database/expense_system.json"
    with open (route,"r")as file:
        data = json.load(file)
    return data


def list_all_expenses():
    expenses = read_expense()
    print("Expenses:")
    for expense in expenses:
        print(f"Descripcion: {expense['Descripcion']}, Categoria: {expense['Categoria']}, Valor: {expense['Valor']}, Fecha: {expense['Fecha']}")

def search_by_category(categoria):
    filtered_expenses = [expense for expense in read_expense() if expense["Categoria"] == categoria]
    if len(filtered_expenses) == 0:
        print("No hay gastos en esta categoría.")
    else:
        print("Expenses de la categoría seleccionada:")
        for expense in filtered_expenses:
            print(f"Descripcion: {expense['Descripcion']}, Categoria: {expense['Categoria']}, Valor: {expense['Valor']}, Fecha: {expense['Fecha']}")


def calculate_total_expenses():
    expenses = read_expense()
    total = sum(expense['Valor'] for expense in expenses)
    print(f"EL total de gastos registrados es: {total}")




