def is_word_guessed(secret_word, letters_guessed):
    for i in range (0, len(secret_word)):
        if secret_word[i] != letters_guessed[i]:
            return False
    return True
        
print(is_word_guessed('app', ['y', 'p', 'p']))
