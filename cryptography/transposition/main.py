from transposition import Transposition

def main():

    message = 'This is my secret message.'
    message_ptbr = 'Essa é minha mensagem secreta.'
    key = 8

    # For english message
    cipher = Transposition(message)

    # Encrypting the message with a key
    cipher_text = cipher.encrypt(key)
    print(cipher_text)

    # Decrypting the message with the key
    original = Transposition(cipher_text)
    original_text = original.decrypt(key)
    print(original_text)

    # Decrypting the message without a key
    original_text = original.brute_force()
    print(original_text)

    # For portuguse message
    cipher = Transposition(message_ptbr)

    # Encrypting the message with a key
    cipher_text = cipher.encrypt(key)
    print(cipher_text)

    # Decrypting the message with the key
    original = Transposition(cipher_text)
    original_text = original.decrypt(key)
    print(original_text)

    # Decrypting the message without a key
    original_text = original.brute_force(language='ptbr')
    print(original_text)

    return

main()