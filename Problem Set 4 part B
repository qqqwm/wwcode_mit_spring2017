"""
Encryption and decryption using Caesar Cipher
"""

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
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

    def __str__(self):
        return Message.get_message_text(self)

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string).
        '''
        encryption_dict = {chr(i) : chr((i - 65 + shift)%26 + 65) for i in range(65, 91)}
        encryption_dict.update({chr(i) : chr((i - 97 + shift)%26 + 97) for i in range(97, 123)})
        return encryption_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.cc with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        encryption_dict = Message.build_shift_dict(self, shift)
        message_text_encrypted = ''
        for symbol in Message.get_message_text(self):
            if symbol in encryption_dict:
                message_text_encrypted += encryption_dict[symbol]
            else:
                message_text_encrypted += symbol
        return message_text_encrypted

    
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        max_counter = 0
        right_shift = 0
        for shift in range(0, 26):
            Message.build_shift_dict(self, shift)
            counter = 0
            message = Message.apply_shift(self, shift).split(' ')
            for i in message:
                if is_word(self.valid_words, i):
                    counter += 1
            if counter >= max_counter:
                max_counter = counter
                right_shift = shift
        return (right_shift, Message.apply_shift(self, right_shift))

if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())
    
    #Test case (PlaintextMessage)
    PLAINTEXT = PlaintextMessage('red, blue, white', 2)
    print('Test 1 PlaintextMessage')
    print('Input:            ', PLAINTEXT)
    print('Expected Output:   tgf, dnwg, yjkvg')
    print('Actual Output:    ', PLAINTEXT.get_message_text_encrypted())

    PLAINTEXT = PlaintextMessage('abcdefghijklmn', 25)
    print('\nTest 2 PlaintextMessage')
    print('Input:            ', PLAINTEXT)
    print('Expected Output:   zabcdefghijklm')
    print('Actual Output:    ', PLAINTEXT.get_message_text_encrypted())
    
    #Test case (CiphertextMessage)
    CIPHERTEXT = CiphertextMessage('tgf, dnwg, engxgt')
    print('\nTest 1 CiphertextMessage')
    print('Input:            ', CIPHERTEXT)
    print('Expected Output:  ', (24, 'red, blue, clever'))
    print('Actual Output:    ', CIPHERTEXT.decrypt_message())

    CIPHERTEXT = CiphertextMessage('a dgnw hqlzgf')
    print('\nTest 2 CiphertextMessage')
    print('Input:            ', CIPHERTEXT)
    print('Expected Output:  ', (8, 'i love python'))
    print('Actual Output:    ', CIPHERTEXT.decrypt_message(), '\n')

    #unencrypting story
    CIPHERTEXT = CiphertextMessage(get_story_string())
    UNECRYPTED_STORY = CIPHERTEXT.decrypt_message()
    print('The best shift value: ', UNECRYPTED_STORY[0])
    print('Unecrypted story:\n', UNECRYPTED_STORY[1])
    
