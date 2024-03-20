def vigenere_encrypt(plaintext, key):
    ciphertext = ''
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ''
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += char
    return plaintext

# Solicita a entrada do usuário
plaintext = input("Digite a mensagem: ")
key = input("Digite a chave: ")

# Criptografa a mensagem
encrypted_text = vigenere_encrypt(plaintext, key)
print("Texto criptografado:", encrypted_text)

# Descriptografa a mensagem
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Texto descriptografado:", decrypted_text)
