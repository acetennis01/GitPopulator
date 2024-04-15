import subprocess
import os
import random
import schedule
import time

def action():
    os.system("./chure.sh")

def random_time():
    """Generate a random time string in HH:MM format."""
    hour = random.randint(16, 23)  # Random hour between 0 and 23
    minute = random.randint(0, 59)  # Random minute between 0 and 59

    hour = 16
    minute = 5

    return f"{hour:02}:{minute:02}"

def schedule_shit(freq):
    schedule.clear()  # Clear existing scheduled jobs before adding new ones
    for _ in range(freq):
        time_str = random_time()
        print(f"Scheduled for {time_str}")
        schedule.every().day.at(time_str).do(action)

if __name__ == "__main__":
    while True:
        num_freq = random.randint(1, 4)
        num_freq = 1
        
        schedule_shit(num_freq)
        print(f"Scheduled {num_freq} tasks for today.")

        # Run the scheduled tasks
        while True:
            schedule.run_pending()
            time.sleep(60)
