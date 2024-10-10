''' 3.  Write a function that takes three mandatory parameters and two optional parameters. '''


def function(a,b,c,d=1,e=2):
    return (a+b-c*d/e)

result = function(1,2,3)
print(result)