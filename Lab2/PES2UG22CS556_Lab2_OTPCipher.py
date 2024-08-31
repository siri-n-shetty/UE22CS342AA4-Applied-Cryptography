def otp_decrypt(cipher_text, key):
    all_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper()
    decrypted_mesg = []
    
    key_length = len(key)
    
    for i, char in enumerate(cipher_text):
        if char.isalpha():
            key_char = key[i % key_length]
            cipher_index = all_alphabets.index(char.upper())
            key_index = all_alphabets.index(key_char)
            new_index = (cipher_index - key_index) % 26
            decrypted_char = all_alphabets[new_index]
            if char.islower():
                decrypted_char = decrypted_char.lower()
            decrypted_mesg.append(decrypted_char)
        else:
            decrypted_mesg.append(char)
    
    return ''.join(decrypted_mesg)

def derive_key(cipher_text, known_plaintext):
    all_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = []
    
    for i, char in enumerate(known_plaintext):
        if char.isalpha():
            cipher_char = cipher_text[i]
            cipher_index = all_alphabets.index(cipher_char.upper())
            plain_index = all_alphabets.index(char.upper())
            key_index = (cipher_index - plain_index) % 26
            key_char = all_alphabets[key_index]
            key.append(key_char)
    
    return ''.join(key)

cipher_text = "CXZIMW VLK DYMA YMZP VLK HIXWMUHO QJ C EELNOUBQLYZ PMTRK !"
known_plaintext = "ATTACK"

key = derive_key(cipher_text, known_plaintext)

decrypted_message = otp_decrypt(cipher_text, key)

print(f"Key: {key}")
print(f"The decrypted message is: {decrypted_message}")