import random, bisect

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
    if chickenObj.chicken != len(chickenObj.chickenIndexes) :
        print("Invalid input!")
        return None
    
    coverage = 0
    # print("This is rooflen : " + str(chickenObj.roofLength))
    # print("This is chicken : " + str(chickenObj.chicken))
    # print(chickenObj.chickenIndexes)
    for i in range(len(chickenObj.chickenIndexes)) :
        chickenPos = chickenObj.chickenIndexes[i]
        # print("___________________________________")
        # print("this is chickenPos : " + str(chickenPos))
        pointer2 = bisect.bisect_left(chickenObj.chickenIndexes, chickenPos + chickenObj.roofLength) - 1
        # print("this is pointer2 : " + str(pointer2))
        # print("this is i : " + str(i))
        if pointer2 - i + 1 > coverage :
            coverage = pointer2 - i + 1
        # print("this is coverage : " + str(coverage))
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
