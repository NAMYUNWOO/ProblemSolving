from functools import reduce
import math

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def gcd_multi(numbers):
    return reduce(lambda x,y: gcd(x,y), numbers)

def reduced_ratio(ratio):
    divisior = gcd_multi(ratio)
    return [int(x/divisior) for x in ratio]

def make_potion(ratio, added):
    reduced = reduced_ratio(ratio)
    multiplier = max([math.ceil(a/r) for a, r in zip(added,reduced)])
    new_amount = [multiplier * r for r in reduced]
    to_be_added = [n_a - a for n_a, a in zip(new_amount,added)]
    return to_be_added[0], to_be_added[1]

def read_inputs():
    c = int(input())
    test_cases = []
    for test_case in range(c):
        ratio = [int(x) for x in input().split()]
        added = [int(x) for x in input().split()]
        test_cases.append((ratio, added))
    return test_cases

def main():
    test_cases = read_inputs()
    for ratio, added in test_cases:
        ans = make_potion(ratio, added)
        print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()