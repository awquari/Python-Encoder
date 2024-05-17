EnglishMorse = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.",
                'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..",
                'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.",
                's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-",
                'y': "-.--", 'z': "--.."}

RussianMorse = {'а': ".-", 'б': "-...", 'в': ".--", 'г': "--.", 'д': "-..", 'е': ".", 'ё': ".",
                'ж': "...-", 'з': "--..", 'и': "..", 'й': ".---", 'к': "-.-", 'л': ".-..",
                'м': "--", 'н': "-.", 'о': "---", 'п': ".--.", 'р': ".-.", 'с': "...",
                'т': "-", 'у': "..-", 'ф': "..-.", 'х': "....", 'ц': "-.-.", 'ч': "---.",
                'ш': "----", 'щ': "--.-", 'ъ': ".--.-.", 'ы': "-.--", 'ь': "-..-", 'э': "..-..",
                'ю': "..--", 'я': ".-.-"}

EnglishMorse_back = {".-": 'a', "-...": 'b', "-.-.": 'c', "-..": 'd', ".": 'e', "..-.": 'f',
                     "--.": 'g', "....": 'h', "..": 'i', ".---": 'j', "-.-": 'k', ".-..": 'l',
                     "--": 'm', "-.": 'n', "---": 'o', ".--.": 'p', "--.-": 'q', ".-.": 'r',
                     "...": 's', "-": 't', "..-": 'u', "...-": 'v', ".--": 'w', "-..-": 'x',
                     "-.--": 'y', "--..": 'z'}

RussianMorse_back = {".-": 'а', "-...": 'б', ".--": 'в', "--.": 'г', "-..": 'д', ".": 'е',
                     "...-": 'ж', "--..": 'з', "..": 'и', ".---": 'й', "-.-": 'к', ".-..": 'л',
                     "--": 'м', "-.": 'н', "---": 'о', ".--.": 'п', ".-.": 'р', "...": 'с',
                     "-": 'т', "..-": 'у', "..-.": 'ф', "....": 'х', "-.-.": 'ц', "---.": 'ч',
                     "----": 'ш', "--.-": 'щ', ".--.-.": 'ъ', "-.--": 'ы', "-..-": 'ь', "..-..": 'э',
                     "..--": 'ю', ".-.-": 'я'}

rus_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'

rus_table = [['а', 'б', 'в', 'г', 'д', 'е'],
             ['ё', 'ж', 'з', 'и', 'й', 'к'],
             ['л', 'м', 'н', 'о', 'п', 'р'],
             ['с', 'т', 'у', 'ф', 'х', 'ц'],
             ['ч', 'ш', 'щ', 'ъ', 'ы', 'ь'],
             ['э', 'ю', 'я']]

eng_table = [['a', 'b', 'c', 'd', 'e', 'f'],
             ['g', 'h', 'i', 'j', 'k', 'l'],
             ['m', 'n', 'o', 'p', 'q', 'r'],
             ['s', 't', 'u', 'v', 'w', 'x'],
             ['y', 'z']]


def code_table(word, language):
    final_word = ''
    if language == 'russian':
        table = rus_table
    else:
        table = eng_table
    for letter in word:
        line = 0
        for lines in table:
            for symbol in lines:
                if symbol == letter:
                    final_word = final_word + str(line + 1) + str(lines.index(symbol) + 1) + ' '
            line += 1
    return final_word


def decode_table(word, language):
    final_word = ''
    word = word.split()
    if language == 'russian':
        table = rus_table
    else:
        table = eng_table
    for letters in word:
        if ('7' in letters) or ('8' in letters) or ('9' in letters) or ('0' in letters) or (not letters.isnumeric()):
            break
        letter = int(letters)
        if (letter > 63) or (letter < 11) and (table == rus_table):
            break
        if (letter > 52) or (letter < 11) and (table == eng_table):
            break
        final_word = final_word + table[letter // 10 - 1][letter % 10 - 1]
    else:
        return final_word


def code_cesar(word, language):
    final_word = ''
    if language == "russian":
        for letter in word:
            new_letter_index = (rus_alphabet.find(letter) + shift) % 33
            final_word = final_word + rus_alphabet[new_letter_index]
    if language == "english":
        for letter in word:
            new_letter_index = (eng_alphabet.find(letter) + shift) % 26
            final_word = final_word + eng_alphabet[new_letter_index]
    return final_word


def decode_cesar(word, language):
    final_word = ''
    if language == "russian":
        for letter in word:
            new_letter_index = (rus_alphabet.find(letter) - shift) % 33
            final_word = final_word + rus_alphabet[new_letter_index]
    if language == "english":
        for letter in word:
            new_letter_index = (eng_alphabet.find(letter) - shift) % 26
            final_word = final_word + eng_alphabet[new_letter_index]
    return final_word


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


def code_morse(word, language):
    final_word = ''
    for letter in word:
        if language == 'russian':
            letter = RussianMorse.get(letter)
        elif language == 'english':
            letter = EnglishMorse.get(letter)
        final_word = final_word + letter + ' '
    return final_word


def decode_morse(word, language):
    final_word = ''
    letters = word.split()
    for letter in letters:

        if language == 'russian':
            letter = RussianMorse_back.get(letter)
        elif language == 'english':
            letter = EnglishMorse_back.get(letter)
        final_word += letter
    return final_word


user_choice_code = input("Выберите систему шифрования (Morse/Cesar/Table): ")
user_choice = input("Выберите действие, которое хотите произвести (code/decode): ")
user_choice_language = input("Выберите язык, с которым хотите работать (english/russian): ")

if user_choice_code == "Cesar":
    shift = int(input("Введите сдвиг по алфавиту: "))

if user_choice == "code" and user_choice_code == "Morse":
    user_word = input("Введите слово, которое хотите закодировать: ")
    if check_language(user_word) == user_choice_language:
        print("Зашифрованное слово:", code_morse(user_word, user_choice_language))
    else:
        print("Try again.")
elif user_choice == "decode" and user_choice_code == "Morse":
    user_word = input("Введите слово, которое хотите расшифровать: ")
    print("Расшифрованное слово:", decode_morse(user_word, user_choice_language))
elif user_choice == "code" and user_choice_code == "Cesar":
    user_word = input("Введите слово, которое хотите закодировать: ")
    if check_language(user_word) == user_choice_language:
        print("Зашифрованное слово:", code_cesar(user_word, user_choice_language))
    else:
        print("Try again.")
elif user_choice == "decode" and user_choice_code == "Cesar":
    user_word = input("Введите слово, которое хотите расшифровать: ")
    if check_language(user_word) == user_choice_language:
        print("Расшифрованное слово:", decode_cesar(user_word, user_choice_language))
    else:
        print("Try again.")
elif user_choice == "code" and user_choice_code == "Table":
    user_word = input("Введите слово, которое хотите зашифровать: ")
    if check_language(user_word) == user_choice_language:
        print("Зашифрованное слово:", code_table(user_word, user_choice_language))
    else:
        print("Try again.")
elif user_choice == "decode" and user_choice_code == "Table":
    user_word = input("Введите слово, которое хотите расшифровать: ")
    decode_word = decode_table(user_word, user_choice_language)
    if not decode_word:
        print("Неправильный ввод")
    else:
        print("Расшифрованное слово:", decode_word)
else:
    print("Неправильный ввод")
