def pgcd(a,b):
    if a == 0:
        return(b)
    return pgcd(b%a, a)
