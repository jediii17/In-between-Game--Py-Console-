from random import randint

print("Welcome To In-Between Game\n")
input("press any to start the game: ")

a = randint(1, 13)
lst = randint(1, 13)
print("\nfirst card", a, "second card", lst)
c = randint(1, 13)

# two number is not identical
if a != lst:
    opt = int(input("\n[1] DEAL or [2] NO DEAL: "))
    print("\nThe third card is ", c)
    if opt == 1:
        if c > a and c < lst or c > lst and c < a:
            print("\nWINNER")
        else:
            print("\nLOSER")
    if opt == 2:
        print("\nstart again")
# two number is identical
else:
    bet = input("\n[H] Higher or [L] Lower: ")
    print("The third card is a", c)
    if bet.upper() == 'H':
        if c > a:
            print("\nWINNER")
        if c < a:
            print("\nLOSER")

    if bet.upper() == 'L':
        if c < a:
            print("\nWINNER")
        if c > a:
            print("\nLOSER")
