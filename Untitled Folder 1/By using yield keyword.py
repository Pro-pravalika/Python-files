def gen():
	x = 2
	while True:
		yield x
		x +=1
y = gen()
for i in y:
	if i>=5:
		break
	else:
		print(i,end=' ')