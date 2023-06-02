import datetime
import time

def wait_for_next_check_hour():
    current_time = datetime.datetime.now()

    if current_time.minute < 30:
        next_time = current_time.replace(minute=30, second=0, microsecond=0)
    else:
        next_hour = (current_time + datetime.timedelta(hours=1)).hour
        next_time = current_time.replace(hour=next_hour, minute=0, second=0, microsecond=0)

    time_to_wait = (next_time - current_time).total_seconds()
    as_min = round(time_to_wait/60, 2)
    print(f'Waiting {as_min} minutes...')
    time.sleep(time_to_wait)
    # Optional: Print a message once the waiting is over
    #print("Next half-hour has arrived!")
