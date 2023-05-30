import datetime
now = datetime.datetime.now()
print("Date:", now.date())
print("Day:", now.strftime("%A"))
print("Hour:", now.hour)
print("Minutes:", now.minute)
print("Seconds:", now.second)
