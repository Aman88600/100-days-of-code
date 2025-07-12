from datetime import datetime
time_1 = datetime.now()
for i in range(1_000):
    print(i)
time_2 = datetime.now()
time_elapsed = time_2 - time_1
print(time_elapsed)