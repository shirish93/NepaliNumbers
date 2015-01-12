
nums = dict()
order= list()
def makeTable():
    global nums
    nums[0]='zero'
    numFile = open(r"Numbers/worded_numbers.txt", 'r')
    numList = [each.strip() for each in numFile]
    start=1000
    for each in xrange(0,100):
        nums[each]=numList[each]
    for each in xrange(5):
        nums[start]= numList[each+100]
        start*=100
    numFile.close()
    global order
    order = numList[-6:]
   
makeTable()
import pdb

def numToNepali(num):
    numF = open(r'Numbers/digits.txt', 'r')
    numList = [each.strip() for each in numF]
    nums= str(num)
    toReturn=''
    for each in nums:
        toReturn = toReturn+numList[int(each)]
    numF.close()
    return "".join(toReturn)

def numToWord(num):
    global nums
    if num<100: return nums[num]
    cur = ""
    temp = num/100
    if temp < 10:
        cur = cur+numToWord(temp)+order[0]+" "+numToWord(int(num-temp*100))
    elif temp<1000:
        cur = cur + numToWord(int(temp/10))+" "+order[1]+ " "+numToWord(int(num-(num/1000)*1000))
    else:
        orders=2
        mult = 1e5
        temp= num/mult
        while (temp>100):
            orders+=1
            mult = mult*100
            temp = temp/100
        cur = cur + numToWord(int(num/mult)) +" "+ order[orders]+" "+numToWord(int(num-int(num/mult) * mult))
    return cur.strip()
