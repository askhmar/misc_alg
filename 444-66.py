s=int(input("Input money: "))

if s<2:
        print "Dont maybe to exchangeable"
       

if (s>=2)and(s<10):
        tt=s//2
        o=s-tt*2
        print "Maybe exchange to", tt, " of 2. But  ",o," is not exchangeable"


if (s>=10)and(s<100):
        t=s//10
        o=s-t*10
        tt=o//2
        o=o-tt*2
        print "Maybe exchange to", t," of 10  and ", tt," of 2. But  ",o," not exchangeable"
        print "Maybe exchange to", s//2," of 2  and ", s%2," not exchangeable"


if (s>=100)and(s<500):
        h=s//100
        o=s-h*100
        t=o//10
        o=o-t*10
        tt=o//2
        o=o-tt*2
        print "Maybe exchange to", h," of 100   and ", t," of 10   and ", tt," of 2. But  ",o," not exchangeable"
        print "Maybe exchange to", s//10," of 10  and ", s%2," not exchangeable"
        print "Maybe exchange to", s//2," of 2  and ", s%2," not exchangeable"

if s>=500:
        fh=s//500
        o=s-fh*500
        h=o//100
        o=o-h*100
        t=o//10
        o=o-t*10
        tt=o//2
        o=o-tt*2
        print "Maybe exchange to", fh, " of 500 and ", h," of 100   and ", t," of 10   and ", tt," of 2. But  ",o," not exchangeable"
        print "Maybe exchange to", s//100," of 100   and ", s//10," of 10   and ", s//2," of 2. But  ",s%2," not exchangeable"
        print "Maybe exchange to", s//10," of 10  and ", s%2," not exchangeable"
        print "Maybe exchange to", s//2," of 2  and ", s%2," not exchangeable"
        
