print('Question 1')
lst = [i for i in range (-1, -2)]
print(lst)

print('Question 2')
y = "3"
x = "6"
print (x + y)

print('Question 3')
z = 0
y = 10
x = y < z and z > y or y > z and z < y
print (x)

print('Question 4')
tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

print('Question 5')
lst = [[x for x in range(3)] for y in range(3)]
for r in range(3):
    for c in range(3):
        if lst[r] [c] % 2 != 0:
            print("#")

print('Question 6')
#foo = (1,2,3)
#foo.index(0)

print('Question 7')
#my_tuple = (1, 2, 3, 4)
#my_tuple[1] = my_tuple[1] + my_tuple[0]

print('Question 8')
nums = [1,2,3]
vals = nums
print(nums)
print(vals)

print('Question 9')
# i = 0
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")

print('Question 10')
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)

print('Question 11')
dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)

for x in dct.keys():
    print(dct[x][1], end="")


print('Question 12')
dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]

print(v)

dd = {"1": "0", "0": "1"}

print('Question 13')
for x in dd.values():
    print(x, end="")

print('Question 14')
#print(Hello, World!)

print('Question 15')
x = 1
y = 2

x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)

print('Question 16')
print("a", "b", "c", sep="sep")

print('Question 18')
# def function_1(a):
#     return None

# def function_2(a):
#     return function_1(a) * function_1(a)

# print(function_2(2))

print('Question 19')
# def func(a, b):
#     return b ** a

# print(func(b=2, 2))

print('Question 20')
def fun(a, b, c=0):
    return
fun(0,1,2)

print('Question 21')
print('Question 22')
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)

print(fun(0, 3))

print('Question 23')
def fun(inp=2, out=3):
    return inp * out

print(fun(out=2))


print('Question 24')
nums = [1, 2, 3]
vals = nums
del vals[:]
print(vals)
print(nums)

print('Question 25')

# try:
#     print(5/0)
#     break
# except:
#     print("Sorry, something went wrong...")
# except (ValueError, ZeroDivisionError):
#     print("Too bad...")

print('Question 26')
x = float(2)
y = float(4)
print(y ** (1 / x))

print('Question 27')
print(1 // 2)

print('Question 28')
x = 3
y = 2
x = x ** y
x = x % y
y = y % x
print(y)

print('Question 29')
print('Question 30')
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2

print(fun(fun(2)))

print('Question 31')
# try:
#     value = input("Enter a value: ")
#     print(int(value) / len(value))
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("Very very bad input...")
# except:
#     print("Booo!")


print('Question 32')
my_list = [x * x for x in range(5)]

def fun(lst):
    del lst[2]
    return lst

print(fun(my_list))

print('Question 33')
my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)

print('Question 34')
x = 1 // 5 + 1 / 5
print(x)