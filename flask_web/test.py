import datetime
import time

n = 1536807600
if n % 3600==0:
    c_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(n))
    print(c_time)