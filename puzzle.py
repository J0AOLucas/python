import random

#I added a list of words that the program can choose randomly
words = ["mosiah", "temple", "church", "pathwayconnect", "prophet", "nephi"]
secret_word = random.choice(words)

guesses_number = 0
hint = "_"
print("Welcome to the word guessing game!")

#Helping the user according to the word in the list
if secret_word == words[0]:
    print("Tip: The word is a name of a prophet")
elif secret_word == words[1]:
    print("The word is a place that the members like to go.")
elif secret_word == words[2]:
    print("The word is a place that the members like to go.")
elif secret_word == words[3]:
    print("The word is a place you use if you want to have success in your life.")
elif secret_word == words[4]:
    print("The word is a name of importants people in this world.")
elif secret_word == words[5]:
    print("Tip: The word is a name of a prophet")

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