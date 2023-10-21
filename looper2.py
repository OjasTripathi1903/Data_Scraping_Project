import looper
import reader
import MacroTrends as mt
import time


def main():
    for i in range(len(looper.SP500_Tickers)):
        symbol = looper.SP500_Tickers[i]
        url = f"https://www.macrotrends.net/stocks/charts/{symbol}/{reader.data2[i]}/number-of-employees"
        mt.scrape_website(url, symbol)
        print(f"{i}/503 completed: {looper.SP500_Tickers[i]}")
        time.sleep(3)


if __name__ == "__main__":
    main()
