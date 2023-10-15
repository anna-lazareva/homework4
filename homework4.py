prefix = input("Введите серию паспорта: ")
if len(prefix) != 4:
    print("серию не корректна")
    exit()
for char in prefix:
    if not char.isdigit():
        print("серию не корректна")
        exit()
print("серия корректна")

prefix = input("Введите номер паспорта: ")
if len(prefix) != 6:
    print("номер не корректен")
    exit()
for char in prefix:
    if not char.isdigit():
        print("номер не корректен")
        exit()
print("номер корректен")


