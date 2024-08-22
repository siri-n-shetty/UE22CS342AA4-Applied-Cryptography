#include <stdio.h>
#include <string.h>
#include <stdlib.h>  

void encryption() {
    int i, key;
    char s[1000], c;

    printf("Enter the plaintext to encrypt:\n");
    getchar();  
    fgets(s, sizeof(s), stdin);

    s[strcspn(s, "\n")] = '\0';

    printf("Enter key: ");
    scanf("%d", &key);

    int n = strlen(s);

    for (i = 0; i < n; i++) {
        c = s[i];

        if (c >= 'a' && c <= 'z') {
            c = c + key;
            if (c > 'z') {
                c = c - 'z' + 'a' - 1;
            }
            s[i] = c;
        } 
        
        else if (c >= 'A' && c <= 'Z') {
            c = c + key;
            if (c > 'Z') {
                c = c - 'Z' + 'A' - 1;
            }
            s[i] = c;
        }
    }

    printf("\nThe encrypted message: \n%s\n", s);
}

void decryption() {
    int i, key;
    char s[1000], c;

    printf("Enter encrypted text:\n");
    getchar();  
    fgets(s, sizeof(s), stdin);

    s[strcspn(s, "\n")] = '\0';

    printf("Enter key: ");
    scanf("%d", &key);

    int n = strlen(s);

    for (i = 0; i < n; i++) {
        c = s[i];
        
        if (c >= 'a' && c <= 'z') {
            c = c - key;
            if (c < 'a') {
                c = c + 'z' - 'a' + 1;
            }
            s[i] = c;
        } 
        
        else if (c >= 'A' && c <= 'Z') {
            c = c - key;
            if (c < 'A') {
                c = c + 'Z' - 'A' + 1;
            }
            s[i] = c;
        }
    }

    printf("Decrypted message: %s\n", s);
}

int main() {  
    int option;  
    while (1) {  
        printf("\nCaesar Cipher Tasks:");
        printf("\n1. Encrypt");  
        printf("\n2. Decrypt");  
        printf("\n3. Exit\n");  
        printf("\nEnter your option: ");  
        scanf("%d", &option);  
  
        switch (option) {  
            case 1:  
                encryption();  
                break;  
            case 2:  
                decryption();  
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
