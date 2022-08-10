print("Welcome!")
g = input("Guess the number: ")
guess = int(g)
if guess == 5:
    print("You win")
if guess == 3:
    print("Dam, little bit more")
if guess == 7:
    print("Dam, little bit less")
if guess == 8:
    print("less, dude")
else:
    print("so far...")
print("Game over")
