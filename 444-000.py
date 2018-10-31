year=int(input("year: "))
if year%4==0:
	if year%100==0 and year%400!=0:
		year=365
	else:
		year=366
else:
	year=365
print "count day in year: ",year
