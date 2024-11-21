import json
def save_expense(descripcion,categoria,valor,fecha):
    route = "database/expense_system.json"
    with open (route,"r")as file:
        data = json.load(file)
        gasto ={
            "Descripcion":descripcion,
            "Categoria":categoria,
            "Valor":valor,
            "Fecha":fecha
        }
        data.append(gasto)
    with open (route,"w") as file:
        json.dump(data,file,indent=4)


