

NUM_POS = 100

# def rotateL(num, curr_pos):
#     return (curr_pos - num) % NUM_POS

# def rotateR(num, curr_pos):
#     return (curr_pos + num) % NUM_POS

# def rotate(instruction: str, curr_pos: int) -> int:
#     dir = instruction[0]
#     num= int(instruction[1:])

#     print("dir:", dir, "num:", num)
#     if dir == 'L':
#         return rotateL(num, curr_pos)
#     elif dir == 'R':
#         return rotateR(num, curr_pos)

# def calculate_passes(instruction: str, curr_pos: int) -> int:
#     if curr_pos == 0:
#         return 0
#     dir = instruction[0]
#     num= int(instruction[1:])
#     count = 0
#     if dir == 'L' and (curr_pos - num <= 0):
#             count += num // NUM_POS
#     elif dir == 'R' and (curr_pos + num >= NUM_POS):
#             count += num // NUM_POS
#     return abs(count)

def calculate_password(lines):
    count = 0
    pos = 50
    p1, p2 = 0, 0
    for line in lines:
         ticks = int(line[1:])
         delta = -1 if line[0] == 'L' else 1 
         p2 += ((100+ delta*pos)%100 +ticks) // NUM_POS
         pos = (pos + delta*ticks) % NUM_POS
         if pos == 0:
                p1 += 1

    print("p1:", p1)
    print("p2:", p2)
    
    return count

    # curr_pos = 50
    # count = 0
    # for line in lines:
    #     print("line:", line.strip())
    #     passes = 0
    #     # passes = calculate_passes(line.strip(), curr_pos)
    #     curr_pos = rotate(line.strip(), curr_pos)
    #     print("curr_pos:", curr_pos)
    #     if curr_pos == 0:
    #         count += 1
    #     else:
    #         count += passes
    # return count

def main():
    # read in inout1.txt:
    with open("input1.txt", "r") as f:
        lines = f.readlines()
        result = calculate_password(lines)
        print("pass", result)

if __name__ == "__main__":
    main()



# test case:
test_cases = [
    "L68",
    "L30",
    "R48",
    "L5" ,
    "R60",
    "L55",
    "L1" ,
    "L99",
    "R14",
    "L82",
]

print("-------")
print(calculate_password(test_cases))  # Expected output depends on the logic implemented