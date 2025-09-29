import datetime
import time

start_time = time.time()
while time.time() - start_time < 5:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now)
    time.sleep(1)