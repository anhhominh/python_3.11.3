from datetime import datetime

print(datetime.now())
dtime = datetime(2024, 5, 15, 0, 0, 0, 0)
print("Datetime: ", dtime)
print(type(dtime))
dtimestamp = dtime.timestamp()
print("Integer timestamp in seconds: ",
      int(round(dtimestamp)))
 
milliseconds = int(round(dtimestamp * 1000))
print("Integer timestamp in milliseconds: ",
      milliseconds)

date_time = datetime.fromtimestamp(1716347069797/1000)
print("Date time object:", date_time)