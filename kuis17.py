user_word = input("Masukkan kata: ")
user_word = user_word.upper()

for huruf in user_word:
    if huruf == 'A' or huruf == 'I' or huruf == 'U' or huruf == 'E' or huruf == 'O':
        continue
    elif huruf != ' ':
        print(huruf, end=' ')
    else:
        continue