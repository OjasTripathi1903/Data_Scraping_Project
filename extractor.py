import yfinance as yf
import pandas as pd
import prettify as pfy


def get_employee_count(symbol):
    logo = yf.Ticker(symbol)
    output = logo.info

    filtered_data = {"Full Time Employees": [output.get("fullTimeEmployees")]}
    employee_df = pd.DataFrame.from_dict(filtered_data, orient="index")

    return employee_df


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


def spacer_creater(index_title: str):
    data = {index_title: ""}
    output = pd.DataFrame(data=data.values(), index=data.keys())
    return output


logo = "MMM"


def master_output(symbol):
    # Define the stock symbol for NVIDIA Corporation

    # Make API request to get the income statement data
    employee_count = get_employee_count(symbol)
    income_statement = get_income_statement(symbol)
    balance_sheet = get_balance_statement(symbol)
    cash_flow = get_cash_flow(symbol)

    # Create Spacers for neatness

    # TODO: Turn this into functions for compactness and find better ways

    employ_cell = {"Employee Count": ""}
    spacer_employee_count = pd.DataFrame(
        data=list(employ_cell.values()), index=employ_cell.keys()
    )

    income_cell = {"Income Statement": ""}
    spacer_income_statement = pd.DataFrame(
        data=list(income_cell.values()), index=income_cell.keys()
    )

    # spacer_balance_sheet = pd.DataFrame()
    # spacer_balance_sheet.set_index(pd.Index(["Balance Sheet"]), inplace=True)

    # spacer_cash_flow = pd.DataFrame()
    # spacer_cash_flow.set_index(pd.Index(["Cash Flow"]), inplace=True)

    array = [
        spacer_income_statement,
        income_statement,
        # spacer_balance_sheet,
        balance_sheet,
        # spacer_cash_flow,
        cash_flow,
        spacer_employee_count,
        employee_count,
    ]
    # Save the data to an Excel sheet
    combined = pd.concat(array)
    save_to_excel(combined, "Data.xlsx")
    return combined


if __name__ == "__main__":
    master_output(logo)
