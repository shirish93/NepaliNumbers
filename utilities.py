


def getNext():
    try:
        f = open("next.txt", 'r')
    except:
        setNext(0)
        return 0
    line = [each for each in f]
    f.close()
    if not line: return 0
    else: return int(line[0])
    
def setNext(num):
    f = open("next.txt", "w")
    f.write(str(num))
    f.close()
