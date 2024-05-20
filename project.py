from ciphers.table import *
from ciphers.morse import *
from ciphers.cesar import *


def check_language(word):
    is_rus = True
    for letter in word:
        if letter not in rus_alphabet:
            is_rus = False
            break
    if is_rus:
        return "russian"
    is_eng = True
    for letter in word:
        if letter not in eng_alphabet:
            is_eng = False
            break
    if is_eng:
        return "english"
    return "invalid language"

user_continue = "continue"

while user_continue == "continue":
    user_choice_code = input("Выберите систему шифрования (Morse/Cesar/Table): ")
    user_choice = input("Выберите действие, которое хотите произвести (code/decode): ")
    user_choice_language = input("Выберите язык, с которым хотите работать (english/russian): ")
    if user_choice == "code":
        if not user_choice_code == "Cesar":
            user_word = input("Введите слово, которое хотите закодировать: ")
        if user_choice_code == "Morse":
            if check_language(user_word) == user_choice_language:
                print("Зашифрованное слово:", code_morse(user_word, user_choice_language))
            else:
                print("Неправильный ввод")
        if user_choice_code == "Cesar":
            shift = int(input("Введите сдвиг по алфавиту: "))
            user_word = input("Введите слово, которое хотите закодировать: ")
            if check_language(user_word) == user_choice_language:
                print("Зашифрованное слово:", code_cesar(user_word, user_choice_language, shift))
            else:
                print("Неправильный ввод")
        if user_choice_code == "Table":
            if check_language(user_word) == user_choice_language:
                print("Зашифрованное слово:", code_table(user_word, user_choice_language))
            else:
                print("Неправильный ввод")
    elif user_choice == "decode":
        if not user_choice_code == "Cesar":
            user_word = input("Введите слово, которое хотите расшифровать: ")
        if user_choice_code == "Morse":
            print("Расшифрованное слово:", decode_morse(user_word, user_choice_language))
        if user_choice_code == "Cesar":
            shift = int(input("Введите сдвиг по алфавиту: "))
            user_word = input("Введите слово, которое хотите расшифровать: ")
            if check_language(user_word) == user_choice_language:
                print("Расшифрованное слово:", decode_cesar(user_word, user_choice_language, shift))
            else:
                print("Неправильный ввод")
        if user_choice_code == "Table":
            decode_word = decode_table(user_word, user_choice_language)
            if not decode_word:
                print("Неправильный ввод")
            else:
                print("Расшифрованное слово:", decode_word)
    else:
        print("Неправильный ввод")
    user_continue = input("Следующее действие (continue/exit): ")
    print("\n=<3==========================\n")