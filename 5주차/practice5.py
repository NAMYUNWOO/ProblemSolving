def best_revenue(n, prices):
    best = [0]*n
    best[0] = prices[0]
    for i in range(1, len(best)):
        tmp = []
        for j, price in enumerate(prices):
            if i >= j:
                tmp.append(best[i-(j+1)] + price)
        best[i] = max(tmp)
    return best[-1]
    

def main():
    n = int(input())
    prices = [int(x) for x in input().strip().split(' ')]
    print(best_revenue(n,prices))

if __name__ == '__main__':
    main()
