from prettytable import PrettyTable
mytable = PrettyTable()

mytable.field_names = ["Имя", "Вік", "Хоби"]

mytable.add_row(["Ніка", 12, "Психологія"])
mytable.add_row(["Лера", 5,"Ноут" ])
mytable.add_row(["Дед Максим", 112, "Дивитися TV"])

print(mytable)