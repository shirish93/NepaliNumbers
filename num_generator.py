
nums = dict()
import math
def makeTable():
    numFile = open(r"Numbers/worded_numbers.txt", 'r')
    numList = [each for each in numFile]
    for each in xrange(1,101):
        print each
        nums[each]=numList[each-1]
    for each in xrange(5):
        nums[pow(10,each+1)]= numList[each+100]
    numFile.close()
    for each in nums:
        print str(each) + ":  "+nums[each].decode('utf-8')
makeTable()
