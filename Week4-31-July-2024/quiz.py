print('Question 1')

nums = [1,2,3]
vals = nums[-1:-2]

print(nums)
print(vals)

print('Question 2')

# my_list = [[0, 1, 2, 3] for i in range (2)]
# print(my_list[2][0])

print('Question 3')

my_list = [3, 1, -2]
print(my_list[my_list[-1]])

print('Question 4')

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

print('Question 5')

i = 0
while i <= 3 :
    i += 2
    print("*")

print('Question 6')

nums = [1,2,3]
vals = nums
del vals[1:2]
print(nums)
print(vals)

print('Question 7')

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)

print('Question 8')
z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

print('Question 9')
for i in range(1):
    print("#")
else:
    print("#")

print('Question 10')
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c + d + e)

print('Question 11')
my_list = [i for i in range(-1,2)]
print(my_list )

print('Question 12')
my_list = [1,2,3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)


print('Question 14')
i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
        break
    print("*")

print('Question 15')
vals = [0,1,2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)

print('Question 16')
my_list = [1,2,3,4]
print(my_list[-3:-2])

print('Question 17')
var = 1
while var < 10:
    print("#")
    var = var << 1

print('Question 18')
vals = [0,1,2]
vals.insert(0,1)
del vals[1]
print(vals)

print('Question 19')
x = 1
x = x == x
print(x)

print('Question 20')
my_list_1 = [1,2,3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0,v)
print(my_list_2)

list = ['cat','rat','bird','dog','elephant']
print(list[0:4])
print(list[2:4])

list(5)
