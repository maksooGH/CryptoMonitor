import src.logic as logic
import src.utls as utls
import time
#import os

def main():
    #os.system('cls')
    #utls.filter_bad_tickers()
    Stocks = utls.read_tickers_from_file()
    if len(Stocks) == 0:
        return
    
    while True:
        utls.wait_for_next_check_hour()
        time.sleep(60)
        print("Checking stocks' percentage change...")
        Stocks = logic.get_current_percentage(Stocks)
        print("Successfully checked stocks!")
        utls.print_matching(Stocks)

if __name__ == '__main__':
    main()
