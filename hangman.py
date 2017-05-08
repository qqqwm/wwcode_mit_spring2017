"""
This program is a game hangman.
Game rules:
1. The user starts with 3 warnings. 
2. If the user inputs anything besides an alphabet (symbols, numbers),
tell the user that they can only input an alphabet.  
a. If the user has one or more warning left, the user should lose one 
warning. Tell the user the number of remaining warnings. 
b. If the user has no remaining warnings, they should lose one guess. 
3. If the user inputs a letter that has already been guessed, print a message 
telling the user the letter has already been guessed before. 
a. If the user has one or more warning left, the user should lose one 
warning. Tell the user the number of remaining warnings. 
b. If the user has no warnings, they should lose one guess. 
4. If the user inputs a letter that hasn’t been guessed before and the letter
is in the secret word, the user loses ​no​ guesses. 
...
"""
# Name: Sasha Panova


import random
import pylint
#import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Loads wordlist from file and returnes it.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    Chooses random word from the wordlist and returnes it.
    """
    return random.choice(wordlist)


WORDLIST = load_words()


def get_guessed_word(secret_word, letters_guessed):
    """
    This function takes in two parameters ­ a string, ​secret_word​, 
    and a list of letters, ​letters_guessed​. 
    This function returns a string that is comprised of letters and underscores,
    based on what letters in letters_guessed​ are in ​secret_word​. 
    """
    return_string = ''
    for i in range (0, len(secret_word)):
        k = False
        for j in range (0, len(letters_guessed)):
            if letters_guessed[j] == secret_word[i]:
                return_string += secret_word[i]
                k = True
                break
        if k == False:
            return_string += '_ '
    return return_string


def is_word_guessed(secret_word, letters_guessed):
    """
    This funtion takes in two parameters ­ a string, ​secret_word​, and a list
    of letters (strings), ​letters_guessed.​ This function returns a boolean ­
    ​True​ if ​secret_word​ has been guessed and False otherwise.
    """
    for i in range (0, len(secret_word)):
        if secret_word[i] != get_guessed_word(secret_word, letters_guessed)[i]:
            return False
    return True


def get_available_letters(letters_guessed):
    """
    Chooses from all_letters letters that user haven't guessed and returnes it.
    """
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    available_letters = ''
    for i in all_letters:
        if i not in letters_guessed:
            available_letters += i
    return available_letters
            

def hangman(secret_word):
    """
    Implements the game with hints.
    """
    letters_guessed = []
    unique_letters = 0
    guesses_left = 6
    warnings_left = 3
    winning = False
    print ('Welcome to the game Hangman!')
    print ('I am thinking of a word that is ', len(secret_word), ' letters long.')
    print ('__________________')
    #print (secret_word)
    while guesses_left > 0:
        available_letters = get_available_letters(letters_guessed)
        print ('You have', guesses_left ,'guesses left.')
        print ('Available letters:', available_letters)
        letters_guessed += [str.lower(input('Please guess a letter: '))]
        if len(letters_guessed[len(letters_guessed) - 1]) != 1:
            print('Enter only one letter.')
        elif letters_guessed[len(letters_guessed) - 1] in letters_guessed[0:-1]:
            if warnings_left > 0:
                warnings_left -= 1
            else:
                guesses_left -= 1
            print("Oops! You've already guessed that letter. You have", \
                  warnings_left,'warnings left :')
        elif letters_guessed[len(letters_guessed) - 1] not in available_letters:
            if warnings_left > 0:
                warnings_left -= 1
            else:
                guesses_left -= 1
            print('Oops! That is not a valid letter. You have', warnings_left, \
                  ' warnings left:', get_guessed_word(secret_word, letters_guessed))
        elif letters_guessed[len(letters_guessed) - 1] in secret_word:
            unique_letters += 1
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))
        else:
            print('Oops! That letter is not in my word:', \
                  get_guessed_word(secret_word, letters_guessed))
            if letters_guessed[len(letters_guessed) - 1] in 'aeuio':
                guesses_left -= 2
            else:
                guesses_left -= 1
        if is_word_guessed(secret_word, letters_guessed) == True:
            total_score = guesses_left*unique_letters
            print('\nCongratulations, you won! Your total score for this game is:', \
                  total_score)
            winning = True
            break
        print(' \n__________________ \n ')
    if winning == False:
        print('Sorry, you ran out of guesses. The word was', secret_word, '.')


def match_with_gaps(my_word, other_word):
    """
    returns False if other_word can't match with my_word,
    otherwise returnes True.
    """
    myword = ''
    for i in range(0, len(my_word)):
        if my_word[i] != ' ':
            myword += my_word[i]
    if len(myword) != len(other_word):
        return False
    for i in range (0, len(other_word)):
        if myword[i] != other_word[i] and myword[i] != '_':
            return False
    return True

def blablabla(my_word, letters_guessed, other_word):
    """
    Helping function for match_with_gaps function.
    """
    myword = ''
    for i in range(0, len(my_word)):
        if my_word[i] != ' ':
            myword += my_word[i]
    for i in range(0, len(myword)):
        if myword[i] == '_':
            if other_word[i] in ''.join(letters_guessed):
                return False
    return True
        
def show_possible_matches(my_word, letters_guessed):
    """
    Prints all words that can be a secret word.
    """
    for word in WORDLIST:
        if match_with_gaps(my_word, word) and blablabla(my_word, letters_guessed, word):
            print(word)


def hangman_with_hints(secret_word):
    """
    Implements the game with hints.
    """
    letters_guessed = []
    unique_letters = 0
    guesses_left = 6
    warnings_left = 3
    winning = False
    print ('Welcome to the game Hangman!')
    print ('I am thinking of a word that is ', len(secret_word), ' letters long.')
    print ('__________________')
    print (secret_word)
    while guesses_left > 0:
        available_letters = get_available_letters(letters_guessed)
        print ('You have', guesses_left ,'guesses left.')
        print ('Available letters:', available_letters)
        letters_guessed += [str.lower(input('Please guess a letter: '))]
        if letters_guessed[len(letters_guessed) - 1] == '*':
            print ('Possible word matches are: ')
            show_possible_matches(get_guessed_word(secret_word, letters_guessed),
            letters_guessed)
        elif len(letters_guessed[len(letters_guessed) - 1]) != 1:
            print('Enter only one letter.')
        elif letters_guessed[len(letters_guessed) - 1] in letters_guessed[0:-1]:
            print("Oops! You've already guessed that letter. You have", \
            warnings_left,'warnings left :')
        elif letters_guessed[len(letters_guessed) - 1] not in available_letters:
            if warnings_left > 0:
                warnings_left -= 1
            else:
                guesses_left -= 1
                
            print('Oops! That is not a valid letter. You have', warnings_left, \
            ' warnings left:', get_guessed_word(secret_word, letters_guessed))
        elif letters_guessed[len(letters_guessed) - 1] in secret_word:
            unique_letters += 1
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))
        else:
            print('Oops! That letter is not in my word:', \
                  get_guessed_word(secret_word, letters_guessed))
            if letters_guessed[len(letters_guessed) - 1] in 'aeuio':
                guesses_left -= 2
            else:
                guesses_left -= 1
        if is_word_guessed(secret_word, letters_guessed) == True:
            total_score = guesses_left*unique_letters
            print('\nCongratulations, you won! Your total score for this game is:', \
                  total_score)
            winning = True
            break
        print(' \n__________________ \n ')
    if winning == False:
        print('Sorry, you ran out of guesses. The word was', secret_word, '.')


if __name__ == "__main__":
    
    #SECRET_WORD = choose_word(WORDLIST)
    #hangman(SECRET_WORD)

    SECRET_WORD = choose_word(WORDLIST)
    hangman_with_hints(SECRET_WORD)
