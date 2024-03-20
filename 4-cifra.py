def transpose_encrypt(plaintext, key):
    # Calcula o número de colunas
    num_columns = len(key)
    # Calcula o número de linhas necessário para a matriz
    num_rows = (len(plaintext) + num_columns - 1) // num_columns
    # Preenche o texto com espaços em branco para preencher a matriz
    plaintext += ' ' * (num_rows * num_columns - len(plaintext))
    # Inicializa a matriz vazia
    matrix = [[''] * num_columns for _ in range(num_rows)]
    # Preenche a matriz com os caracteres do texto
    for i, char in enumerate(plaintext):
        row = i // num_columns
        col = i % num_columns
        matrix[row][col] = char
    # Constrói o texto cifrado lendo a matriz de acordo com a chave
    encrypted_text = ''
    for col in key:
        col_index = int(col) - 1
        if col_index < num_columns:
            for row in range(num_rows):
                encrypted_text += matrix[row][col_index]
    return encrypted_text

def transpose_decrypt(ciphertext, key):
    # Calcula o número de colunas
    num_columns = len(key)
    # Calcula o número de linhas necessário para a matriz
    num_rows = (len(ciphertext) + num_columns - 1) // num_columns
    # Inicializa a matriz vazia
    matrix = [[''] * num_columns for _ in range(num_rows)]
    # Preenche a matriz de acordo com a ordem das colunas na chave
    col_order = [int(col) for col in key]
    col_order.sort()
    index = 0
    for col in col_order:
        col_index = col - 1
        for row in range(num_rows):
            if index < len(ciphertext):
                matrix[row][col_index] = ciphertext[index]
            index += 1
    # Constrói o texto decifrado lendo a matriz
    decrypted_text = ''
    for row in range(num_rows):
        for col in range(num_columns):
            decrypted_text += matrix[row][col]
    return decrypted_text.strip()  # Remove espaços em branco extras adicionados durante a cifragem

# Solicita a entrada do usuário
plaintext = input("Digite a mensagem: ")
key = input("Digite a chave de transposição (uma permutação dos números de 1 a N, por exemplo, '2143'): ")

# Criptografa a mensagem
encrypted_text = transpose_encrypt(plaintext, key)
print("Texto criptografado:", encrypted_text)

# Descriptografa a mensagem
decrypted_text = transpose_decrypt(encrypted_text, key)
print("Texto descriptografado:", decrypted_text)



