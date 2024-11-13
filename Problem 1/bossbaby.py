import random
import string

testCase = ''.join(random.choices("R" + "S", k=random.choices(string.digits)))
print(testCase)