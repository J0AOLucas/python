import random

#I added a list of words that the program can choose randomly
words = ["apple", "beach", "guitar", "sister", "mary", "river"]
secret_word = random.choice(words)

guesses_number = 0
hint = "_"
print("Welcome to the word guessing game!")

#Helping the user according to the word in the list
if secret_word == words[0]:
    print("Tip: The word is a red fruit.")
elif secret_word == words[1]:
    print("The word is a place that the people like to go on summer.")
elif secret_word == words[2]:
    print("The word is an instrument with strings.")
elif secret_word == words[3]:
    print("I am your brother, but you are not my brother. Who are you? ")
elif secret_word == words[4]:
    print("Mary's mother had four children. April, May and June were the top three. What is the name of the 4th child?")
elif secret_word == words[5]:
    print("What can run but never walks; he has a bed, but he never sleeps; is born, but does not die?")

print(f"\nYour hint is: {hint * len(secret_word)}")

while True:
    guess = input("\nWhat is your guess? ").lower()
    guesses_number += 1
    if guess == secret_word:
        print("\nCongratulations! You guessed it!")
        print(f"It took you {guesses_number} guesses.")
        break
    else:
        for i, x in enumerate(guess):
            if len(guess) == len(secret_word):
                if guess[i] == secret_word[i]:
                    print(x.upper(), end="")
                elif guess[i] in secret_word:
                    print(x.lower(), end="")
                else:
                    print(x.replace(x,"_"), end="")
            else:
                print("\nSorry, the guess must have the same number of letters as the secret word.")
                break
