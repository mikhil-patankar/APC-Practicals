# Encrypt and decrypt a message using the Caesar Cipher algorithm.

def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift
    
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

message = input("Enter a message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_cipher(message, shift, mode='encrypt')
decrypted = caesar_cipher(encrypted, shift, mode='decrypt')

print(f"Encrypted message: {encrypted}")
print(f"Decrypted message: {decrypted}")
