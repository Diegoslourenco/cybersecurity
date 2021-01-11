from caesar import Caesar

def main():

    message = 'This is my secret message'
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz "

    original = Caesar(message)

    # Encrypting a message with a key value equal to 13
    cipher_message = original.encrypt(symbols, 13)
    print(cipher_message)

    # Decrypting a message with the key
    cipher = Caesar(cipher_message)
    original_message = cipher.decrypt(symbols, 13)
    print(original_message)

    # Decrypting a message without the key with brute-force
    # Printing all the possibilities and the original one
    original_message = cipher.brute_force(symbols)
    print(original_message)
    print(original_message[13])

    return

main()

