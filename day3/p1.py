

row = {}

def getBest(s: str, remainingNeeded):
    i=0
    d1 = 0
    MAX = 9
    nextStart = 0
    for i,c in enumerate(s):
        if i >= len(s)+1 - remainingNeeded:
            break
        n = int(c)
        if n>d1:
            d1=n
            nextStart = i + 1
        if d1 == MAX:
            break
    return d1, s[nextStart:]


def calc(line: str):
    digitsNeeded = 12
    s=line
    res = []
    while digitsNeeded>0:
        digit, s = getBest(s, digitsNeeded)
        digitsNeeded-=1
        res.append(str(digit))
    return int("".join(res))

with open("data.txt") as f:
    lines = f.read().split("\n")
    total = 0
    for i,line in enumerate(lines):
        res = calc(line)
        print("res", res)
        total+=int(res)
    
    print("total", total)
    print("diff", 3121910778619 - total)

    # 3121910778619


# def p1(line: str):
#     i=0
#     d1,d2 = 0,-1
#     MAX = 9
#     nextStart = 0
#     for i,c in enumerate(line):
#         if i == len(line) - 1:
#             break
#         n = int(c)
#         if n>d1:
#             d1=n
#             nextStart = i + 1
#         if d1 == MAX:
#             break

#     print(nextStart)
#     nextDigits = line[nextStart:]
#     print("nextDigits", nextDigits)
#     for i,c in enumerate(nextDigits):
#         n = int(c)
#         if n>d2:
#             d2=n
#         if d2 == MAX:
#             break
#     print("d1d2,",d1,d2)
#     return (d1 * 10) + d2
