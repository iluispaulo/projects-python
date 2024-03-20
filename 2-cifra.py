def simple_substitution_encrypt(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            encrypted_text += key[index].upper() if char.isupper() else key[index]
        else:
            encrypted_text += char
    return encrypted_text

def simple_substitution_decrypt(encrypted_text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_text = ''
    for char in encrypted_text:
        if char.lower() in key:
            index = key.index(char.lower())
            decrypted_text += alphabet[index].upper() if char.isupper() else alphabet[index]
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
key = 'zyxwvutsrqponmlkjihgfedcba'  # Example key, reverse alphabet
plaintext = input("Digite uma mensagem: ")
encrypted_text = simple_substitution_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = simple_substitution_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)

 