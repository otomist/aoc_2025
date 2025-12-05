

fRanges = []
all_food = []

# l -> r-l
d = {}

def addToD(ran: str):
    sl,sr = ran.split("-")
    l = int(sl)
    r = int(sr)
    dx = r-l
    if(l in d):
        d[l] = max(dx, d[l])
    else:
        d[l] = dx

def calcOverlap():
    for l1, dx1 in d.items():
        if d[l1] is None:
            continue
        r1 = l1 + dx1 
        for l2, dx2 in d.items():
            if d[l2] is None:
                continue
            r2 = l2 + dx2
            if l1 == l2:
                continue
            if l2 <= l1 <= r2:
                if r1 > r2:
                    d[l2] = r1 - l2
                d[l1] = None


with open("data.txt", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        if(line == ''):
            break
        addToD(line)
    calcOverlap()

    print("d", d)
    values = list(filter(lambda x: x != None, d.values()))
    print("filtered", values)
    res = sum(values) + len(values)
    print(d.values())
    print("count", res)