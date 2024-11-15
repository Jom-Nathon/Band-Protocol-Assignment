import random

class testCase :
    def __init__(self, chicken, roofLength, chickenIndexes) -> None:
        self.roofLength = roofLength
        self.chicken = chicken
        self.chickenIndexes = sorted(chickenIndexes)
    
    @classmethod
    def genTestCase(cls):
        roofLength = random.randrange(1,100001)
        chicken = random.randrange(1,100000001)
        chickenIndexes = sorted((random.sample(range(1,100000001), chicken)))
        return cls(chicken, roofLength, chickenIndexes)

def findMaxChicken(chickenObj) :

    ### Invalid data fail save ###
    if chickenObj.chicken != len(chickenObj.chickenIndexes) or chickenObj.roofLength < 0 :
        print("Invalid input!")
        return None
    
    coverage = 0
    right = 0
    left = 0

    while right < len(chickenObj.chickenIndexes) :
        if chickenObj.chickenIndexes[right] - chickenObj.chickenIndexes[left] < chickenObj.roofLength :
            coverage = max(coverage, right - left + 1)
            right += 1
        else :
            left += 1

    return coverage

# test1 = testCase(5, 5, [2, 5, 10, 12, 15])
# test2 = testCase(6, 10, [1, 11, 30, 34, 35, 37])
# test3 = testCase(1, 1, [37])
# test4 = testCase(6, -50, [1, 11, 30, 34, 35, 37])

# print("result : " + str(findMaxChicken(test1)))
# print("result : " + str(findMaxChicken(test2)))
# print("result : " + str(findMaxChicken(test3)))
# print("result : " + str(findMaxChicken(test4)))
print(findMaxChicken(testCase.genTestCase()))
