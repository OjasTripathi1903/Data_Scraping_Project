import yfinance as yf
import pandas as pd
import prettify as pfy


def get_income_statement(symbol):
    # Use the yfinance package to retrieve the income statement data
    stock = yf.Ticker(symbol)
    # Get the income statement
    income_statement = stock.financials
    # Create a Pandas DataFrame from the data
    df = pd.DataFrame(income_statement)
    # Only output the specific values
    output = pfy.prettifyIncome(df)
    return output


def get_balance_statement(symbol):
    # Use the yfinance package to retrieve the income statement data
    stock = yf.Ticker(symbol)

    # Get the balance statement
    balancesheet = stock.balance_sheet
    # Create a Pandas DataFrame from the data
    df = pd.DataFrame(balancesheet)

    output = pfy.prettifyBalance(df)

    return output


def get_cash_flow(symbol):
    # Use the yfinance package to retrieve the income statement data
    stock = yf.Ticker(symbol)

    # Get the cash flow
    cash_flow = stock.cashflow
    # Create a Pandas DataFrame from the data
    df = pd.DataFrame(cash_flow)
    output = pfy.prettifyCash(df)
    return output


def save_to_excel(dataframe, filename):
    # Save the DataFrame to an Excel sheet
    dataframe.to_excel(filename, index=True)


def main():
    # Define the stock symbol for NVIDIA Corporation
    symbol = "NVDA"

    # Make API request to get the income statement data
    income_statement = get_income_statement(symbol)
    balance_sheet = get_balance_statement(symbol)
    cash_flow = get_cash_flow(symbol)

    spacer_income_statement = pd.Series("Income Statement")
    spacer_balance_sheet = pd.Series("Balance Sheet")
    spacer_cash_flow = pd.Series("Cash Flow")
    array = [
        spacer_income_statement,
        income_statement,
        spacer_balance_sheet,
        balance_sheet,
        spacer_cash_flow,
        cash_flow,
    ]
    # Save the data to an Excel sheet
    combined = pd.concat(array)
    save_to_excel(combined, "Data.xlsx")


if __name__ == "__main__":
    main()
