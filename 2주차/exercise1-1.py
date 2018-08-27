def find_earliest(rooms):
    # Implement here
    min_datenum = 99999
    for i in range(0, len(rooms), 2):
        datenum = rooms[i] * 100 + rooms[i+1]
        if datenum < min_datenum:
            min_datenum = datenum

    return min_datenum // 100, min_datenum%100

def read_inputs():
    num_testcases = int(input())
    testcases = []
    for i in range(num_testcases):
        month_dates = [int(x) for x in input().split()]
        testcases.append(month_dates)
    return testcases

def main():
    testcases = read_inputs()
    for testcase in testcases:
        ans = find_earliest(testcase)
        print(ans)

if __name__ == "__main__":
    main()