c_totals = {}

with open("data.txt", "r") as f:
    lines = f.read().splitlines()
    operaters = [x for x in lines[-1] if x != ' ' and x != '']
    for i,line in enumerate(lines):
        if i == len(lines) -1:
            continue
        clean_line = [int(x) for x in line.split(" ") if x != '']
        for j, num in enumerate(clean_line):
            print("j",j, num)
            if operaters[j] == "+":
                if j not in c_totals:
                    c_totals[j] = 0
                c_totals[j] += num
            elif operaters[j] == "*":
                if j not in c_totals:
                    c_totals[j] = 1
                c_totals[j] *= num
            else:
                print("i",i, operaters)
                raise TypeError("Invalid operator")
        

    total = 0    
    for v in c_totals.values():
        total += v
        print("v", v)
    print("answer: ", total)