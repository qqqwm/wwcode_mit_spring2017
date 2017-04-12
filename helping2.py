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
print (get_guessed_word('kitty', ['k', 't', 'o', 'u']))
