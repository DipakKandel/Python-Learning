from datetime import datetime
from time import sleep

username = input("Enter your name: ")
current_time = datetime.now()
print(f"Hello {username}, You logged in at {current_time.strftime("%H:%M:%S")}")
year_only = current_time.strftime("%Y-%m-%d")
time_only = current_time.strftime("%H Hours %m Minutes and %S Seconds,")

print(year_only)
print(time_only)
sleep(2)
print(f"Session Started : {datetime.now().strftime("%d-%m-%Y | %HH:%MM:%SS")}")



today = datetime.now()
new_year = datetime(year=today.year + 1, month=1, day=1)

diff = new_year - today
print(f"🎉 Days until New Year: {diff.days}")


todays_date = datetime.now()
birthdate = input("Enter your birth date (YYYY-MM-DD) : ")
formatted_bday = datetime.strptime(birthdate,"%Y-%m-%d")

age = todays_date.year - formatted_bday.year
print(age)


date1 = input("Enter A FROM date (YYYY-MM-DD) : ")
date1 = datetime.strptime(date1,"%Y-%m-%d")
date2 = input("Enter A TO date (YYYY-MM-DD) : ")
date2 = datetime.strptime(date2,"%Y-%m-%d")

difference = (date2-date1).days
status = ""
if difference<0:
  status = "PAST"
else:
  status = "FUTURE"

print (f"📅 Date Difference Report\n From: {date1}\n To: {date2}\n Days: {difference} \n Status:{status}")

