from random import randint, choice
from string import ascii_letters, ascii_lowercase, ascii_uppercase, punctuation, digits

# Generate random number of length n
def generateNumbers(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def generateLetterString(mode, n):
    if mode == "lowercase":
        return "".join(choice(ascii_lowercase) for i in range(n))
    elif mode == "uppercase":
        return "".join(choice(ascii_uppercase) for i in range(n))
    elif mode == "letters":
        return "".join(choice(ascii_letters) for i in range(n))

def generateSpecialCharString(n):
    return "".join(choice(punctuation) for i in range(n))

def generateString(n):
    return "".join(choice(ascii_letters + digits + punctuation) for i in range(n))


print(generateString(10))