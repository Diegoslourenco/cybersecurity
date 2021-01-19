# Transposition cipher Algorithm

class Transposition:
    """
    Receive the text
    """

    def __init__(self, text):
        self.text = text
    
    def encrypt(self, key):
        """
        Giving a key, return the encrypted message in a transposition way
        """

        cipher_text = [''] * key

        for column in range(key):
            pointer = column

            while pointer < len(self.text):

                cipher_text[column] += self.text[pointer]

                pointer += key

        return ''.join(cipher_text)

    def decrypt(self, key):
        """
        Given a key, decrypt a message using the transposition method
        """
        import math

        # Setting the matrix
        columns_number = math.ceil(len(self.text) / key)
        rows_number = key
        empty_boxes = (columns_number * rows_number) - len(self.text)

        original_text = [''] * columns_number

        # Points to where the characters will go in the matrix
        column = 0
        row = 0

        for symbol in self.text:
            # Put the symbol in the matrix and the column will point to the next column
            original_text[column] += symbol
            column += 1

            # If the column reached the end of the matrix, or
            # In the last column, it is pointing to the boxes that should be empty
            # point to the beggining of the next row
            if (column == columns_number) or (column == columns_number - 1 and row >= rows_number - empty_boxes):
                column = 0
                row += 1

        return ''.join(original_text)

    def brute_force(self, language='', word_percentage=50, letter_percentage=80):
        """
        Use the brute force attack to check for all keys\n
        Check the decrypted text for a given language and returns all the possibilities 
        in a list as (key, message)\n
        The default values are language equals to english, word percentage 50% and letter percentage 80%
        """
        from detect_language import check_valid_language

        possible_decrypted = []

        for key in range(1, len(self.text)):
            decrypted_text = self.decrypt(key)

            if check_valid_language(decrypted_text, language, word_percentage, letter_percentage):
                possible_decrypted.append((key, decrypted_text))
        
        return possible_decrypted
