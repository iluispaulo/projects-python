def simple_block_encrypt(plaintext, key):
    texto_criptografado = ''
    for char in plaintext:
       texto_criptografado += key.get(char, char)
    return texto_criptografado

def simple_block_decrypt(ciphertext, key):
    texto_descriptografado = ''
    for char in ciphertext:
        texto_descriptografado += key.get(char, char)
    return texto_descriptografado

# Solicita a entrada do usuário
plaintext = input("Digite a mensagem: ")
key = 'zyxwvutsrqponmlkjihgfedcba'

# Verifica se a chave tem 26 caracteres
if len(key) != 26:
    print("A chave de substituição deve ter exatamente 26 caracteres.")
    exit()

# Cria o dicionário de substituição a partir da chave
key_dict = {chr(97+i): key[i] for i in range(26)}

# Criptografa a mensagem
texto_criptografado = simple_block_encrypt(plaintext, key_dict)
print("Texto criptografado:", texto_criptografado)

# Descriptografa a mensagem
texto_descriptografado = simple_block_decrypt(texto_criptografado, {v: k for k, v in key_dict.items()})
print("Texto descriptografado:", texto_descriptografado)

