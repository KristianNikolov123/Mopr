from collections import OrderedDict

def generate_matrix(key_word):
    key_word = key_word.upper()
    no_duplicates = "".join(OrderedDict.fromkeys(key_word))
    alphabet = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")
    for letter in alphabet:
        if letter not in no_duplicates:
            no_duplicates += letter
    
    matrix = [list(no_duplicates[i:i+5]) for i in range (0, 25, 5)]
    return matrix

def split_into_pairs(message):
    message = message.upper().replace(" ","").replace("J", "I")
    pairs = []
    i = 0
    while i < len(message):
        a = message[i]
        if i + 1 == len(message):
            pairs.append(a + "X")
            i += 1
        else:
            b = message[i + 1]
            if a == b:
                pairs.append(a + "X")
                i += 1
            else:
                pairs.append(a + b)
                i += 2
    return pairs

def find_position(matrix, letter):
    for row_idx, row in enumerate(matrix):
        if letter in row:
            return row_idx, row.index(letter)
    return None

def encrypt_pair(matrix, pair):
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])

    if row1 == row2:
        encrypted = matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        encrypted = matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        encrypted = matrix[row1][col2] + matrix[row2][col1]

    return encrypted


def encrypt_playfair(plaintext, key_word):
    matrix = generate_matrix(key_word)
    pairs = split_into_pairs(plaintext)
    cyphertext = ""

    for pair in pairs:
        cyphertext += encrypt_pair(matrix, pair)

    return cyphertext

key_word = "keyword"
plaintext = "SECRET MESSAGE"
cyphertext = encrypt_playfair(plaintext, key_word)
print(cyphertext)


def decrypt_pair(matrix, pair):
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])

    if row1 == row2:
        decrypted = matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        decrypted = matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else: 
        decrypted = matrix[row1][col2] + matrix[row2][col1]

    return decrypted

def decrypt_playfair(cyphertext, key_word):
    matrix = generate_matrix(key_word)
    pairs = [cyphertext[i:i+2] for i in range(0, len(cyphertext), 2)]
    plaintext = ""

    for pair in pairs:
        plaintext += decrypt_pair(matrix, pair)

    return plaintext

key_word = "keyword"
cyphertext = "NORDKUNKQZPCND"
plaintext = decrypt_playfair(cyphertext, key_word)
print(plaintext)