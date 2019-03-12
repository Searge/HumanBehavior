import time

time_string = "7:10 17 March, 2017"
time_tuple = time.strptime(time_string, "%H:%M %d %B, %Y")
# time.struct_time(tm_year=2017, tm_mon=3, tm_mday=17,
#                  tm_hour=7, tm_min=10, tm_sec=0,
#                  tm_wday=4, tm_yday=76, tm_isdst=-1)

bb_bday = (2017, 3, 17, 7, 10, 0, 6, 76, -1)
bb_bday_nix = time.mktime(bb_bday)

bb = time.localtime(bb_bday_nix)
print(f"{bb.tm_hour}:{bb.tm_min} {bb.tm_mday}.{bb.tm_mon}.{bb.tm_year}")
print(f"Or: {time.asctime(bb)}")
