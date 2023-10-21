import looper
import reader
import MacroTrends as mt


def main():
    for i in range(len(looper.SP500_Tickers)):
        symbol = looper.SP500_Tickers[i]
        url = f"https://www.macrotrends.net/stocks/charts/{symbol}/{reader.data2[i]}/number-of-employees"
        mt.scrape_website(url, symbol)


if __name__ == "__main__":
    main()
