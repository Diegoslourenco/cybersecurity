from file_encrypt import encrypt_transposition, decrypt_transposition

def main():

    file_name = 'tomsawyer.txt'
    file_name_encrypted = 'encrypted_tomsawyer.txt'
    key = 15

    # Encrypting the book
    encrypt_transposition(file_name, key)

    # Decrypting the book with the key
    decrypt_transposition(file_name_encrypted, key)

    return

main()