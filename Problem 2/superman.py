import random

class testCase :
    def __init__(self, chicken, roofLength, chickenIndexes) -> None:
        self.roofLength = roofLength
        self.chicken = chicken
        self.chickenIndexes = sorted(chickenIndexes)
    
    @classmethod
    def genTestCase(cls):
        roofLength = random.randrange(1,1000001)
        chicken = random.randrange(1,1000000001)
        chickenIndexes = sorted((random.sample(range(1,1000000001), chicken)))
        return cls(chicken, roofLength, chickenIndexes)

def findMaxChicken(chickenObj) :

    ### Invalid data fail save ###
    if chickenObj.chicken != len(chickenObj.chickenIndexes) or chickenObj.roofLength < 0  or chickenObj.chicken > 1000000000 or chickenObj.chicken <= 0 or chickenObj.roofLength > 1000000:
        print("Invalid input!")
        return None
    
    chickenNum = len(chickenObj.chickenIndexes)

    if chickenNum <= 1:
        return chickenNum

    max_chickens = 0
    left = 0

    for right in range(chickenNum):
        while (chickenObj.chickenIndexes[right] - chickenObj.chickenIndexes[left]) >= chickenObj.roofLength:
            left += 1
        max_chickens = max(max_chickens, right - left + 1)
    
    return max_chickens

test1 = testCase(5, 5, [2, 5, 10, 12, 15])
test2 = testCase(6, 10, [1, 11, 30, 34, 35, 37])
test3 = testCase(0, 1, [])
test4 = testCase(1, 1, [15])
test5 = testCase(6, -50, [1, 11, 30, 34, 35, 37])

print("result : " + str(findMaxChicken(test1)))
print("result : " + str(findMaxChicken(test2)))
print("result : " + str(findMaxChicken(test3)))
print("result : " + str(findMaxChicken(test4)))
print("result : " + str(findMaxChicken(test5)))
# print(findMaxChicken(testCase.genTestCase()))
