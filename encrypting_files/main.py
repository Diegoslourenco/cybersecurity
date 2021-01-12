from file_encrypt import file_encrypt_transposition

def main():

    file_name = 'tomsawyer.txt'
    key = 15
    file_encrypt_transposition(file_name, key)

    return

main()