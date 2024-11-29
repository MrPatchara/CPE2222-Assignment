def secret_password(text, key):
    """
    Encrypts or decrypts the input text using a Caesar cipher with the given key.

    Parameters:
    text (str): The input text to be encrypted or decrypted.
    key (int): The encryption/decryption key. Positive for encryption, negative for decryption.

    Returns:
    str: The resulting ciphertext or plaintext.

    Raises:
    ValueError: If the input contains unsupported characters.
    """
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter (A-Z, a-z)
            shift_base = ord('A') if char.isupper() else ord('a')  # Determine ASCII base for uppercase or lowercase
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base)  # Shift and wrap within alphabet range
            result += shifted_char  # Append the encrypted/decrypted character to the result
        elif char.isspace():  # Preserve spaces in the text
            result += char
        else:  # Raise error if unsupported character is found
            raise ValueError("Error!!!! Input contains unsupported characters.")
    return result

try:
    # Prompt the user until a valid plaintext is provided
    while True:
        plaintext = input("Enter plaintext (Alphabet Only, Non-Empty): ").strip()
        if plaintext:  # Ensure the input is not empty
            break
        print("Error: Plaintext cannot be empty. Please try again.")
    
    # Prompt the user for a valid key
    key = int(input("Enter secret key (Number Only): "))

    # Encrypt the plaintext
    ciphertext = secret_password(plaintext, key)
    print("The encrypted ciphertext:", ciphertext)

    # Decrypt the ciphertext
    decrypted_text = secret_password(ciphertext, -key)
    print(f'The decryption result: {decrypted_text}')
except ValueError as e:
    print(e)
