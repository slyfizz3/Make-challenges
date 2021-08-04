form="Sunrin{lets_start_reversing}"
form=list(map(ord,form))
array=[]
for i in range(len(form)):
	array.append(form[i]^(0x23+i))
print(array)
print(len(form))