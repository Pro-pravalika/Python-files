# If you do not know how many keyword arguments, that will be passed into your function by adding two asterisk.


def by_asterisk(**elements):
	print(elements['last_name'])
	print(elements['first_name'])
	print(elements['f_name'])
by_asterisk(first_name='pravalika',last_name='chunarkar',f_name='baburao')