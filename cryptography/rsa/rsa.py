# RSA Cipher Algorithm

class Rsa:
    """
    Can receive the text and the block size
    """

    def __init__(self, text='', block_size=128):
        self.text = text
        self.block_size = block_size
        self.byte_size = 256 # Each byte has 256 different values


    def read_key_file(self, key_file_name):
        """
        Open a file and get the pairs for the public and private keyy
        """
        with open(key_file_name) as key_file:
            key_size, n, e_or_d = key_file.read().split('\n')
        return (int(key_size), int(n), int(e_or_d))


    def get_blocks_from_text(self, text):
        """
        Convert a text in a list of block integers. Each integer represents
        the number set in block_size as string characters
        """
        # Converting the text to bytes
        message_bytes = text.encode('ascii')

        # Start the list of blocks
        block_integers = []

        for block_start in range(0, len(message_bytes), self.block_size):
            # Calculate the block integer for this block of text
            block_int = 0
            for i in range(block_start, min(block_start + self.block_size, len(message_bytes))):
                block_int += message_bytes[i] * (self.byte_size ** (i % self.block_size))
            
            block_integers.append(block_int)
        
        return block_integers


    def get_text_from_blocks(self, block_integers, message_length):
        """
        Convert a list of block integers to the original message
        """
        message = []

        for block_int in block_integers:
            block_message = []

            for i in range(self.block_size -1, -1, -1):
                if len(message) + i < message_length:
                    # Decode the message for the number of the block_size characters
                    # from this block integer
                    ascii_number = block_int // (self.byte_size ** (i % self.block_size))
                    block_int = block_int % (self.byte_size ** i)
                    block_message.insert(0, chr(ascii_number))
            message.extend(block_message)
        return ''.join(message)


    def encrypt(self, message_file, public_key_file):
        """
        Convert the message to a list of blocks integers, encrypt each block\n
        and export a file with the content\n
        Receive the message file and the public key file to encrypt
        """
        from sys import exit

        # Getting the keys
        key_size, n, e = self.read_key_file(public_key_file)

        # Check if the key size is greater than block size, converting bytes to bits
        if key_size < self.block_size * 8:
            exit(f'ERROR: RSA cipher requires that the block size ({self.block_size * 8} bits) to be '+
                        f'equal to or less than key size ({key_size} bits). '+
                        f'Increase block size or use different keys.')

        encrypted_blocks = []

        for block in self.get_blocks_from_text(self.text):
            # cipher_text = plain_text ** e mod n
            encrypted_blocks.append(pow(block, e, n))

        # Converting the large integer values to one string
        for i in range(len(encrypted_blocks)):
            encrypted_blocks[i] = str(encrypted_blocks[i])
        encrypted_content = ','.join(encrypted_blocks)

        # Export the content
        with open(f'{message_file}', 'w') as encrypted:
            encrypted.write(f'{len(self.text)}\n{self.block_size}\n{encrypted_content}')

        return


    def decrypt(self, message_file, private_key_file):
        """
        Decrypt a list of encrtpted blocks integers into the original message
        Receive the message file and the private key file
        """
        from sys import exit

        # Getting the keys
        key_size, n, d = self.read_key_file(private_key_file)

        # Read the message length, block size and encrypted message from the file
        with open(message_file, 'r') as encrypted_file:
            message_length, block_size, encrypted_message = encrypted_file.read().split('\n')
        
        message_length = int(message_length)
        block_size = int(block_size)

        # Check if the key size is greater than block size, converting bytes to bits
        if key_size < block_size * 8:
            exit(f'ERROR: RSA cipher requires that the block size ({self.block_size * 8} bits) to be '+
                        f'equal to or less than key size ({key_size} bits). '+
                        f'Use the correct encrypted file and private key.')

        # Convert the encrypted message into large integer values
        encrypted_blocks = []

        for block in encrypted_message.split(','):
            encrypted_blocks.append(int(block))

        # Decrpt the large integer values
        decrypted_blocks = []

        for block in encrypted_blocks:
            # plain_text = cipher_text ** d mod n
            decrypted_blocks.append(pow(block, d, n))

        original_message = self.get_text_from_blocks(decrypted_blocks, message_length)

        with open(f'decrypted_{message_file}', 'w') as decrypted:
            decrypted.write(original_message)
        
        return original_message




