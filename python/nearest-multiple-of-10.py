def nearestMultiple(n: int) -> int:
	# Write your code here.
	# pass
	return (n // 10) * 10 if n % 10 <= 5 else ((n // 10) + 1) * 10