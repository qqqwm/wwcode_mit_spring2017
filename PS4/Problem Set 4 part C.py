
import string
from ps4a import get_permutations

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    #print("Loading word list from file...")
    # infile: file
    infile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in infile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list



WORDLIST_FILENAME = 'words.txt'

VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        transpose_dict = {i : i for i in CONSONANTS_LOWER}
        transpose_dict.update({i : i for i in CONSONANTS_UPPER})
        transpose_dict.update({VOWELS_LOWER[i] : vowels_permutation[i].lower() \
                               for i in range(len(VOWELS_LOWER))})
        transpose_dict.update({VOWELS_UPPER[i] : vowels_permutation[i].upper() \
                               for i in range(len(VOWELS_UPPER))})
        return transpose_dict
        
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypted_message = ''
        message = SubMessage.get_message_text(self)
        for letter in message:
            if letter in transpose_dict:
                encrypted_message += transpose_dict[letter]
            else:
                encrypted_message += letter
        return encrypted_message
                
        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
    
        max_counter = 0
        best_message = 0
        available_permutations = get_permutations('aeiou')
        for permutation in available_permutations:
            transpose_dict = SubMessage.build_transpose_dict(self, permutation)
            counter = 0
            message = SubMessage.apply_transpose(self, transpose_dict).split(' ')
            for word in message:
                if is_word(self.valid_words, word):
                    counter += 1
            if counter >= max_counter:
                max_counter = counter
                best_message = message
        return ' '.join(best_message)
   

if __name__ == '__main__':

    
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("\nOriginal message:       ", message.get_message_text())
    print("Permutation:            ", permutation)
    print("Expected encryption:    ", "Hallu Wurld!")
    print("Actual encryption:      ", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:      ", enc_message.decrypt_message())

    message = SubMessage("it's better to burn out than to fade away")
    permutation = "ieauo"
    enc_dict = message.build_transpose_dict(permutation)
    print("\nOriginal message:       ", message.get_message_text())
    print("Permutation:            ", permutation)
    print("Expected encryption:    ", "at's better tu born uot thin tu fide iwiy")
    print("Actual encryption:      ", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:      ", enc_message.decrypt_message())

    message = SubMessage("Wanting to be someone else is a waste of the person you are.")
    permutation = "ioeua"
    enc_dict = message.build_transpose_dict(permutation)
    print("\nOriginal message:       ", message.get_message_text())
    print("Permutation:            ", permutation)
    print("Expected encryption:    ", 'Winteng tu bo sumouno olso es i wisto uf tho porsun yua iro.')
    print("Actual encryption:      ", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:      ", enc_message.decrypt_message())
