import elice_utils

def fib(n):
    if 1 == n:
        return 1
    elif 0 == n:
        return 0
    else:
        return fib(n-1) + fib(n-2)

def main():
    k = int(input())
    for i in range(k):
        n = int(input())
        print(fib(n))
	
if __name__ == "__main__":
    main()
