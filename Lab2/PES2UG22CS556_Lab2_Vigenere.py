from collections import Counter
import string

def most_common_letter(text):
    frequencies = Counter(text)
    return frequencies.most_common(1)[0][0]

def guess_key(ciphertext, key_length):
    key = []
    for i in range(key_length):
        nth_letters = ciphertext[i::key_length]
        
        most_common = most_common_letter(nth_letters)
        shift = (ord(most_common) - ord('E')) % 26
        key.append(chr(shift + ord('A')))
        
    return ''.join(key)

def decrypt_vigenere(ciphertext, key):
    plaintext = []
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            decrypted_char = (ord(char) - shift)
            
            if char.isupper():
                decrypted_char = (decrypted_char - ord('A')) % 26 + ord('A')
            else:
                decrypted_char = (decrypted_char - ord('a')) % 26 + ord('a')
            
            plaintext.append(chr(decrypted_char))
        else:
            plaintext.append(char)
    
    return ''.join(plaintext)

ciphertext = ("Sr rri oemcd xmgr mp Vgfipdsl, dlc cyl cir qildpw yzcb xfo lmbmxyr yc xfo xmgrqzimzpc qerripoh dyv rrigb itorgxk dowrszgdmcc. Xfo wrbicdw uovc vmloh usxf msjyvdep jkrrovlc, eln xfo wmerb yj jkyerxcb jgvpcn xfo egb. Ekshqd xfo gfoippyj kxkywnripo, e kiwrovgyyq pmeevc cpgztcn xfbssql rri absun, gybvw sre k gpitrsg kowqkkc dlyd amepb csmx ylbetop y dlpspjsre ciabir. Kw rri lskfd hcotcxib, dlc obasxcwild kpoa, yxh cfipislo iyqipvc yxxgmmnkxcn xfo ylpsjnmlq sd dlc rmbnil dvsdl.")

key_length = 3

key = guess_key(ciphertext.replace(" ", ""), key_length)
print(f"Guessed Key: {key}")

decrypted_text = decrypt_vigenere(ciphertext, key)
print("Decrypted Text:")
print(decrypted_text)
