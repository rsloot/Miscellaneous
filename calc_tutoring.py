from datetime import datetime as dt
import re

def write_to_file(f, today, date_in_file=None, earns=0, old_tot=0,
				  weekday=None, week_total=0):
	# print(date_in_file, today)
	if date_in_file:
		date_in_file = re.sub('[0-9]{1,2}[-][0-9]{1,2}[-][0-9]{4}',
							  today, date_in_file)
	else:
		date_in_file = today

	total_b = float(input('\nMonthly before today? '))
	tot = round(total_b+earns, 2)
	# if Sunday reset week total to 0
	if weekday != 0:
		week_total += (total_b-old_tot)
	## write total before today to file
	## overwriting previous
	f.seek(0)
	f.truncate()
	f.write('%s\n%s\n%.2f' % (today, total_b, week_total))
	return float(week_total+earns), float(tot)

days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
day_map = {i:v for i,v in enumerate(days)}

def main():
	update=False
	###########
	rate = 20 #
	###########
	answer = (input('\nNumber of minutes today? ').split())
	# answer =0
	if len(answer) > 1 and answer[1] == '-u':
		update = True
	mins = float(answer[0])
	earns = mins/60*rate # where rate is to be set based on monthly calculation
	try:
		f = open('last_total.txt', 'r+')
	except Exception as e:
		print(-1)
		tot = float(input("Monthly earnings before today? "))
		print('Total so far: $%.2f' % round(tot+earns,2))

	today = dt.today()
	weekday = dt.weekday(today)%7+1
	today = '%d-%d-%d' % (today.month, today.day, today.year)
	date_in_file = f.readline().strip()
	tot = float(f.readline())
	week_total = float(f.readline().strip())
	if earns == 0 and weekday != 0:
		weekday -=1

	if len(answer) > 1 and answer[1] == '-r': #reset week total -r flag
		weekday = 0
		week_total = 0
		update = True

	if date_in_file:
		if today == date_in_file and not update:
			# print(week_total)
			print("\n - TODAY: $%.2f" % round(earns,2))
			print(' - THRU %s: $%.2f' % (day_map[weekday],
										 round(week_total+earns, 2)))
			print(' - TOTAL: $%.2f' % round(tot+earns,2))
		else:
			print("\n - TODAY: $%.2f" % round(earns,2))
			print(' - THRU %s: $%.2f\n - TOTAL: $%.2f' % (day_map[weekday],
												*write_to_file(f=f, today=today, 
												  date_in_file=date_in_file, 
												  earns=earns, old_tot=tot,
												  weekday=weekday, 
												  week_total=week_total)))
	else:
		print("\n - TODAY: $%.2f" % round(earns,2))
		print(' - THRU %s: $%.2f\n - TOTAL: $%.2f' % (day_map[weekday],
												*write_to_file(f=f, today=today, 
												  date_in_file=date_in_file, 
												  earns=earns, old_tot=tot,
												  weekday=weekday, 
												  week_total=week_total)))
	
	f.close()


if __name__ == '__main__':
	main()