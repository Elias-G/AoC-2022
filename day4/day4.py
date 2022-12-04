from collections import Counter
import time

with open('input_test.txt') as f:
    lines = f.read().splitlines()

def prep(lines):
    lines2 = [line.split(',') for line in lines]
    lines3 = [[line1.split('-'),line2.split('-')] for line1,line2 in lines2]
    lines4 = [([int(line1[0]),int(line1[1])],[int(line2[0]),int(line2[1])]) for line1,line2 in lines3]
    return lines4

def prepSmall(lines):
    linesNewAndImproved = map(doThing(),lines)
    return linesNewAndImproved

def doThing(thing):
    a = thing.split(',')
    b = (map(int(),a[0].split('-')),map(int(),a[1].split('-')))
    return b

def doListThing(lines):
    #glhf
    lines4 = [([int(line1[0]),int(line1[1])],[int(line2[0]),int(line2[1])]) for line1,line2 in [[line1.split('-'),line2.split('-')] for line1,line2 in [line.split(',') for line in lines]]]
    return lines4

def doGoodListThing(lines):
    lines2 =  [[[int(weight) for weight in elf.split('-')] for elf in line.split(',')] for line in lines]
    return lines2

#I tried doing with maps, lost abit of myself doing it, doesnt work, fuck it
def doGoodMapThing(lines):
    """
    lines3 =  list(
        map(
            lambda a : 
                list(map()
                )
                list(
                    map(
                        int(),
                        a.split('-')
                        )
                    )
                    ,str.split(','), lines)
                )
    """
    #str.split(',')
    #list(map(int(),a.split('-'))
    #list(map(lambda x: list(map(lambda t: t.strip(), x.split(',', 1))), lst))
    #return lines3

#print(doGoodListThing(lines))
lines4 = prep(lines)
lines2 = doGoodListThing(lines)
#lines3 = doGoodMapThing(lines)

#print(lines4)
#print(lines2)
#print(lines4 == lines2)

#fully contained if:
# lowest bound lower of same as other bound
# highest bound higher or same as other bound

def doMagic(range1,range2):
    #Cannot assume order
    low1,high1 = range1[0],range1[1]
    low2,high2 = range2[0],range2[1]
    diff1 = high1-low1
    diff2 = high2-low2
    if diff1 >= diff2:
        if high1 >= high2 and low1 <= low2:
            return 1
        else:
            return 0
    elif diff2 > diff1:
        if high2 >= high1 and low2 <= low1:
            return 1
        else:
            return 0
    else:
        return 0

lines5 = sum([doMagic(thing[0],thing[1]) for thing in lines4])
print(lines5)


# Part 2
def doBlackMagic(range1,range2):
    #Cannot assume order
    low1,high1 = range1[0],range1[1]
    low2,high2 = range2[0],range2[1]
    diff1 = high1-low2
    diff2 = high2-low1
    #diff negative => range2 inside of range 1
    if diff1 >= 0:
        if diff2 >=0:
            return 1
        else:
            return 0
    elif diff2 >= 0:
        if diff1 >= 0:
            return 1
        else:
            return 0
    else:
        return 0

lines6 = sum([doBlackMagic(thing[0],thing[1]) for thing in lines4])
print(lines6)
