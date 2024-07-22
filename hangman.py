import random 

def game():
    words = ["apple", "banana", "grapes", "watermelon"]
    num = random.randint(0, len(words)-1)
    word = []
    guess = []
    guessed0 = []
    for x in words[num]:
        word.append(x)
        guess.append("_")
        guessed0.append(0)
    
    i = 0
    tries = len(guess) -2
    print(guess, "Is the word")
    print(f"You have {tries} tries to guess the word!")
    print("Type \"exit\" to exit the game")
    while i < len(word)-1:
        if word == guessed0:
            return print(("Words guessed you win!"))
        input_word = input("Enter a letter: ")
        if input_word == "exit":
            return print("Exitting the game")
        if input_word in guess and input_word not in word:
            print("Words already guessed, Guess another!", (guess), tries, "Tries left")
        elif input_word in word:
            pos = word.index(input_word)
            guess[pos] = input_word
            word[pos] = 0
            print(str(guess), tries, "Tries left")
        else:
            print("Does not include that word, Try again!", (guess), tries, "Tries left")
            tries = tries - 1
            i = i + 1


game()