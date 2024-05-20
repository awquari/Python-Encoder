rus_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'

def code_cesar(word, language, shift):
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


def decode_cesar(word, language, shift):
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
