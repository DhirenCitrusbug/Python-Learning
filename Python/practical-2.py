a = [['$','#','#','$','#'],['%','%','%','#','#'],['$','$','%','$','%']]

x = a[0].count('$')
print(x)
swap = 0
for i in a:
    if i.count('$') != 0 and a.index(i)!=0:
        for j in range(i.count('$')):
            swap += 1

print(swap)


y = a[1].count('%')
print(y)
for i in a:
    if i.count('%') != 0 and a.index(i)!=1:
        for j in range(i.count('%')):
            swap += 1


print(swap)


z = a[2].count('#')
print(z)
for i in a:
    if i.count('#') != 0 and a.index(i)!=2:
        for j in range(i.count('#')):
            swap += 1

print(swap)

























# a1 = []
# for y in a:
#     for x in y:
#         a1.append(x)
# print(a1)
# pr = {'$':1,'%':2,
# '#':3,}
# step = 0
# for i in range(len(a1)-1):
#     for j in range(len(a1)-1-i):
#         if pr[a1[j]]>pr[a1[j+1]]:
#             a1[j],a1[j+1] = a1[j+1],a1[j]
#             step += 1
# print(a1)


# a2 = [[],[],[]]
# for i in a1:
#     if i == '$':
#         a2[0].append(i)
#     if i == '%':
#         a2[1].append(i)
#     if i == '#':
#         a2[2].append(i)

# print(a2,step)

# if True:
#     x1 = a[0].count('$')
#     x2 = a[1].count('$')
#     x3 = a[2].count('$')
#     print(x1,x2,x3)
#     y1 = a[0].count('%')
#     y2 = a[1].count('%')
#     y3 = a[2].count('%')
#     print(y1,y2,y3)
#     z1 = a[0].count('#')
#     z2 = a[1].count('#')
#     z3 = a[2].count('#')
#     print(z1,z2,z3)
#     def repl(x,y):
#         for i in range(x):
#             a[0][a[0].index('$')],a[1][a[1].index('#')] = a[1][a[1].index('#')],a[0][a[0].index('$')]
#     # for i in range(x1):
#     #     a[0][a[0].index('$')],a[1][a[1].index('#')] = a[1][a[1].index('#')],a[0][a[0].index('$')]
#     print(a)
#     x1 = a[0].count('$')
#     x2 = a[1].count('$')
#     x3 = a[2].count('$')
#     print(x1,x2,x3)
#     y1 = a[0].count('%')
#     y2 = a[1].count('%')
#     y3 = a[2].count('%')
#     print(y1,y2,y3)
#     z1 = a[0].count('#')
#     z2 = a[1].count('#')
#     z3 = a[2].count('#')
#     print(z1,z2,z3)
    

# repl(x2,y3) 