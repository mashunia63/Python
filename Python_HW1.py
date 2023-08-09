#print("Hello World!")

n1 = 'Maria'
n2 = 10
n3 = 3.14
n4 = False
n4_4 = True

#list
n5 = [1, 2, True, [33, 'Fly']]
n5_1 = list ("lists")
print (n5)
print (n5_1)


# dictionary - словарь. Ключ - значение
d = {}
d1 = {'dict': 1, 'dictionary': 2}
d2 = dict(short='dict', long='dictionary')
print (d,d1,d2['long'])

n7 = {'name':'Maria',
      'age':34,
      3:'age',
      True: False}
print(n7[True])

# set множество - уникальные значения
set_example = {1, 1, 2, 3, 3, 3}
print (set_example)

#foezenset
person = {"name": "John", "age": 23, "sex": "male"}
print (type(person))
fSet = frozenset(person)
print (type(fSet))
print('The frozen set is:', fSet)

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
print (type(vowels))
fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print(type(fSet))

# frozensets are immutable
#fSet.add('v')



s1= 'Hello'
s2 = "World!"

print (s1,s2,n2)