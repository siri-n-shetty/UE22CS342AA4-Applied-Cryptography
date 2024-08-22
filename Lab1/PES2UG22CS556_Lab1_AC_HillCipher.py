import numpy as np

def matrix_mod_inverse(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))  
    det_inv = pow(det, -1, mod)  
    matrix_mod_inv = (
        det_inv
        * np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    )
    return matrix_mod_inv % mod

def hill_encrypt(message, key_matrix):
    message_vector = [ord(char) - ord('A') for char in message]
    message_vector = np.reshape(message_vector, (-1, 1))

    encrypted_vector = np.dot(key_matrix, message_vector) % 26
    encrypted_message = ''.join(chr(int(num) + ord('A')) for num in encrypted_vector.flatten())

    return encrypted_message

def hill_decrypt(encrypted_message, key_matrix):
    key_matrix_inv = matrix_mod_inverse(key_matrix, 26)

    encrypted_vector = [ord(char) - ord('A') for char in encrypted_message]
    encrypted_vector = np.reshape(encrypted_vector, (-1, 1))

    decrypted_vector = np.dot(key_matrix_inv, encrypted_vector) % 26
    decrypted_message = ''.join(chr(int(num) + ord('A')) for num in decrypted_vector.flatten())

    return decrypted_message

key_matrix = np.array([[6, 24, 1], 
                       [13, 16, 10], 
                       [20, 17, 15]])

message = "PES"
encrypted_message = hill_encrypt(message, key_matrix)
print("The encrypted message is: ", encrypted_message)

decrypted_message = hill_decrypt(encrypted_message, key_matrix)
print("The decrypted message is: ", decrypted_message)