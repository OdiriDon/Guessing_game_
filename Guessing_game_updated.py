import random 

guesstaken = 0

print("Hello! What's your name?")
myname = input()

number = random.randint(0, 20)
print(f"Well, {myname}, I am thinking of a number between 0 and 20.")

for guesstaken in range(6):
    print("Take a guess")
    guess = input()
    guess = float(guess)
    
    if guess < number:
        print("Your guess is too low!")
        
    if guess > number:
        print("Your guess is too high!")
        
    if guess == number:
        break
    
if guess == number:
    guesstaken = str(guesstaken + 1)
    print(f"Good job, {myname}, You guessed my number in {guesstaken} guesses!")
    
if guess != number:
    number = str(number)
    print(f"Nope. The number i was thinking of was {number}")
    
    
    
    
    
    