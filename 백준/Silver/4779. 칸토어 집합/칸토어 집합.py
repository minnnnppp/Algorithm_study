def func(n):
	if n == 0:
		print('-', end = "")
		return
	
	func(n-1) 
	print(' '*(3**(n-1)), end = "")
	func(n-1)

while True:
	try:
		N = int(input())
		func(N)
		print()
	except:
		break