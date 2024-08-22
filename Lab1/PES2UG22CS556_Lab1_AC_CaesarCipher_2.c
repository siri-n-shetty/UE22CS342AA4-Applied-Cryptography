#include <stdio.h>
#include <string.h>
#include <ctype.h>

void decrypt_caesar_cipher(char *ciphertext, int shift) {
    char decrypted_text[1000];
    strcpy(decrypted_text, ciphertext);

    for (int i = 0; i < strlen(ciphertext); i++) {
        char c = ciphertext[i];
        if (isalpha(c)) {
            char ascii_offset = isupper(c) ? 'A' : 'a';
            decrypted_text[i] = (c - ascii_offset - shift + 26) % 26 + ascii_offset;
        } else {
            decrypted_text[i] = c;
        }
    }

    decrypted_text[strlen(ciphertext)] = '\0';
    printf("Shift %d: %s\n", shift, decrypted_text);
}

void brute_force_caesar(char *ciphertext) {
    for (int shift = 1; shift < 26; shift++) {
        decrypt_caesar_cipher(ciphertext, shift);
    }

    int correct_shift;
    printf("\nEnter the correct shift value based on the above outputs: ");
    scanf("%d", &correct_shift);

    printf("\nCorrect plaintext: ");
    decrypt_caesar_cipher(ciphertext, correct_shift);
    printf("Shift value: %d\n", correct_shift);
}

int main() {
    char ciphertext[] = "Ofctyr zfc xppetyr ezxzcczh, hp htww qtylwtkp esp awlyd qzc esp fanzxtyr pgpye. Te td ncfntlw esle pgpcjzyp fyopcdelyod esptc czwpd lyo cpdazydtmtwtetpd. Awpldp pydfcp esle lww ypnpddlcj acpalcletzyd lcp nzxawpepo mj esp pyo zq esp olj.";
    brute_force_caesar(ciphertext);
    return 0;
}
