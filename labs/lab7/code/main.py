def toBinary(a):
    a = " ".join(reversed([i + j for i, j in zip(*[["{0:04b}".format(int(c, 16)) for c in reversed("0" + a)][n::2] for n in [1, 0]])]))
    return a


phrase = 'Штирлиц  –  Вы Герой!!!'
key = '05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 0B B2 70 54 05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 B0 D2 94'
res = 'С Новым Годом, друзья!'


def encryption(phrase, key):
    hex_phrase = phrase.encode('utf-8').hex()
    bin_phrase = toBinary(hex_phrase)

    hex_key = key.replace(' ', '').lower()
    bin_key = toBinary(hex_key)

    bin_cipher = ""
    if len(bin_phrase) == len(bin_key):
        for i in range(len(bin_phrase)):
            if bin_phrase[i] == ' ':
                bin_cipher += ' '
            elif bin_phrase[i] == bin_key[i]:
                bin_cipher += '0'
            elif bin_phrase[i] != bin_key[i]:
                bin_cipher += '1'

    bin_cipher = bin_cipher.split()
    cipher = ''
    for i in range(len(bin_cipher)):
        x = int(bin_cipher[i], 2)
        cipher += hex(x)[2:]
        cipher += ' '

    cipher = cipher.upper()
    return cipher


def get_key(cipher, res):
    hex_cipher = cipher.replace(' ', '').lower()
    bin_cipher = toBinary(hex_cipher)

    hex_res = res.encode('utf-8').hex()
    bin_res = toBinary(hex_res)

    bin_key = ''
    if len(bin_cipher) == len(bin_res):
        for i in range(len(bin_cipher)):
            if bin_cipher[i] == ' ':
                bin_key += ' '
            elif bin_cipher[i] == bin_res[i]:
                bin_key += '0'
            elif bin_cipher[i] != bin_res[i]:
                bin_key += '1'

    bin_key = bin_key.split()
    hex_key = ''
    for i in range(len(bin_key)):
        x = int(bin_key[i], 2)
        if len(hex(x)[2:]) < 2:
            hex_key += '0'
        hex_key += hex(x)[2:]
        hex_key += ' '
    return hex_key


phrase = 'Штирлиц  –  Вы Герой!!!'
key = '05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 0B B2 70 54 05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 B0 D2 94'
res = 'С Новым Годом, друзья!'


print('Шифрослово: ', encryption(phrase, key))
print('Ключ: ', get_key(encryption(phrase, key), res))


