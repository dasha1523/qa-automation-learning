while True:
    user_input = input('Введите число или "exit" для завершения программы')

    if user_input.lower() == "exit":
        print ("До скорых встреч!")
        break

    try:
        number = int(user_input)
        if number % 2 == 0:
            print("Четное")
        if number % 2 == 1:
            print("Нечетное")

    except ValueError:
        print("Это не число! Попробуйте снова")
