import random
number = random.randint(1,10)
name = input("Enter your name: ")
number_guess = 0
print(name + ' Guess a number between 1,10: ' )
while number_guess < 5:
    guess = int(input())
    number_guess += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_guess) + ' tries!')
else:
    print('You did not guess the number, the number was ' + str(number))
print("done")