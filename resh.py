def chet(array):
    a = array.split(', ')
    ch=[]
    for i in a:
        i = int(i)
        if i % 2 == 0:
            ch.append(i)
    print(*ch, sep=' ')

def nechet(array):
    a = array.split(', ')
    ch=[]
    for i in a:
        i = int(i)
        if i % 2 != 0:
            ch.append(i)
    print(*ch, sep=' ')

a = input()
chet(a)
nechet(a)