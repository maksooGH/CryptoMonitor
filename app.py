import src.logic as logic
import src.utls as utls
#import os

def main():
    #os.system('cls')
    Stocks = [
        {"Ticker":"BTC-USD"},
        {"Ticker":"ETH-USD"},
        {"Ticker":"AAPL"},
        {"Ticker":"TSLA"},
        {"Ticker":"META"},
    ]
    
    while True:
        utls.wait_for_next_check_hour()
        print("Checking stocks' percentage change...")
        Stocks = logic.get_current_percentage(Stocks)
        print(Stocks)
        print("Successfully checked stocks!")


if __name__ == '__main__':
    main()
