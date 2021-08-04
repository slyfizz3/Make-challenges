#Sunrin{345y_r4ns0m3w4r3_r1ght?}
from ctypes import *

enc=open("out.enc","rb").read()
libc=CDLL("msvcrt")
libc.srand(0x1234)
enc=list(map(ord,enc))

for i in range(len(enc)):
	v7=libc.rand()&0xff
	v6=libc.rand()&0xff
	enc[i]^=libc.rand()&0xff
	enc[i]=enc[i]+v6-v7
	enc[i]&=0xff
out=''.join([chr(i)for i in enc])
open("out.png","wb").write(out)