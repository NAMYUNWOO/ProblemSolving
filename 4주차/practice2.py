def n_of_binaries(N):
    #implement here...
    a = 0
    b = 1
    for i in range(1, N):
        (a, b) = (a+b , a)
    return a+b

def main():
    digit = int(input())
    print(n_of_binaries(digit))

if __name__ == '__main__':
    main()