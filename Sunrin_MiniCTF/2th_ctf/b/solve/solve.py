import string
b=841541640615299532945052254191892660
table=[]
for i in range(0xff):
	if i>>5==3:
		table.append(i)

flag=""
while b>0:
	flag+=chr(table[b%32])
	b-=b%32
	b//=32
print(flag[::-1])


