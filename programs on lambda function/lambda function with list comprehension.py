# to print the 10th table by using list comprehension...


table = [lambda x=x:x*10 for x in range(1,11)]
for each in table:
	print(each())