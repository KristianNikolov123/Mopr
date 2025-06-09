plain_text = "Hello world"
def caeser_encrypter(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base) 
        else:
            result += char
    return result

print(caeser_encrypter(plain_text, 3))  

encrypted_text = "Khoor zruog"
def caeser_decrypter(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - key) % 26 + base)
        else:
            result += char
    return result

print(caeser_decrypter(encrypted_text, 3))  