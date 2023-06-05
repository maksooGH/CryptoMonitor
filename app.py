import src.logic as logic
import src.utls as utls
import src.webhook as wh

import time
#import os

urlGainers = "https://discord.com/api/webhooks/1115308486851567718/DsHgMQlVDm3H6T_0CRksbf0jZYIhwVYlamp_xM9qr3LoJcK1oyS6Qo47gT74Hd0RuHkh"
urlLosers = "https://discord.com/api/webhooks/1115308625821450313/nNoB1A_3Kko14vhl2DDK99DM8HhwKsjVgcl-eV52AOEP21fUfe-I6zSCxVIJzod2O3ao"

def main():
    Stocks = utls.read_tickers_from_file()
    if len(Stocks) == 0:
        return
    
    while True:
        utls.wait_for_next_check_hour()
        time.sleep(60)
        print("Checking stocks' percentage change...")
        Stocks = logic.get_current_percentage(Stocks)
        print("Successfully checked stocks!")
        ##utls.print_matching(Stocks)
        wh.prepare_and_send_webhooks(Stocks, urlGainers, urlLosers)
        print("Webhook sent stocks!")
        
if __name__ == '__main__':
    main()
