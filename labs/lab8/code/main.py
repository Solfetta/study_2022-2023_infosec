def toBinary(a):
    a = " ".join(reversed([i + j for i, j in zip(*[["{0:04b}".format(int(c, 16)) for c in reversed("0" + a)][n::2] for n in [1, 0]])]))
    return a


def encryption(P, K):
    hex_P = P.encode('utf-8').hex()
    bin_P = toBinary(hex_P)
    hex_K = K.replace(' ', '').lower()
    bin_K = toBinary(hex_K)

    bin_C = ""
    if len(bin_P) == len(bin_K):
        for i in range(len(bin_P)):
            if bin_P[i] == ' ':
                bin_C += ' '
            elif bin_P[i] == bin_K[i]:
                bin_C += '0'
            elif bin_P[i] != bin_K[i]:
                bin_C += '1'
    bin_C = bin_C.split()
    C = ''
    for i in range(len(bin_C)):
        x = int(bin_C[i], 2)
        if len(hex(x)[2:]) < 2:
            C += '0'
        C += hex(x)[2:]
        C += ' '

    C = C.upper()
    return C


def decryption(C1, C2, P1):
    hex_C1 = C1.replace(' ', '').lower()
    bin_C1 = toBinary(hex_C1)
    hex_C2 = C2.replace(' ', '').lower()
    bin_C2 = toBinary(hex_C2)
    hex_P1 = P1.encode('utf-8').hex()
    bin_P1 = toBinary(hex_P1)
    bin_P2 = ''
    for i in range(len(bin_P1)):
        if bin_P1[i] == ' ':
            bin_P2 += ' '
        else:
            bin_P2 += str(int(bin_C1[i]) ^ int(bin_C2[i]) ^ int(bin_P1[i]))

    bin_P2 = bin_P2.split()
    P2 = ''
    for i in range(len(bin_P2)):
        x = int(bin_P2[i], 2)
        if len(hex(x)[2:]) < 2:
            P2 += '0'
        P2 += hex(x)[2:]
        P2 += ''
    P2 = bytes.fromhex(P2).decode("ASCII")
    return P2


P1 = 'NaVahishodahiiot1204'
P2 = 'VSevernyifilialBanka'
key = "05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 0B B2 70 54"

print("Выражение 1:", P1)
print("Выражение 2:", P2)
print("Ключ:", key)
print()
C1 = encryption(P1, key)
C2 = encryption(P2, key)
print("Шифротекст 1:", C1)
print("Шифротекст 2:", C2)
print()
print("Расшифрованное выражение 2:", decryption(C1, C2, P1))