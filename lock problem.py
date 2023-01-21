'''
Problem:
You are tasked with unlockign a 3-digit lock and are given the following
rules:

For the numbers 6-8-2, one digit is in the correct place.
For the numbers 6-1-4, one digit is correct, but in the wrong place.
For the numbers 2-0-6, two digits are right but both are in the wrong place.
For the numbers 7-3-8, all  the digits are wrong
For the numbers 3-8-0, one digit is in the wrong place

What are the correct 3 digits?
'''

def test(guess):
    win = True
    [i,j,k] = [*guess]

    #Rule #1 either 6,8,2 is in the correct place
    correct = 0
    if i == "6":
        correct += 1
    if j == "8":
        correct += 1
    if k == "2":
        correct += 1

    if correct != 1:
        win = False

    #Rule #2 6,1,4 must be in the guess, but not in that place
    correct = 0
    if "6" in [j,k]:
        correct += 1
    if "1" in [i,k]:
        correct += 1
    if "4" in [i,j]:
        correct += 1

    if correct != 1:
        win = False

    #Rule #3 2,0,6 two are right, but in wrong place.

    correct = 0

    #"2" in [j,k] "0" in [i,k] "6" in [i,j]
    if "2" in [j,k]:
        correct +=1
    if "0" in [i,k]:
        correct +=1
    if "6" in [i,j]:
        correct +=1

    if correct != 2:
        win = False

    #Rule #4 7 , 3 , 8 are wrong
    for n in ["7","3","8"]:
        if n in [i,j,k]:
            win = False

    #Rule #5 3,8,0 must be in the guess, but not in that place

    correct = 0
    if "3" in [j,k]:
        correct += 1
    if "8" in [i,k]:
        correct += 1
    if "0" in [i,j]:
        correct += 1

    if correct != 1:
        win = False

    if win:
        print(f"{guess} was correct!")
        return win

#Brute force solution
for i in range(10):
    for j in range(10):
        for k in range(10):
            guess = str(i) + str(j) + str(k)
            test(guess)
