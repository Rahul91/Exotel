from datetime import datetime

register_date=raw_input()
test_date=raw_input()

date_register=datetime.strptime(register_date, '%Y-%m-%d')
date_test = datetime.strptime(test_date,'%Y-%m-%d')


month1=str(date_test.month)
if len(month1)==1:
	month1='0'+month1
year1=str(date_test.year)
date1=str(date_register.day)
if len(date1)==1:
	date1='0'+date1
startdate=year1+'-'+month1+'-'+date1

if date1=='01':
	month2=month1
	year2=str(date_test.year)
	if (int(year1)%4==0 and month1=='02'):
		date2='29'
	elif(month1=='01' or month1=='03' or month1=='05' or month1=='06' or month1=='08' or month1=='10' or month1=='12'):
		date2='31'
	elif(month1=='04' or month1=='07' or month1=='09' or month1=='11'):
		date2='30'
	else:
		date2='28'

else:
	month2=str(date_test.month+1)
	if len(month2)==1:
		month2='0'+month2
	year2=str(date_test.year)
	date2=str(date_register.day)
	if len(date2)==1:
		date2='0'+date2
	
enddate=year2+'-'+month2+'-'+date2

print startdate
print enddate