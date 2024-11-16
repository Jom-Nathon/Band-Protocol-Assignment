import random

def genTestCase() :
    testCase = "".join(random.choices("R" + "S", k=random.randrange(1, 1000001)))
    return testCase

def checkBoy(boyString) :
    try :
        if boyString[0] == 'R':
            return "Bad boy"
    except IndexError :
        print("Empty List!")
        return "Good boy"
    
    shotCount= 0
    remainingLength = len(boyString)

    for char in boyString:
        remainingLength -= 1
        if char == 'S':
            shotCount += 1
        else:
            shotCount = max(0, shotCount - 1)

        if shotCount > remainingLength :
            return "Bad boy"

    return "Good boy"

test_cases = [
    "SRSSRRR",  # Good boy
    "RSSRR",    # Bad boy (starts with R)
    "SSSRRRRS", # Bad boy (last S has no revenge)
    "SRRSSR",   # Bad boy (last S has no revenge)
    "SSRSRR",    # Good boy
    "S",        # Bad boy
    "R",        # Bad boy
    ""          # Empty
]

for test in test_cases:
    print(f"{test}: {checkBoy(test)}")

# print(checkBoy(genTestCase()))
