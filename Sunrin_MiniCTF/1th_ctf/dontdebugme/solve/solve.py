from ctypes import *
libc=CDLL("msvcrt")
libc.srand(1)
arr1=[34, 78, 212, 174, 28, 154, 239, 203, 58, 189, 142, 28, 227, 214, 238, 197, 227, 7, 24, 74, 237, 44, 67, 178, 84, 112, 107, 42, 67, 24, 103, 165, 10, 105, 48, 231]
arr2=[82, 163, 197, 48, 83, 23, 169, 40, 41, 60, 252, 120, 119, 15, 121, 109, 7, 54, 85, 172, 4, 130, 66, 27, 180, 221, 112, 146, 142, 39, 206, 80, 58, 156, 131, 98]
select=1
if select==1:
    for i in range(len(arr1)):
       arr1[i]-=23
       arr1[i]&=0xff
       arr1[i]^=123
       arr1[i]&=0xff
       arr1[i]+=10
       arr1[i]&=0xff
       arr1[i]^=libc.rand()
       arr1[i]&=0xff
    print(arr1)
    print(''.join([chr(i)for i in arr1]))
else:
    for i in range(len(arr2)):
        arr2[i]^=libc.rand()
        arr2[i]&=0xff
        arr2[i]-=58
        arr2[i]&=0xff
        arr2[i]^=90
        arr2[i]&=0xff
        arr2[i]+=83
        arr2[i]&=0xff
    print(arr2)
    print(''.join([chr(i)for i in arr2]))