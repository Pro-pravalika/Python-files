
from functools import reduce
nums = [10,24,32,47,51,69]
sums = reduce(lambda x,y: x+y,nums)
print(sums)