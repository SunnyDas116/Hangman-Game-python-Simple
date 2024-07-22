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
    print(guess)
    while i < len(word)-1:
        if word == guessed0:
            return print(("Words guessed you win!"))
        input_word = input("Enter a letter: ")
        if input_word == "exit":
            return print("Exitting the game")
        if input_word in guess and input_word not in word:
            print("Words already guessed, Guess another!", str(guess), str(word))
        elif input_word in word:
            pos = word.index(input_word)
            guess[pos] = input_word
            word[pos] = 0
            print(str(guess))
        else:
            print("Does not include that word, Try again!", (guess))
            i = i + 1


game()