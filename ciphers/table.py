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
