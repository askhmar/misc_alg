m=int(input("Input suit of card(1-4): "))
k=int(input("Input card (6-14): "))



if m==1:
        s='piki'
if m==2:
        s='trefi'
if m==3:
        s='bubni'
if m==4:
        s='chervi'


if k==6:
        s='shesterka  '+s

if k==7:
        s='semerka '+s

if k==8:
        s='vosmerka '+s

if k==9:
        s='devyatka '+s

if k==10:
        s='desyatka '+s

if k==11:
        s='valet '+s

if k==12:
        s='dama '+s

if k==13:
        s='korol '+s

if k==14:
        s='tuz '+s

        
print (s)
