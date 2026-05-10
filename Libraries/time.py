import time

start_time = time.perf_counter() # Execution time, highly accurate, used for benchmarking
print(start_time) # 0.0491393

epochs = time.time() # Seconds since 1970 Jan 1, 00:00:00 (UTC)
print("Current time in seconds since epoch =", epochs) # 1771742122.3487928


# ctime returns time in our current local time zones in str type
# ctime takes seconds as argument and returns time since 1970 Jan 1, 00:00:00 (UTC)
# default argument value is time.time() meaning it will give current time
print(time.ctime(0)) # Thu Jan  1 05:30:00 1970 
# Equivalent to time.ctime(time.time())
print(time.ctime()) # Sun Feb 22 12:05:22 2026


# Just like ctime but returns struct_time instead of str
print(time.localtime(0)) # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=5, tm_min=30, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
# Equivalent to time.localtime(time.time())
print(time.localtime()) # time.struct_time(tm_year=2026, tm_mon=2, tm_mday=22, tm_hour=12, tm_min=5, tm_sec=22, tm_wday=6, tm_yday=53, tm_isdst=0)


# Just like localtime but instead of local time zone, it uses UTC/ GMT time zone
print(time.gmtime(0)) # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
# Equivalent to time.gmtime(time.time())
print(time.gmtime()) # time.struct_time(tm_year=2026, tm_mon=2, tm_mday=22, tm_hour=6, tm_min=35, tm_sec=22, tm_wday=6, tm_yday=53, tm_isdst=0)


# converts time.struct_time object to epochs (seconds)
print(time.mktime(time.localtime())) # 1771742122.0

# strftime is used to convert time.stuct_time object into your required format of string
# Abbreviations can be foudn here, No need to memorize https://www.geeksforgeeks.org/python/python-strftime-function/
print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())) # Sun, 22 Feb 2026 12:11:20


# converts str time to time.struct_time object
print(time.strptime(time.ctime())) # time.struct_time(tm_year=2026, tm_mon=2, tm_mday=22, tm_hour=12, tm_min=5, tm_sec=22, tm_wday=6, tm_yday=53, tm_isdst=-1)


for i in range(5):
    print(i)
    time.sleep(1) # defines delay of time in execution of seconds.


# Approximate code execution time, not very accurate
print(time.time() - epochs) # 0.018715381622314453 

# Highly accurate code execution time
print(time.perf_counter()) # 0.0564354

# Execution time between start_time and now
print(time.perf_counter() - start_time) # 0.007430800000000001