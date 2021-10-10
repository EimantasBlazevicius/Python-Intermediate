# Normal python function
def a_name(x):
    return x + x

# Lambda function
# lambda x: x + x


# Immediately invoked lambda
print((lambda x: x*2)(12))


# Used in filter
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filter(lambda x: x % 2 == 0, list_1)

list(filter(lambda x: x % 2 == 0, list_1))


# Used in Map
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cubed = map(lambda x: pow(x, 3), list_1)
list(cubed)


# Bad vs Good practices

#Bad
triple = lambda x: x*3
#Good
def triple(x):
     return x*3

#Bad
map(lambda x:abs(x), list_1)
#Good
map(abs, list_1)
#Good
map(lambda x: pow(x, 2), list_1)


# lambda line is harder to read than function because of multiline would be more readable
listas = [15, 15, 26, 48, 59, 3, 6]
result = map(lambda x: x if (x == 48 or (x == 3 and "World is awesome" == True)) else 59, listas)
