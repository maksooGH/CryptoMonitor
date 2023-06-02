import src.logic as logic
import src.utls as utls

def main():
    Stocks = [
        {"ticker":"BTC-USD"},
        {"ticker":"ETH-USD"},
        {"ticker":"AAPL"},
        {"ticker":"TSLA"},
        {"ticker":"META"},
    ]
    #utls.wait_for_next_round_hour()
    logic.get_current_percentage(Stocks)
    return
    while True:
        
        
        for stock in Stocks:
            change, last = get_last_price(stock['ticker'])
            stock['change'] = change
            stock['last'] = last
        Stocks = sort_dict_list_by_change(Stocks)
        print(Stocks)


if __name__ == '__main__':
    main()
