a = [('c',1),('a',4),('b',2),('d',3)]

print(a)
a = sorted(a, key=lambda x: x[1])
print(a)

a = sorted(a, key=lambda x: x[0], reverse=True)
print(a)