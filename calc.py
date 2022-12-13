while True:
    command = input("Выберите операцию: ")
    if command in "+-*/":
        break
    print("Ошибка: такой операции не существует. Попробуйте ещё раз.")

one = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))

result = 0
if command == "+":
    result = first + second
elif command == "-":
    result = first - second
elif command == "*":
    result = first * second
elif command == "/":
    result = first / second

print(f"{first} {command} {second} = {result}")