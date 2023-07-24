def primeFactor(num):
    b = 0
    for a in range(num):
        if((a != 0 and a != 1) and (num % a == 0) and (a % 2 != 0 and a % 3 != 0)):
            if(b == 0):
                b = a
            elif (b * a == num):
                print(a)
                return a
            else:
                b = b * a

primeFactor(600851475143)