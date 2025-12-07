

layout = {}
count = 0
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
    
    active_lasers = set([Spos])
    for cpos in layout.keys():
        for lpos in active_lasers.copy():
            if cpos[1] == lpos:
                active_lasers.remove(lpos)
                active_lasers.add(lpos-1)
                active_lasers.add(lpos+1)
                count += 1

    print("active_lasers", len(active_lasers), count)
            

