from collections import Counter
import time

with open('input_test.txt') as f:
    lines = f.read().splitlines()

#print(lines)
lines3 = [[line[0:len(line)//2],line[len(line)//2:len(line)]] for line in lines]


#Holy shit now we are ascending
lines4 = [[''.join(sorted(line[0:len(line)//2])),''.join(sorted(line[len(line)//2:len(line)]))] for line in lines]

#26 letters a to z
#print(ord('A')) # 65 - x = 27 => x = 38
#print(ord('a')) # 97 - x = 1 => x = 96

def doMagic(char):
    if(char.isupper()):
        return ord(char) - 38   
    return ord(char) - 96

# No this doesnt work because of positioning! ARGH!
l1 = [(a,b) for a,b in zip(lines4[0][0],lines4[0][1])]
l2 = [a == b for a,b in zip(lines4[0][0],lines4[0][1])]

#print(''.join(set(lines4[0][0]).intersection(lines4[0][1])))
#print(lines4)
wtf =[''.join(set(hmm[0]).intersection(hmm[1])) for hmm in lines4]

#print(sum([doMagic(you) for you in wtf]))
tic = time.perf_counter()
#Yeah thats right???
with open('input_test.txt') as f:
    lines = f.read().splitlines()
yep = sum([doMagic(you) for you in [''.join(set(hmm[0]).intersection(hmm[1])) for hmm in [[''.join(sorted(line[0:len(line)//2])),''.join(sorted(line[len(line)//2:len(line)]))] for line in lines]]])
toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
#print(yep)

index0 = 0
length = len(lines)
newlines = []
while index0 < length:
    newlines.append([lines[index0 : index0+3]])
    index0 = index0 +3
    #print(index0)

#lines[0 : 3] = [lines[0 : 3]]
#print(newlines)


newyep = sum([doMagic(you) for you in [''.join(set(hmm[0][0]).intersection(hmm[0][1]).intersection(hmm[0][2])) for hmm in newlines]])

print(newyep)
