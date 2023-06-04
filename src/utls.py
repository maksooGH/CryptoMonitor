import datetime
import time
import os

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

def print_matching(dict_list):   
    for x in dict_list:
        if abs(x['LastChange'])>0.05:
            change = x['LastChange']
            print(x['Ticker'], f'{change}%')

def read_tickers_from_file():
    # 1. Check if file named "tickers.txt" is in app dir, if no create it
    filename = "tickers.txt"
    if not os.path.exists(filename):
        open(filename, 'w', encoding='utf-8').close() # this creates an empty file
        print('Add tickers to "tickers.txt" file to continue')
        return [] # we close program (by returning from function)
    
    # 2. Read this file and create list of string with individual tickers
    with open(filename, 'r',encoding='utf-8') as file:
        tickers = [line.strip() for line in file] # read lines and remove newline characters

    # 4. If list is empty print "Add tickers to "tickers.txt" file to continue" and close program
    if not tickers:
        print('Add tickers to "tickers.txt" file to continue')
        return [] # we close program (by returning from function)
    stocks = [{"Ticker":x} for x in tickers]
    # 5. return list
    return stocks