def reserve_rooms(month_dates):
    rooms = []
    for md in month_dates:
        start = md[0] * 100 + md[1]
        end = md[2] * 100 + md[3]
        rooms.append((start, end))
    start = 201
    end = 201
    rooms = sorted(rooms)
    ans = 1
    for s, e in rooms:
        if s > end:
            break
        if s <= start:
            if e > end:
                end = e
        else:
            if e > end:
                start = end
                end = e
                ans += 1
        if end > 1031:
            break
    if end > 1031:
        return ans
    return 0

def read_inputs():
    num_room = int(input())
    rooms = []
    for room in range(num_room):
        month_dates = [int(x) for x in input().split()]
        rooms.append(month_dates)
    return rooms

def main():
    rooms = read_inputs()
    ans = reserve_rooms(rooms)
    print(ans)

if __name__ == "__main__":
    main()