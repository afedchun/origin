def guess_the_number():
    """
    Реалізує гру "Вгадай число".
    Програма випадковим чином обирає ціле число, а гравець має обмежену кількість спроб,
    щоб його вгадати, отримуючи підказки після кожної спроби.
    """
    min_num = 1
    max_num = 100
    max_attempts = 7

    secret_number = random.randint(min_num, max_num)
    print(f"Привіт! Я загадав ціле число від {min_num} до {max_num}.")
    print(f"У тебе є {max_attempts} спроб, щоб його вгадати.")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Спроба {attempt}/{max_attempts}. Введи своє число: "))
        except ValueError:
            print("Будь ласка, введи ціле число.")
            continue

        if guess < min_num or guess > max_num:
            print(f"Твоє число має бути в діапазоні від {min_num} до {max_num}.")
            continue

        if guess < secret_number:
            print("Занадто маленьке.")
        elif guess > secret_number:
            print("Занадто велике.")
        else:
            print(f"Вітаємо! Ти вгадав число {secret_number} за {attempt} спроб!")
            return

    print(f"\nНа жаль, у тебе закінчилися спроби.")
    print(f"Загадане число було: {secret_number}.")
    print("Спробуй ще раз!")

if __name__ == "__main__":
    guess_the_number()
