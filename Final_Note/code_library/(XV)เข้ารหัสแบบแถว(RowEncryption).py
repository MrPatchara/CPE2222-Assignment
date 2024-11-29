def secret_password_row(text, key, row_count):
    """
    Encrypts text using a Caesar cipher and splits it into rows.

    Parameters:
    text (str): The input text to be encrypted.
    key (int): The encryption key.
    row_count (int): Number of rows for splitting.

    Returns:
    list: A list of encrypted text split into rows.
    """
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')  # Determine ASCII base
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base)
            result += shifted_char  # Append the encrypted character
        elif char.isspace():
            result += char
        else:
            raise ValueError("Error!!!! Input contains unsupported characters.")
    
    # Split the result into rows of approximately equal size
    row_size = len(result) // row_count + (len(result) % row_count > 0)
    return [result[i:i + row_size] for i in range(0, len(result), row_size)]

try:
    # Input text, key, and desired number of rows
    plaintext = input("Enter plaintext (Alphabet Only): ")
    key = int(input("Enter secret key (Number Only): "))
    row_count = int(input("Enter number of rows for output (Integer Only): "))

    # Encrypt the plaintext and split it into rows
    encrypted_rows = secret_password_row(plaintext, key, row_count)
    print("The encrypted text split into rows:")
    for i, row in enumerate(encrypted_rows, 1):
        print(f"Row {i}: {row}")

    # Combine the rows back and decrypt to verify
    combined_encrypted = ''.join(encrypted_rows)
    decrypted_text = secret_password_row(combined_encrypted, -key, 1)[0]  # Decrypt back to single row
    print(f"The decryption result: {decrypted_text}")
except ValueError as e:
    print(e)
