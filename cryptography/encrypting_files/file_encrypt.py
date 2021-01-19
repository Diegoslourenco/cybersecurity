from transposition import Transposition

def open_file(file_name):
    """
    Open a file and return the content
    """
    opened_file = open(file_name, encoding='utf8')
    content = opened_file.read()
    opened_file.close()

    return content


def export_file(content, file_name):
    """
    Export the content to a txt file
    """
    exported_file = open(file_name, 'w', encoding='utf8')
    exported_file.write(content)
    exported_file.close()

    return


def encrypt_transposition(input_file, key):
    """
    Encrypt a text in a file given a key according to the Transposition method
    """
    # Open the file and saving the content in a variable
    content = open_file(input_file)

    # Instances the object
    cipher = Transposition(content)

    # Encrypting the content according to the key
    cipher_text = cipher.encrypt(key)

    # Exporting file as txt
    export_file(cipher_text, f'encrypted_{input_file}')

    return


def decrypt_transposition(input_file, key):
    """
    Decrypt a text in a file given a key according to the Transposition method
    """
    # Open the file and saving the content in a variable
    content = open_file(input_file)

    # Instances the object
    plain = Transposition(content)

    # Decrypting the content according to the key
    plain_text = plain.decrypt(key)

    # Exporting file as txt
    export_file(plain_text, f'decrypted_{input_file}')

    return








