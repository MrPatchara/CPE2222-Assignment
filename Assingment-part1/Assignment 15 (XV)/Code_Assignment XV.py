# Input: Plaintext and secret key from the user
plaintext = input("Enter your plaintext (Alphabet Only): ")
secretkey = int(input("Enter your secret key (Number Only): "))

# Caesar Cipher encryption function
def encrypt(P, k):
    result = ""
    for char in P:
        if char.isupper():
            # Shift character and wrap around within uppercase letters
            result += chr((ord(char) - 65 + k) % 26 + 65)
        elif char.islower():
            # Shift character and wrap around within lowercase letters
            result += chr((ord(char) - 97 + k) % 26 + 97)
    return result

# Caesar Cipher decryption function
def decrypt(C, k):
    result = ""
    for char in C:
        if char.isupper():
            # Reverse shift for uppercase letters
            result += chr((ord(char) - 65 - k) % 26 + 65)
        elif char.islower():
            # Reverse shift for lowercase letters
            result += chr((ord(char) - 97 - k) % 26 + 97)
    return result

# Encrypt the plaintext
ciphertext = encrypt(plaintext, secretkey)
print('The encrypted ciphertext:', ciphertext)

# Decrypt the ciphertext
decryptedtext = decrypt(ciphertext, secretkey)
print('The decryption results:', decryptedtext)
