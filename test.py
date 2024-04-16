import subprocess
import os
import random
import schedule
import time

ran = 0

def action():
    global ran
    print("Hello")
    ran += 1

def random_time():
    """Generate a random time string in HH:MM format."""
    hour = random.randint(16, 23)  # Random hour between 0 and 23
    minute = random.randint(0, 59)  # Random minute between 0 and 59

    hour = 16
    minute = 22

    return f"{hour:02}:{minute:02}"

def schedule_shit(freq):
    schedule.clear()  # Clear existing scheduled jobs before adding new ones
    for _ in range(freq):
        time_str = random_time()
        print(f"Scheduled for {time_str}")
        schedule.every().day.at(time_str).do(action)

num_freq = 1
schedule_shit(num_freq)
while(True):
    schedule.run_pending()
    print(len(schedule.jobs))
    time.sleep(10)
    if ran == num_freq:
        break

print("Done")
schedule.clear()
print(len(schedule.jobs))