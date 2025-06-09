import string

def generate_vigenere_matrix():
    alphabet = list(string.ascii_uppercase)
    matrix = []

    for i in alphabet:
        matrix.append("".join(alphabet))
        alphabet.append(alphabet.pop(0))
    return matrix

def vigenere_encrypter(plain_text, key):
    result = []
    matrix = generate_vigenere_matrix()
    alphabet = string.ascii_uppercase
    key = key.upper().replace(" ", "")
    key_index = 0
    
    for ch in plain_text:
        if ch.upper() in alphabet:
            row = ord(key[key_index % len(key)]) - ord('A')
            col = ord(ch.upper()) - ord('A')
            encrypted = matrix[row][col]
            result.append(encrypted if ch.isupper() else encrypted.lower())
            key_index += 1
        else:
            result.append(ch)
    return "".join(result)

plain_text = "HELLO WORLD"
cypher = vigenere_encrypter(plain_text, "LEMON")
print(cypher)

def vigenere_decrypter(plain_text, key):
    result = []
    matrix = generate_vigenere_matrix()
    alphabet = string.ascii_uppercase
    key = key.upper().replace(" ", "")
    key_index = 0
    
    for ch in plain_text:
        if ch.upper() in alphabet:
            row = ord(key[key_index % len(key)]) - ord('A')
            col = matrix[row].index(ch.upper())
            decrypted = alphabet[col]
            result.append(decrypted if ch.isupper() else decrypted.lower())
            key_index += 1
        else:
            result.append(ch)
    return "".join(result)

cypher = "SIXZB HSDZQ"
decypher = vigenere_decrypter(cypher, "LEMON")
print(decypher)