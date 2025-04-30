import random

print("Welcome to the Number Guessing Game!You've 5 chances! Depending on your guess, " \
"I will tell you whether it is greater or lesser than the answer!Let's start the game!")

answer = random.randrange(100)

guessLimit = 5

guessCount = 0

while guessCount < guessLimit:

    guessCount += 1
    guess = int(input('Please Enter your Guess : '))

    if guess == answer:
        print(f'You guessed the answer right in {guessCount} attempt(s)!')
        break

    elif guessCount >= guessLimit and guess != answer:
        print(f'The answer is.....{answer}! Better luck next time')

    elif guess > answer:
        print('Your guess is greater than the answer!')

    elif guess < answer:
        print('Your guess is lesser than the answer!')