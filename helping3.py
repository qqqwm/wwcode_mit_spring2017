def get_available_letters(letters_guessed):
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    available_letters = ''
    for i in all_letters:
        if i not in letters_guessed:
            available_letters += i
    return available_letters
                    

print (get_available_letters(['a', 'b', 'c']))
