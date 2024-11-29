# Import functions from the required modules
from caesar_encrypt import f as caesar_encrypt
from caesar_decrypt import f as caesar_decrypt
from plaintext import data as plaintext_dict
from ciphertext import data as ciphertext_list

# Brute Force Caesar Cipher Decryption function
def brute_force_decryption():
    print("-----------------------------------------------------------")
    print("Brute Force Caesar Cipher Decryption (Unknown Key)")
    print("-----------------------------------------------------------")
    
    # Loop through each plaintext
    for key, plaintext in plaintext_dict.items():  # Corrected line here
        print(f'Reading dictionary of plaintexts {key}) "{plaintext}"')
        
        # Loop through possible secret keys (1 to 26)
        for shift in range(1, 27):
            # Encrypt the plaintext with the current shift value
            encrypted_text = caesar_encrypt(plaintext, shift)
            
            # Check if the encrypted text matches any ciphertext
            if encrypted_text in ciphertext_list:
                print(f'Finding the ciphertext match: "{encrypted_text}"')  # Show ciphertext that matches
                print(f'The secret key is {shift}')
                break  # Break when a match is found for this plaintext
        print("-----------------------------------------------------------")

# Call the brute_force_decryption function to start the process
brute_force_decryption()
