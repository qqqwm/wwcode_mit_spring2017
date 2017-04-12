
# Name: Sasha Panova


import random
import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def get_guessed_word(secret_word, letters_guessed):
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
    for i in range (0, len(secret_word)):
        if secret_word[i] != get_guessed_word(secret_word, letters_guessed)[i]:
            return False
    return True


def get_available_letters(letters_guessed):
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    available_letters = ''
    for i in all_letters:
        if i not in letters_guessed:
            available_letters += i
    return available_letters
            

def hangman(secret_word):
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
            print("Oops! You've already guessed that letter. You have", warnings_left,'warnings left :')
        elif letters_guessed[len(letters_guessed) - 1] not in available_letters:
            if warnings_left > 0:
                warnings_left -= 1
            else:
                guesses_left -= 1
            print('Oops! That is not a valid letter. You have', warnings_left,' warnings left:', get_guessed_word(secret_word, letters_guessed))
        elif letters_guessed[len(letters_guessed) - 1] in secret_word:
            unique_letters +=1
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))
        else:
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
            if letters_guessed[len(letters_guessed) - 1] in 'aeuio':
                guesses_left -= 2
            else:
                guesses_left -= 1
        if is_word_guessed(secret_word, letters_guessed) == True:
            total_score = guesses_left*unique_letters
            print('\nCongratulations, you won! Your total score for this game is:', total_score)
            winning = True
            break
        print(' \n__________________ \n ')
    if winning == False:
        print('Sorry, you ran out of guesses. The word was', secret_word, '.')


def match_with_gaps(my_word, other_word):
    myword = ''
    for i in range(0, len(my_word)-1):
        if my_word[i] != ' ':
            myword += my_word[i]
    if len(myword) != len(other_word):
        return False
    for i in range (0, len(other_word)):
        if myword[i] != other_word[i] and myword[i] != '_':
            return False
    return True


def show_possible_matches(my_word):
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            print(word)


def hangman_with_hints(secret_word):
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
        if letters_guessed[len(letters_guessed) - 1] == '*':
            print ('Possible word matches are: ')
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif len(letters_guessed[len(letters_guessed) - 1]) != 1:
            print('Enter only one letter.')
        elif letters_guessed[len(letters_guessed) - 1] in letters_guessed[0:-1]:
            print("Oops! You've already guessed that letter. You have", warnings_left,'warnings left :')
        elif letters_guessed[len(letters_guessed) - 1] not in available_letters:
            if warnings_left > 0:
                warnings_left -= 1
            else:
                guesses_left -= 1
                
            print('Oops! That is not a valid letter. You have', warnings_left,' warnings left:', get_guessed_word(secret_word, letters_guessed))
        elif letters_guessed[len(letters_guessed) - 1] in secret_word:
            unique_letters +=1
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))
        else:
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
            if letters_guessed[len(letters_guessed) - 1] in 'aeuio':
                guesses_left -= 2
            else:
                guesses_left -= 1
        if is_word_guessed(secret_word, letters_guessed) == True:
            total_score = guesses_left*unique_letters
            print('\nCongratulations, you won! Your total score for this game is:', total_score)
            winning = True
            break
        print(' \n__________________ \n ')
    if winning == False:
        print('Sorry, you ran out of guesses. The word was', secret_word, '.')


if __name__ == "__main__":
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
