

layout = {}
with open("data.txt", "r") as f:
    lines = f.read().splitlines() 
    Spos = 0 
    cc = 0
    for i,z in enumerate(lines[0]):
        if z == 'S':
            Spos = cc
            break
        cc+=1

    for r in range(len(lines)):
        for c, v in enumerate(lines[r]):
            if v == '^':
                layout[(r,c)] = '^'
    
    # active_lasers = set([Spos])
    active_lasers = {Spos: 1}
    for cpos in layout.keys():
        for lpos in active_lasers.copy():
            if cpos[1] == lpos:
                val = active_lasers[lpos]
                del active_lasers[lpos]
                active_lasers[lpos-1] = active_lasers.get(lpos-1, 0) + val
                active_lasers[lpos+1] = active_lasers.get(lpos+1, 0) + val
                printPos = (1+cpos[0], 1+cpos[1])
                print("at:",printPos, val)

    count = sum(list(active_lasers.values()))
    print("count", count)
    print("active_lasers", len(active_lasers),count, active_lasers.values())
            

# .......S.......
# .......|.......
# ......1^1...... 2
# ......|........
# .....1^2^1..... 4
# ...............
# ....1^3^3^1.... 8 
# ...............
# ...1^4^3.1^1... 10
# ...............
# ..1^5^4.1^2^1..
# ...............
# .1^1.4^4...1^1.
# ...............
# 1^2^5^8^8^..^.
# 1.2.a.8.8.21.1.

# 1+2+10+8+8+2+1+1