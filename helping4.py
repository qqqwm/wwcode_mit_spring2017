my_word = '_ ppl_ '
other_word = 'apple'
wordlist = ['apple', 'applr', 'fret']


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
                    

show_possible_matches(my_word)
