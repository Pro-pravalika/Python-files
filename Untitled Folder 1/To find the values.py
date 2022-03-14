def test(i,j):
	if i == 0:
		return j
	else:
		return (i-1,i+j)
print(test(5,9))