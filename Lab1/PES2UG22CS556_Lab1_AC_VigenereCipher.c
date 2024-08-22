#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

void encrypt() {
    char plaintext[128];
    char key[16];
    printf("\nEnter the plaintext (up to 128 characters): ");
    scanf(" %[^\n]", plaintext); // Read input with spaces
    printf("Enter the key (up to 16 characters): ");
    scanf(" %[^\n]", key);

    printf("Cipher Text: ");
    for (int i = 0, j = 0; i < strlen(plaintext); i++) {
        if (isalpha(plaintext[i])) {
            if (j >= strlen(key)) {
                j = 0;
            }
            int shift = toupper(key[j]) - 'A';
            char encryptedChar = ((toupper(plaintext[i]) - 'A' + shift) % 26) + 'A';
            printf("%c", encryptedChar);
            j++;
        } else {
            printf("%c", plaintext[i]); // Non-alphabetic characters are unchanged
        }
    }
    printf("\n");
}

void decrypt() {
    char ciphertext[128];
    char key[16];
    printf("\nEnter the ciphertext: ");
    scanf(" %[^\n]", ciphertext);
    printf("Enter the key: ");
    scanf(" %[^\n]", key);

    printf("Deciphered Text: ");
    for (int i = 0, j = 0; i < strlen(ciphertext); i++) {
        if (isalpha(ciphertext[i])) {
            if (j >= strlen(key)) {
                j = 0;
            }
            int shift = toupper(key[j]) - 'A';
            char decryptedChar = ((toupper(ciphertext[i]) - 'A' - shift + 26) % 26) + 'A';
            printf("%c", decryptedChar);
            j++;
        } else {
            printf("%c", ciphertext[i]); // Non-alphabetic characters are unchanged
        }
    }
    printf("\n");
}

int main() {
    int option;
    while (1) {
        printf("\n1. Encrypt");
        printf("\n2. Decrypt");
        printf("\n3. Exit\n");
        printf("\nEnter your option: ");
        scanf("%d", &option);

        switch (option) {
            case 1:
                encrypt();
                break;
            case 2:
                decrypt();
                break;
            case 3:
                exit(0);
            default:
                printf("\nInvalid selection! Try again.\n");
                break;
        }
    }
    return 0;
}
