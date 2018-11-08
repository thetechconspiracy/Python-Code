# Calculates with the Collatz Conjecture for all numbers up to 65535
#input = input()
for i in range (2, 65535):
    input = i
    while input != 1:
        if input % 2 == 0: #input is even
            input /= 2
        else: # input is odd
            input *= 3
            input += 1
        print(input)
    print("\t\t\tDone with " + str(i))
