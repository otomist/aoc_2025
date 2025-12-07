rc_v = {}
longest = {}
c_totals = {}
operaters = []
col_after_operations = {}

ccount = 0
with open("data.txt", "r") as f:
    lines = f.read().splitlines()
    operaters = [x for x in lines[-1] if x != ' ' and x != '']
    for r,line in enumerate(lines):
        if r == len(lines) -1:
            continue
        rev_strs_list = [x for x in line.split(" ") if x != '']

        ccount = len(rev_strs_list)
        for c, num in enumerate(rev_strs_list):
            if c not in longest:
                longest[c] = 1 
            rc_v[(r,c)] = num
            longest[c] = max(longest[c], len(num))
            if operaters[c] == "+":
                if c not in c_totals:
                    c_totals[c] = 0
            elif operaters[c] == "*":
                if c not in c_totals:
                    c_totals[c] = 1


    values = {}
    for r,line in enumerate(lines):
        if len(lines)-1 == r:
            continue
        pastLength = 0
        for col in range(len(operaters)):
            leng = longest[col]
            seg = line[pastLength:pastLength+leng]
            values[(r,col)] = seg
            pastLength += leng+1


    for c in range(ccount):

        strVals =[values[r,c] for r in range(len(lines)-1)]
        vert_str_nums = {}
        for s in strVals:
            digitPos = 0
            for dstr in s:
                if dstr != ' ':
                    if digitPos not in vert_str_nums:
                        vert_str_nums[digitPos] = ''
                    vert_str_nums[digitPos] += dstr 
                digitPos +=1
        if operaters[c] == "*":
            for v in vert_str_nums.values():
                if(c not in col_after_operations):
                    col_after_operations[c] = 1
                col_after_operations[c] *= int(v) 
        elif operaters[c] == "+":
            for v in vert_str_nums.values():
                if(c not in col_after_operations):
                    col_after_operations[c] = 0
                col_after_operations[c] +=  int(v)
        else:
            raise ValueError
            
        print("col",c,": ",vert_str_nums.values())
        print("col_after_operations", col_after_operations.values())
print("final:", sum(col_after_operations.values()))