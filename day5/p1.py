def isFresh(food: int):
    for fRange in fRanges:
        l, r = fRange
        if  l <= food <= r:
            return True
    return False

fRanges = []
all_food = []
with open("data.txt", "r") as f:
    lines = f.read().splitlines()
    print(lines)

    isFood = False

    for line in lines:
        if(line == ''):
            isFood = True
            continue
        if(isFood):
            all_food.append(int(line))
        else: #is range
            l,r = map(int, line.split("-"))
            fRanges.append((l,r))
    
    count=0
    print("ranges", fRanges)
    print("all_foods", all_food)
    for f in all_food:
        isf = isFresh(f)
        print("checking", f, isf)
        if isf:
            count+=1
    print("all fresh", count)
