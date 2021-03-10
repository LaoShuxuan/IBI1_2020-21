a=020405
b=190784
c=210310
d=abs(a-c)
e=abs(a-b)
if d>e:
   print("d>e")
elif d==e:
   print("d=e")
else:
   print("d<e")

X=True
Y=False
Z=(X and not Y) or (Y and not X)
if Z==True:
   print("verify Z is true if either X or are true")
W=(X!=Y)
if Z is not W:
   print(Z,"is not the same as",W)
else:
   print("Z is the same as W")
   
