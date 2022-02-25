
# Module of Assignment3_5.py

def ChkPrime(n):
    if n==2:
        return True
    if n==5:
        return True

    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
            elif n%5==0:
                return False
            else:
                return True
    else:
        return False


