def factorial(n):
    if n < 0:
        return "Invalid Input"
        
    if 1 == n:
        return 1
    else:
        return n * factorial(n-1)

def main():
    testCase = int(input())
    for i in range(testCase):
        x = int(input())
        y = factorial(x)
        print(y)
if __name__ == "__main__":
    main()
