modo_encriptar = 1
modo_decriptar = 0

def caesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVXYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == modo_encriptar else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data

# Tests
key = 5
original = input("Digite uma mensagem: ")
print('  Original:', original)
ciphered = caesar(original, key, modo_encriptar)
print('Encriptada:', ciphered)
plain = caesar(ciphered, key, modo_decriptar)
print('Decriptada:', plain)