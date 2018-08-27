LIMIT_NUMBER = 1000000007

def pow_log(m, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0 :
            t = pow_log(m, n // 2)
            if t * t > LIMIT_NUMBER:
                return t * t % LIMIT_NUMBER
            else:
                return t * t
        else:
            return m * pow_log(m, n - 1)

def pow_linear(m, n):
	if n > 0:
		t = m * pow_linear(m, n - 1)
		if t > LIMIT_NUMBER:
			return t % LIMIT_NUMBER
		else:
			return t
	else:
		return 1

def main():
	'''
	Do not change this code
	'''
	m = int(input())
	n = int(input())

	print(pow_log(m, n))
	print(pow_linear(m, n))

if __name__ == "__main__":
	main()
