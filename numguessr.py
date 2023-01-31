import random_1

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random_1.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Bhai.... kya krrha hai yaar tu...rehn de")
        continue

    if user_guess == random_number:
        print("Bahut tej ho rahe ho")
        break
    else:
        if user_guess > random_number:
            print("Upar kahan jaa rha hai?? Neeche jaa!!")
        else:
            print("Neeche kahan ja rha hai?? Upar ja!!")

print("Chal theek,", guesses, "baar main bataa diya tune")  
