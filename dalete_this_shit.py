import datetime

current_datetime = datetime.datetime.now()
print("Pašreizējais datums un laiks:",current_datetime)

current_date = current_datetime.date()
print("Pašreizejais datums:",current_date)

current_time= current_datetime.time()
print("Pašreizejais laiks:", current_time)

custom_datetime = datetime.datetime(2024,9,30,15,45,30)
print("Konkrēts datums un laiks:",custom_datetime)

start_date=datetime.date(2023,9,1)
end_date=datetime.date(2024,9,30)
date_difference = end_date - start_date
print("Dienu starpība starp datumiem",date_difference.days)

print("Pašreizējais datums un laiks(bez ms):", current_datetime.replace(microsecond=0)) 