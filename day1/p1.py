

NUM_POS = 100

def rotateL(num, curr_pos):
    return (curr_pos - num) % NUM_POS

def rotateR(num, curr_pos):
    return (curr_pos + num) % NUM_POS

def rotate(instruction: str, curr_pos: int) -> int:
    dir = instruction[0]
    num= int(instruction[1:])

    print("dir:", dir, "num:", num)
    if dir == 'L':
        return rotateL(num, curr_pos)
    elif dir == 'R':
        return rotateR(num, curr_pos)

def calculate_password(lines):
    curr_pos = 50
    count = 0
    for line in lines:
        print("line:", line.strip())
        curr_pos = rotate(line.strip(), curr_pos)
        print("curr_pos:", curr_pos)
        if curr_pos == 0:
            count += 1
    return count

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
