import time
from datetime import datetime
while True:
    ts = input()
    if ts == 'exit':
        break
    p_time_stamp = int(ts)
    p_time_str = datetime.fromtimestamp(p_time_stamp).strftime('%Y-%m-%d %H:%M:%S')
    print(p_time_str)