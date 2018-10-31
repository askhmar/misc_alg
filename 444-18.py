y=int(input("Input year: "))

if ((y%10)==0) or ((y%10)==1):
        s='white metal '


if ((y%10)==2) or ((y%10)==3):
        s='black water '



if ((y%10)==4) or ((y%10)==5):
        s='blue tree '


if ((y%10)==6) or ((y%10)==7):
        s='red fire '


if ((y%10)==8) or ((y%10)==9):
        s='yellow ground '


yyy=(y-1900)%12

if yyy==0:
        s=s+' rat'
if yyy==1:
        s=s+' bull'

if yyy==2:
        s=s+' tiger'

if yyy==3:
        s=s+' rabbit'

if yyy==4:
        s=s+' dragon'

if yyy==5:
        s=s+' snake'

if yyy==6:
        s=s+' horse'

if yyy==7:
        s=s+' goat'

if yyy==8:
        s=s+' monkey'

if yyy==9:
        s=s+' cock'

if yyy==10:
        s=s+' dog'

if yyy==11:
        s=s+' pig'

print "This year of ",s



