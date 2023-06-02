import src.logic as logic
import src.utls as utls

def main():
    Stocks = [
        {"Ticker":"BTC-USD"},
        {"Ticker":"ETH-USD"},
        {"Ticker":"AAPL"},
        {"Ticker":"TSLA"},
        {"Ticker":"META"},
    ]
    #utls.wait_for_next_round_hour()
    Stocks = logic.get_current_percentage(Stocks)
    print(Stocks)
    return
    while True:
        
        
        for stock in Stocks:
            change, last = get_last_price(stock['Ticker'])
            stock['change'] = change
            stock['last'] = last
        Stocks = sort_dict_list_by_change(Stocks)
        print(Stocks)


if __name__ == '__main__':
    main()
