with open('input.txt') as f:
    lines = [line.split() for line in f]
rock = "A"
paper = "B" 
scissors = "C"

rockX = "X"
paperY = "Y" 
scissorsZ = "Z"

loss = "X"
draw = "Y"
win = "Z"

map = {
    rock:{
        rockX:3+1,
        paperY:6+2,
        scissorsZ:0+3,
    },
    paper:{
        rockX:0+1,
        paperY:3+2,
        scissorsZ:6+3,
    },
    scissors:{
        rockX:6+1,
        paperY:0+2,
        scissorsZ:3+3,
    }
}

map2 = {
    rock:{
        3+1:rockX,
        6+2:paperY,
        0+3:scissorsZ,
    },
    paper:{
        0+1:rockX,
        3+2:paperY,
        6+3:scissorsZ,
    },
    scissors:{
        6+1:rockX,
        0+2:paperY,
        3+3:scissorsZ,
    }
}

map3 = {
    rock:{
        draw:3+1,#draw
        win:6+2,#win
        loss:0+3,#loss
    },
    paper:{
        loss:0+1,#loss
        draw:3+2,
        win:6+3,
    },
    scissors:{
        win:6+1,
        loss:0+2,#loss
        draw:3+3,
    }
}

def score(char1,char2):
    return map[char1][char2]

score = 0
for thing in lines:
    score = score + map3[thing[0]][thing[1]]

print(sum([map3[thing[0]][thing[1]] for thing in lines]))
print(score)