import random
import string

# Function to generate a random key
def generate_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

# Function to encrypt using OTP
def encrypt(plaintext, key):
    cipher = []
    for p, k in zip(plaintext, key):
        cipher_char = (ord(p) - 65 + ord(k) - 65) % 26 + 65
        cipher.append(chr(cipher_char))
    return ''.join(cipher)

# Function to decrypt using OTP
def decrypt(ciphertext, key):
    plaintext = []
    for c, k in zip(ciphertext, key):
        plain_char = (ord(c) - 65 - (ord(k) - 65)) % 26 + 65
        plaintext.append(chr(plain_char))
    return ''.join(plaintext)

# Example Usage
plaintext = "EVERYONE"

# First key
key1 = "SIMPLYON"
ciphertext1 = encrypt(plaintext, key1)
decrypted_text1 = decrypt(ciphertext1, key1)
print(f"Plaintext: {plaintext}")
print(f"Key 1: {key1}")
print(f"Cipher Text with Key 1: {ciphertext1}")
print(f"Decrypted Text with Key 1: {decrypted_text1}\n")

# Second key
key2 = "STUDENTS"
ciphertext2 = encrypt(plaintext, key2)
decrypted_text2 = decrypt(ciphertext2, key2)
print(f"Key 2: {key2}")
print(f"Cipher Text with Key 2: {ciphertext2}")
print(f"Decrypted Text with Key 2: {decrypted_text2}")
