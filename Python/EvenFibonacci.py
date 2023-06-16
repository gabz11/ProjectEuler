def Even(number):
    if(number % 2 == 0):
        return True
    else:
        return False

def Fibonacci(terms):
    a1 = 0
    an = 1
    sum = 0
    for number in range(0,terms):
        if(Even(an) and an < 4000000):
           sum += an
        an = a1 + an
        a1 = an - a1
        print(f"{an} ")
    print(f"Sum of terms: {sum}")

Fibonacci(1000)
