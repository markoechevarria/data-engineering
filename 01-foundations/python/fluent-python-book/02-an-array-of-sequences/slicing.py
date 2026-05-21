l = list(range(10,70,10))
print(l[:2], l[2:])

information = "hello world my name is marko\nhello world my name is percy\nhello world my name is joaqui"

for info in information.split('\n'):
    print(info[slice(23,None)]) # notation a,b,c produces slice(a,b,c)

l = list(range(10))
l[2:5] = [20,30]
del l[5:7]
l[3::2] = [11,22]
l[2:5] = [100]

board = [['_'] * 3 for i in range(3)]
board = [['_'] * 3] * 3
print(board)

### dont
tupla = (12, 13, [3,4,5])
tupla[2] += [6,7,8]
print(tupla)
