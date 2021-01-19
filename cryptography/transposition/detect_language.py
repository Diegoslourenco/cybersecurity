# Detect Language Module

def load_dictionary(language=''):
    """
    Load a dictionary that contains all the words in a refered language\n
    The default language is english
    """
    dictionary_file = open(f'dictionary{language}.txt', encoding='utf-8')
    words = {}
    for word in dictionary_file.read().split('\n'):
        words[word] = None
    dictionary_file.close()

    return words
          
def remove_non_letters(text):
    """
    Remove all non letters characters from a text
    """
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters_and_space = upper_letters + upper_letters.lower() + ' \t\n' + 'áàãâéêíîóõú' + '-ç'

    letters = []

    for symbol in text:
        if symbol in letters_and_space:
            letters.append(symbol)

    return ''.join(letters)

def count_language(text, language=''):
    """
    Returns the percentage about how many words from a language are in a text\n
    The default language is english
    """
    text = text.upper()
    text = remove_non_letters(text)

    possible_words = text.split()

    # If the is no possible words the percentage is zero
    if possible_words == []:
        return 0.0

    # If there is possible words, start a count for matches with zero
    # Open a dictionary for a language with the valid words
    # Each wor in possible words is checked in the valid words
    word_matches = 0
    valid_words = load_dictionary(language)

    for word in possible_words:
        if word in valid_words:
            word_matches += 1
        
    # Divide the number of matches for all the possibilities
    return float(word_matches) / len(possible_words)

def check_valid_language(text, language='', word_percentage=50, letter_percentage=80):
    """
    Checks if the text is in a language and returns a bool\n
    By default the language is english, the word percentage equals to 50% and letter percentage 80%
    """

    words_match = count_language(text, language) * 100 >= word_percentage
    
    number_letters = len(remove_non_letters(text))
    letters_percentage = (float(number_letters) / len(text)) * 100
    letters_match = letters_percentage >= letter_percentage

    return words_match and letters_match