print("Welcome to the Palindrome checker!")

def palind(r):

    e = len(r) - 1
    s = 0

    while (s<e):


        if(r[s]!=r[e]):

            False

        e-=1
        s+=1

    return True

r = (1, 2, 3, 3, 2, 1)

if (palind(r)):
    print(f"The tuple {r} is flip flop!")
else:
    print(f"The tuple {r} is not flip flop!")