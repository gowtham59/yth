ax1,ay2=map(int,input().split())
mh3=list(map(int,input().split()))
mh3.sort()
mh3.reverse()
ah4=ay2
z5=0
for i in mh3:
    if(ah4>=i):
        no=int(ah4/i)
        z5=z5+no
        ah4=ah4-no*i
    if ah4==0:
        break
if(ah4==0):
   print(z5)
else:
   print("it's not posiible to select coins ",S)
