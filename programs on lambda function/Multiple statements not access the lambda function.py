list = [[1,23,4,6],[87,450,200],[876,543,123,100],[2,0,8]]

sort_list = lambda x:(sorted(i) for i in x)
largest_element = lambda x, function : [y[len(y)-1] for y in function(x)]
result = largest_element(list,sort_list)
print(result)
