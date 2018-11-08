#Generates all prime numbers, up to the input
print("Enter a number to generate all primes up to the input")
num = input() #Number to stop checking for prime numbers at
for i in range (1, int(num), 2): #Step 2, as an even number can't be prime
    prime = False
    for j in range (2, i):
        if i % j != 0:
            prime = True
        else:
            prime = False
            break
    if prime:
        print(str(i) + " is prime")
    #else:
    #    print(str(i) + " is not prime")
