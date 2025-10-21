import csv
import time
from datetime import datetime

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])

    for i in range(1, 301):
        now = datetime.now()
        sec = now.second
        microsec = int(now.microsecond / 1000)
        writer.writerow([i, sec, microsec])
        time.sleep(0.01)