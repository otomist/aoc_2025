import math

def di(p1, p2):
    return math.dist(p1, p2)

all_points = []
pd = {}
groups = {}

with open("test.txt", "r") as f:
    lines = f.read().splitlines()
    

    for line in lines:
        s = line.split(",")
        xyz = (int(s[0]), int(s[1]), int(s[2])) 
        all_points.append(xyz)
    for p1 in all_points:
        for p2 in all_points:
            if p1==p2:
                continue
            if p1 not in pd:
                pd[p1] = p2
                continue
            curr_small = pd[p1]
            cdx = di(p1, curr_small)
            dx = di(p1, p2)
            if dx < cdx:
                pd[p1] = p2

    for p1, curr_small in pd.items():
        seen = set(p1)
        nextP = curr_small
        # we can make this better by doing a group check earlyy to 'cahce'
        while nextP not in seen:
            seen.add(nextP)
            nextP = pd[nextP]

        foundKey=None
        for s in seen:
            if s in groups:
                foundKey = s
                break
        if foundKey == None:
            foundKey = seen.pop()

        groups[foundKey] = foundKey
        for p in seen:
            groups[p] = foundKey

    freq={}
    for g in groups.values():
        if g not in freq:
            freq[g] = 1
        else:
            freq[g] += 1
    prd = 1
    vals = sorted(freq.values())
    top3=vals[-3:]
    print('val', vals, math.prod(top3))