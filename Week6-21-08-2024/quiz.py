print("Question 1")

def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)

print (f(3))

print("Question 2")

# my_list = ['Mary', 'had', 'a', 'little', 'lam']

# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'

# print (my_list(my_list))

print("Question 3")

print("Question 4")

# def function(x=0):
#     return x

# print("Question 5")
# try:
#     value = input("Enter a value: ")
#     print(value/value)
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("very very bad input...")
# except:
#     print("Boo!")

print("Question 6")
# my_tuple = (1, 2, 3)
# my_tuple[1] = my_tuple[1] + my_tuple[0]

print("Question 7")

dictionary = {'one': 'two',
              'three': 'one',
              'two': 'three'}

v = dictionary['one']

for k in range(len(dictionary)):
    v = dictionary[v]

print (v)

print("Question 8")

def func(a, b):
    return a ** a
print(func(2))

print("Question 9")

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return

# print(fun(fun(2)) + 1)

print("Question 10")
def fun(x, y, z):
    return x+ 2 * y + 3 * z

print(fun(0, z=1, y=3))

print("Question 11")
def fun(x):
    x += 1
    return x

x = 2
x = fun(x+1)
print(x)

print("Question 12")
def fun(x):
    global y
    y = x * x
    return y

fun(2)
print(y)

print("Question 13")

def any():
    print(var + 1, end='')

var = 1
any()
print(var)

print("Question 14")

print("Question 15")
def fun(inp=2, out=3):
    return inp * out

print(fun(out=2))

print("Question 16")
x = None
print(x == None)

print("Question 17")
def func_1(a):
    return a ** a

def func_2(a):
    return func_1(a) * func_1(a)

print(func_2(2))


print("Question 18")
def fun():
    print("test")
fun()

print("Question 19")
tup = (1,2,4,8)
tup = tup[1:-1]
tup = tup[0]
print(tup)

print("Question 20")
def fun(a=0, b=0):
    print(a,b)

print("Question 21")
dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) -1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k[0])

print("Question 22")
