from rsa import Rsa
from rsa_key_generator import export_key

def main():
    # Creating public and private keys
    key_size = 1024
    export_key('diego', key_size)

    # Message to be encrypted
    message = 'This is my secret message'

    # Encrypting the message and exporting to a file
    cipher = Rsa(message)
    cipher.encrypt('encrypted_message.txt', 'diego_public_key.txt')

    # Decrypting the message from a file and exporting to another file
    original = Rsa()
    original.decrypt('encrypted_message.txt', 'diego_private_key.txt')

    return

main()