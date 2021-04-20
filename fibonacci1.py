def fib(num):
	
	a = 0
	b = 1
	sum = 0
	for i in range(0, num-1):
		sum = a+b
		a = b
		b = sum
	return sum

def fibonacci(num):
	if num < 2:
		return num
	return fibonacci(num-1) + fibonacci(num-2)

print(fib(5s))
print(fibonacci(5))