import src.logic as logic
import src.utls as utls
import src.webhook as wh

import time
#import os



def main():
    Stocks = utls.read_tickers_from_file()
    if len(Stocks) == 0:
        return

    while True:
        utls.wait_for_next_check_hour()
        time.sleep(100)
        print("Checking stocks' percentage change...")
        Stocks = logic.get_current_percentage(Stocks)
        print("Successfully checked stocks!")
        wh.prepare_and_send_webhooks(Stocks)
        print("Webhook sent stocks!")

if __name__ == '__main__':
    main()
