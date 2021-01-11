# Caesar Cipher Algorithm

class Caesar:

    def __init__(self, text):
        self.text = text

    def encrypt(self, symbols, key):
        """
        Encrypt a text according to a given key and symbols
        """
        encrypted_text = ""

        for symbol in self.text:
            # Look for the index in the symbols
            original_index = symbols.find(symbol)
            
            # Sum the index found with the key value and handle wraparound when needed
            cipher_index = (original_index + key) % len(symbols)
            encrypted_text += symbols[cipher_index]

        return encrypted_text

    def decrypt(self, symbols, key):
        """
        Decrypt a text according to a given key and symbols
        """
        decrypted_text = ""

        for symbol in self.text:
            cipher_index = symbols.find(symbol)

            original_index = (cipher_index - key) % len(symbols)
            decrypted_text += symbols[original_index]

        return decrypted_text

    def brute_force(self, symbols):
        """
        Receives a text and returns a list with all the possibilities to decrypt a text without a 
        key using brute-force attack

        """

        translated_list = []

        # look for every possible key
        for key in range(len(symbols)):

            translated_text = ""

            for symbol in self.text:
                if symbol in symbols:
                    # get the index of the symbol minus the key value and handle wraparound when needed
                    cipher_index = symbols.find(symbol)
                    symbol_index = (cipher_index - key) % len(symbols) 

                    # add the symbol at the end of translated
                    translated_text += symbols[symbol_index]

                else:
                    # add the symbol without changing it
                    translated_text += symbol

            translated_list.append((key, translated_text))

        return translated_list
