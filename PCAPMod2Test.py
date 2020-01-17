#
#           This program is test code written during Cisco class (17/1/20)
#           Write the name of a method/function in Main with () to call it 
#
#

def questionOne():
    i =2 

    while i >= 0:
        print("*")
        i -= 2

def questionThree():
    for i in range(-1, 1):
        print("#")

def questionFive():
    lst = [3, 1, -1]
    lst[-1] = lst[-2]
    print(lst)

def questionTen():
    L = [0, 1, 2, 3]
    x = 1
    for e in L:
        x *= e
    print(x)

i = 0

def storage1():
    while(i <= 5):
        i += 1
        if i % 2 == 0:
            break
        print("*")

def storage2():
    var = 1
    while var < 10:
        print("#")
        var = var << 1

def storage3():
    a = 1
    b = 0
    c = a & b
    d = a | b
    e = a ^ b
    print(c + d + e)

def storage4():
    list_numbers = [1,2,3,4,5,6,7,8]

    print(list_numbers[1:3])
    print(list_numbers[:4])
    print(list_numbers[5:])
    print(list_numbers[:-5])

def storage5():
    lst = [1,2,3,4]
    print(lst[-3:-2])

def storage6():
    l1 = [1,2,3]
    for v in range(len(l1)):
        l1.insert(1,l1[v])
    print(l1)

def storage7():
    L = [i for i in range(-1,2)]
    print(L)

def storage8():
    T = [[3-i for i in range(3)] for j in range(3)]
    s = 0
    for i in range(3):
        s += T[i][i]
    print(s)

def storage9(): # causes runtime error
    L = [[0, 1, 2, 3] for i in range(2)]
    print(L[2][0]) #list is not within index - causes error


# << - bit shift operator ()
# bin(0b1111 << 1) == 0b11110
# bin(0b1111 << 2) == 0b111100
#
#       "A left shift by n bits == multiplication by pow(2,n). "
#       "A long integer is returned if the result exceeds the range of plain integers."

def shiftTest():
    a = 1
    for i in range(3):
        a << i
        i << i
        print(a)
    print(a)
    print(i)

def Main():
    print("Hello")
    
Main()

