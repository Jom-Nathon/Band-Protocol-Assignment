import random

def genTestCase() :
    testCase = "".join(random.choices("R" + "S", k=random.randrange(1, 100)))
    print(testCase)
    return testCase

def checkBoy(boyString) :
    boyList = list(boyString)
    print(boyList)
    status = True

    pointer1 = 0
    pointer2 = 0

    while pointer1 <= (len(boyList)) :
        if boyList[pointer1] == 'R':
            status = False
            print("Bad boy!")
            return status
        elif boyList[pointer1] == 'S':
            while (boyList[pointer2] != 'R') and (pointer2 < len(boyList)-1):
                pointer2 += 1
            if boyList[pointer2] == 'S' and pointer2 == len(boyList)-1:
                status = False
                print("Bad boy!")
                return status
            while boyList[pointer2] == 'R':
                boyList.pop(pointer2)
            boyList.pop(pointer1)
        print(boyList)
    print("Good boy!")
    return status

checkBoy(genTestCase())
