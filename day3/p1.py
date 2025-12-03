

row = {}

def getBest(s: str, remainingNeeded):
    i=0
    d1 = 0
    MAX = 9
    nextStart = 0
    for i,c in enumerate(s):
        if i == len(s) - remainingNeeded:
            break
        n = int(c)
        if n>d1:
            d1=n
            nextStart = i + 1
        if d1 == MAX:
            break
    return d1, s[nextStart:]





with open("data.txt") as f:
    lines = f.read().split("\n")
    total = 0
    for i,line in enumerate(lines):
        print('==========',i)
        res = getBest(line)
        print("res", res)
        total+=res
    
    print("total", total)


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
