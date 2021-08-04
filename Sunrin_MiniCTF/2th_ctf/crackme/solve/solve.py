import string,base64
table="0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasd+/=fghjklzxcvbnm"
orige=string.ascii_uppercase+string.ascii_lowercase+string.digits+"+/="
tb=string.maketrans(table,orige)
flag=base64.b64decode("AjSaLewaXhRgRFUdKSvNR7E=F=GfFhSaG=1qHSvqJDICXDvgFjS=HSveLewqR3vv".translate(tb))
print(flag)