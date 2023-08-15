#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda - only do things that require single expression
print( (lambda x: x**2 + 5*x + 4) (-4))