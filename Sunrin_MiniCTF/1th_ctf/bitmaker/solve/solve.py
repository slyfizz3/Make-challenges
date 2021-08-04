#Sunrin{y0u_4r3_g00d_b1t_m4k3r!!}
from ctypes import *
sbox1=[i for i in range(0x100)]
dec1box=[[[0 for i in range(8)] for j in range(8)]for k in range(4)]
table1=[0]*256
table2=[0]*256
def rc4(data, key):
    res = []
    S = []
    for i in range(256):
        S.append(i)
    j = 0
    for i in range(256):
        j = (j + S[i] + key[(i % len(key))]) % 256
        S[j], S[i] = S[i], S[j]
    i = 0
    j = 0
    for b in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[j], S[i] = S[i], S[j]
        K = S[((S[i] + S[j]) % 256)]
        res.append(K ^ b)

    return res

def gensbox1():
    libc=CDLL("libc.so.6")
    libc.srand(1)
    for i in range(256):
        b=libc.rand()&0xff
        sbox1[i],sbox1[b]=sbox1[b],sbox1[i]

def gensbox2():
    for i in range(len(sbox2)):
        for j in range(len(sbox2[i])):
            sbox2[i][j][0]=i
            sbox2[i][j][1]=j
    
    for i in range(len(sbox2)):
        for j in range(len(sbox2[i])):
            a=sbox1[i]%8
            b=sbox1[j]%8
            sbox2[i][j],sbox2[a][b]=sbox2[a][b],sbox2[i][j]

def tobinary(inp):
    for i in range(len(inp)):
        cc=inp[i]
        for j in range(8):
            table1[i*8+7-j]=cc&1
            cc>>=1

def setbox():
    for i in range(4):
        for j in range(8):
            for k in range(8):
                dec1box[i][j][k]=table1[i*64+j*8+k]

def dec1():
    for i in range(4):
        for j in range(8):
            for k in range(8):
                table2[sbox1[i*64+j*8+k]]=dec1box[i][j][k]

def tostring():
    out=[]
    for i in range(len(table2)//8):
        oo=0
        for j in range(8):
            oo+=table2[i*8+j]<<j
        out.append(oo)
    out=''.join([chr(i)for i in out])
    return out

if __name__ == "__main__":
    enc=open("out.txt","rb").read()
    enc=list(map(ord,enc))
    key=list(map(ord,"Sunrins"))  
    enc=rc4(enc,key)
    gensbox1()
    tobinary(enc)
    setbox()
    dec1()
    out=tostring()
    print(out)