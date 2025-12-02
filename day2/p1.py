



def invalid_p1(num):
    s = str(num)
    if len(s) % 2 != 0:
        return False
    
    window_size = len(s) // 2
    if s[:window_size] == s[window_size:]:
        return True

    return False


def invalid_p2(num):
    s = str(num)
    if len(s) % 2 != 0:
        return False
    
    window_size = len(s) // 2
    if s[:window_size] == s[window_size:]:
        return True

    return False

fname = "data.txt"
# fname = "test_data.txt"

with open(fname, "r") as f:
    data_ranges = f.read().strip().split(",")
    total = 0
    for data_range in data_ranges:
        start, end = map(int, data_range.split("-"))
        for i in range(start, end + 1):
            if invalid_p2(i):
                total += i
                
    print("total:", total)

