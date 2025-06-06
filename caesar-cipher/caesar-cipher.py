"""Implementation of the caesar cipher."""

def get_double_alphabet(alphabet):
    """Concatenates the given string to itself and returns the result."""
    double_alphabet = alphabet + alphabet
    return double_alphabet

def get_message():
    """Prompts user for message and returns input."""
    string_to_encrypt = input("Please enter a message to encrypt: ")
    return string_to_encrypt

def get_cipher_key():
    """Prompts user for cipher key and returns input."""
    shift_amount = int(input("Please enter a key (whole number from 1-25): "))
    if 1 > shift_amount or 25 < shift_amount:
        raise ValueError
    return shift_amount

def encrypt_message(message, cipher_key, alphabet):
    """Encrypts given message in given alphabet with given cipher key."""
    encrypted_message = ""
    uppercase_message = message.upper()
    uppercase_alphabet = alphabet.upper()
    for character in uppercase_message:
        position_in_alphabet = uppercase_alphabet.find(character)
        shifted_position_in_alphabet = position_in_alphabet + int(cipher_key)
        if character in uppercase_alphabet:
            encrypted_message = encrypted_message + uppercase_alphabet[shifted_position_in_alphabet]
        else:
            encrypted_message = encrypted_message + character
    return  encrypted_message

def decrypt_message(message, cipher_key, alphabet):
    """Decrypts given message in given alphabet with given cipher key."""
    decrypt_key = -1 * int(cipher_key)
    return encrypt_message(message, decrypt_key, alphabet)

def run_caesar_cipher():
    """Runs caesar cipher"""
    alphabet = "ABCDEFGHIJKLMNOPQRZTUVWXYZ"
    double_alphabet = get_double_alphabet(alphabet)
    
    message = get_message()
    
    try:
        cipher_key = get_cipher_key()
        encrypted_message = encrypt_message(message, cipher_key, double_alphabet)
        print("The encrypted message is: " + encrypted_message)
        decrypted_message = decrypt_message(encrypted_message, cipher_key, double_alphabet)
        print("The decrypted message is: " + decrypted_message)
    except ValueError:
        print("Something went wrong! Please make sure that all inputs are valid.")

run_caesar_cipher()