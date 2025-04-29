from random import randint

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&'()*+,-./:;<=>?@[]^_{}|~`"

letters_list = list(letters)
numbers_list = list(numbers)
symbols_list = list(symbols)

def generate(length, level):
    password = ""
    if level == 0:
        for l in range(length):
            password += letters_list[randint(0, len(letters_list))]
    elif level == 1:
        for l in range(length):
            mid_list = letters_list + numbers_list
            password += mid_list[randint(0, len(mid_list))]
    elif level == 2:
        for l in range(length):
            hard_list = letters_list + numbers_list + symbols_list
            password += hard_list[randint(0, len(hard_list))]
    else:
        print("Bunday daraja yo'q!")

    return password

while 1:
    length = int(input("Parol uzunligi: "))

    print("Parol qiyinligi darajasini yozing!\n\nYordam:\n    0 - oson\n    1 - o'rta\n    2 - qiyin")
    level = int(input("Qiyinlik darajasi: "))

    print(generate(length, level))

    copy = str(input("Yuklab olish uchun  tugmasini bosing: "))