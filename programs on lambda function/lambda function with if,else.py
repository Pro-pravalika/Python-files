# lambda function by using if, else conditions..

max = lambda x,y : x if(x>y) else 'not a greater value'
print(max(267,765))


variable  = lambda x,y: x if(x%y==0) else 'not a value'
print(variable(24,2))


multiples = lambda x,y :x if(x==100) else 'not equal'
print(multiples(100,200))
print(multiples(700,200))