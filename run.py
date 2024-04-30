import subprocess
import os
import random
import schedule
import time

ran = 0

def action():
    global ran
    os.system("./chure.sh")
    ran += 1

def random_time():
    hour = random.randint(0, 23) 
    minute = random.randint(0, 59)  

    return f"{hour:02}:{minute:02}"

def schedule_shit(freq):
    schedule.clear()  
    for _ in range(freq):
        time_str = random_time()
        print(f"Scheduled for {time_str}")
        schedule.every().day.at(time_str).do(action)

if __name__ == "__main__":
    while True:
        num_freq = random.randint(1, 4)

        schedule_shit(num_freq)
        print(f"Scheduled {num_freq} tasks for today.")

        # Run the scheduled tasks
        while True:
            schedule.run_pending()
            time.sleep(60)
            #print(ran)
            #print(len(schedule.jobs))
            if ran == num_freq:
                break
        
        print("Done")
        schedule.clear()
        print(len(schedule.jobs))
