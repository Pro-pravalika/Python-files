# filter function filters the given sequence with the help of a function that test each element in the sequence to be true or not.
def fun(variable):
	sequence = ['a','e','i','o','u']
	filtered = filter(fun,sequence)
	for s in filtered:
		print(s)
fun('')