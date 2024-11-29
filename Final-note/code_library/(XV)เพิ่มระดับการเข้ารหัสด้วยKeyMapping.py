def secret_password_with_mapping(text, key_mapping):
    """
    Encrypts text using a custom key mapping.

    Parameters:
    text (str): The input text to be encrypted.
    key_mapping (dict): A dictionary mapping each letter to its shifted counterpart.

    Returns:
    str: The encrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():
            result += key_mapping.get(char, char)  # Replace character using mapping
        elif char.isspace():
            result += char  # Preserve spaces
        else:
            raise ValueError("Error!!!! Input contains unsupported characters.")
    return result

try:
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key = int(input("Enter secret key (Number Only): "))

    # Create key mapping for both uppercase and lowercase letters
    key_mapping = {}
    for i in range(26):
        key_mapping[chr(ord('A') + i)] = chr((ord('A') + i - ord('A') + key) % 26 + ord('A'))
        key_mapping[chr(ord('a') + i)] = chr((ord('a') + i - ord('a') + key) % 26 + ord('a'))

    # Encrypt and display the result
    ciphertext = secret_password_with_mapping(plaintext, key_mapping)
    print("The encrypted ciphertext:", ciphertext)

    # Reverse the mapping for decryption
    reverse_mapping = {v: k for k, v in key_mapping.items()}
    decrypted_text = secret_password_with_mapping(ciphertext, reverse_mapping)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)
