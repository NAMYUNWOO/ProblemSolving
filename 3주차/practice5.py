def findMaxMeeting(li):
    sorted_li = sorted(li, key=lambda x: x[1])
    curEnd = 0
    ans = 0
    for case in sorted_li:
        if curEnd <= case[0]:
            ans += 1
            curEnd = case[1]

    return ans
