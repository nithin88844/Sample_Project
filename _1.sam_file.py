print("Hello   World")

def loop(n):
    for i in range(n):
        print(i)

def prime(x):
    for i in range(x):
        if x%i==0:
            print(f"{x} is not a prime number")
    else:
        print(f"{x} is a prime number")