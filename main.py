def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        number = int(input("Введіть число для обчислення факторіалу: "))
        if number < 0:
            print("Факторіал не визначений для від'ємних чисел.")
        else:
            print(f"Факторіал числа {number} дорівнює {factorial(number)}")
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")
