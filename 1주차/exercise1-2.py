def sieve_of_eratosthenes(max_hi):
    factors_counts = [0]*(max_hi+1)
    for i in range(1, max_hi+1):
        for j in range(i, max_hi+1, i):
            factors_counts[j] += 1

    return factors_counts

def print_answers(n, lo, hi, factors_counts):
    return factors_counts[lo:hi+1].count(n)

def read_inputs():
    c = int(input())
    test_cases = []
    max_hi = 0
    for test_case in range(c):
        line = input()
        test_case = [int(x) for x in line.split()]
        if max_hi <= test_case[2]:
            max_hi = test_case[2]
        test_cases.append(test_case)

    return test_cases, max_hi

def main():
    test_cases, max_hi = read_inputs()
    factors_counts = sieve_of_eratosthenes(max_hi)
    for tc in test_cases:
        n, lo, hi = tc
        print(print_answers(n, lo, hi, factors_counts))

if __name__ == "__main__":
    main()