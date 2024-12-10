def func(n):
	if n == 0:
		return '-'
	
	return func(n-1) + ' '*(3**(n-1)) + func(n-1)

while True:
	try:
		N = int(input())
		print(func(N))
	except:
		break