def generate_playfair_square(key):
    # Remove duplicates from the key
    key = "".join(sorted(set(key), key=key.index))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Combine 'I' and 'J'
    
    # Create the 5x5 matrix
    matrix = []
    used_chars = set()
    
    for char in key + alphabet:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    return [matrix[i:i + 5] for i in range(0, len(matrix), 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def decrypt_playfair(ciphertext, key):
    matrix = generate_playfair_square(key)
    plaintext = []
    
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        
        if row1 == row2:
            plaintext.append(matrix[row1][(col1 - 1) % 5])
            plaintext.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            plaintext.append(matrix[(row1 - 1) % 5][col1])
            plaintext.append(matrix[(row2 - 1) % 5][col2])
        else:
            plaintext.append(matrix[row1][col2])
            plaintext.append(matrix[row2][col1])
    
    return ''.join(plaintext)

# Ciphertext
ciphertext = "ITCSITGSSMBWKFBQTS"

# Try common keys
common_keys = ["KEYWORD", "SECURITY", "SECRET", "PASSWORD"]

for key in common_keys:
    decrypted_text = decrypt_playfair(ciphertext, key)
    print(f"Key: {key}, Decrypted Text: {decrypted_text}")
