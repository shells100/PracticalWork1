print("Арифметический (1)")
print("Логический (2)")
print("Побитовый (3)")

try:
    calculator = int(input("Выберите тип калькулятора: "))
except ValueError:
    print("Неизвестное значение")
    exit()

if calculator == 1:

    try:
        num1 = int(input("Введите число 1: "))
        num2 = int(input("Введите число 2: "))
    except ValueError:
        print("Неизвестное значение")
        exit()
    
    print("Сложение (1)")
    print("Вычитание (2)")
    print("Умножение (3)")
    print("Деление (4)")
    print("Целочисленное деление (5)")
    print("Остаток от деления (6)")
    print("Возведение в степень (7)")
    
    try:
        operation = int(input("Введите номер операции: "))
    except ValueError:
        print("Неизвестное значение")
        exit()

    if operation == 1:
        print(num1 + num2)
    
    elif operation == 2:
        print(num1 - num2)
    
    elif operation == 3:
        print(num1 * num2)
    
    elif operation == 4:
        if num2 == 0:
            print("Делить на ноль нельзя")
        else:
            print(num1 / num2)
    
    elif operation == 5:
        if num2 == 0:
            print("Делить на ноль нельзя")
        else:
            print(num1 // num2)
    
    elif operation == 6:
        if num2 == 0:
            print("Делить на ноль нельзя")
        else:
            print(num1 % num2)
    
    elif operation == 7:
        if num1 != 0 and num2 == 0:
            print("1")
        elif num1 == 0 and num2 == 0:
            print("Не имеет смысла в математике")
        else:
            print(num1 ** num2)
    
    else:
        print("Неизвестное значение")
    
elif calculator == 2:
    
    print("Логическое И (1)")
    print("Логическое ИЛИ (2)")
    print("Логическое НЕ (3)")

    try:
        operation = int(input("Введите номер операции: "))
    except ValueError:
        print("Неизвестное значение")
        exit()

    if operation == 3:
        try:
            num = int(input("Введите число: "))
        except ValueError:
            print("Неизвестное значение")
            exit()

        print(not bool(num))
    
    elif operation == 1 or operation == 2:
        try:
            num1 = int(input("Введите число 1: "))
            num2 = int(input("Введите число 2: "))
        except ValueError:
            print("Неизвестное значение")
            exit()

        if operation == 1:
            print(bool(num1) and bool(num2))
        
        elif operation == 2:
            print(bool(num1) or bool(num2))
        
        else:
            print("Неизвестное значение")
    
    else:
        print("Неизвестное значение")

elif calculator == 3:
    
    print("Побитовое И (1)")
    print("Побитовое ИЛИ (2)")
    print("Побитовое исключающее ИЛИ (3)")
    print("Побитовое НЕ (4)")
    print("Побитовый сдвиг влево (5)")
    print("Побитовый сдвиг вправо (6)")

    try:
        operation = int(input("Введите номер операции: "))
    except ValueError:
        print("Неизвестное значение")
    
    if operation == 4:
        try:
            num = int(input("Введите число: "))
        except ValueError:
            print("Неизвестное значение")

        print(~ num)

    elif operation != 4 and operation in [1, 2, 3, 4, 5, 6]:
        try:
            num1 = int(input("Введите число 1: "))
            num2 = int(input("Введите число 2: "))
        except ValueError:
            print("Неизвестное значение")
            exit()
            
        if operation == 1:
            print(num1 & num2)
        
        elif operation == 2:
            print(num1 | num2)
        
        elif operation == 3:
            print(num1 ^ num2)
        
        elif operation == 5:
            print(num1 << num2)
        
        elif operation == 6:
            print(num1 >> num2)
        
        else:
            print("Неизвестное значение")
    
    else:
        print("Неизвестное значение")

else:
    print("Неизвестное значение")