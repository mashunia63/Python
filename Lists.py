l1 = [1,2,3,4,5,44]
l_names = ['Vadim', 'Igor','Anna']

print(l1)
print(l_names)

l11 = []
l2 = list()

obj_1 = [11,3,'Anna', True, ['','Ivan',23],{"age":30}]

l3=[3]*5
l33=l3

print(l3)
print(l33)

l4 = ['Inna','Anna']
l44 = l4*5

print(l44)

l4 = ['Inna','Anna','Sergey']

l44_0 = l4[0]
l44_1 = l4[1]
l44_2 = l4[2]

print(l44_0)
print(l44_1)
print(l44_2)

l44_n1 = l4[-1]
l44_n2 = l4[-2]
l44_n3 = l4[-3]

print(l44_n1)
print(l44_n2)
print(l44_n3)

l4 = ['Inna','Anna','Sergey']
l4[1] = 'Ira'
print(l4)
n1, n2, n3 = l4
print(l4)
print(n1)
print(n2)
print(n3)

m1 = m2 = l4
m3 = l4.copy() #делать copy

print('l4 - ',l4)
print('m1 - ',m1)
print('m2 - ',m2)
print('m3 - ',m3)

m1[0] = 200
# опасно , поменяло также m2

print('l4 - ',l4)
print('m1 - ',m1)
print('m2 - ',m2)
print('m3 - ',m3)

m3[2] = 200

print('l4 - ',l4)
print('m1 - ',m1)
print('m2 - ',m2)
print('m3 - ',m3)


l4 = ['Inna','Anna','Sergey']
ll = len(l4)
print(ll)

for i in l4[0]:
    print(i)

i = 0
while i < len(l4):
    print(l4[i])
    i+=1

l1 = ['Inna', 'Anna', 'Sergey']
l2 = ['Inna', 'Anna', 'Serge']

if l1 == l2:
    print('l1 =l2')
    print('l1 =',l1)
    print('l2 =', l2)
else: print('l1 != l2')

#add elem in list

l1 = ['Inna', 'Anna', 'Sergey']
l2 = ['Inna', 'Anna', 'Serge']
print(l1)
l1.append(1000)
print(l1)
n=0
for i in l1:
    l1.append(n)
    print(l1)
    n+=1
    if len(l1)>10:
        break

l1 = ['Inna', 'Anna', 'Sergey']
print(l1)
l1.insert(1,1000)
print(l1)

l1 = ['Inna', 'Anna', 'Sergey']
print(l1)
l1.extend([1,1000])
print(l1)


l1 = ['Inna', 'Anna', 'Sergey']
print('Anna', l1.index('Anna'))

for i in l1:
    print (i, l1.index(i))

#delite by index
print(l1)
l1.pop(1)
print(l1)
l1.pop()
print(l1)

l1.remove('Inna')
print(l1)

l1 = ['Inna', 'Anna', 'Sergey']
l1.clear()
print(l1)



l1 = ['Inna', 'Anna', 'Sergey']
print(l1)
a = l1.pop(1)
print(l1)
print('a-',a)


#search by

l1 = ['Inna', 'Anna',[], 'Sergey','Anna']
if "Sergey" in l1:
    print(l1)
    print ("Sergey","OK")

print('count Anna = ', l1.count("Anna"))

#Sort

l1 = ['Inna', 'Anna', 'Sergey','Anna']
l1.sort()
print(l1)

l1.reverse()
print(l1)

l2 = [1,2,3,5,6,7,5,4,3,2343,4,0,-1]
l2.sort()
print(max(l2))
print(l2)
print(l2[3:])
print(l2[:3])
print(l2[-3:])
print(l2[:-3])
print(l2[2:7:2])
print(l2[2:7:1])


#slice

print(l2)

obj_1 = [11,3,'Anna', True, ['','Ivan',23],{"age":30}]
print(obj_1)
print(obj_1)