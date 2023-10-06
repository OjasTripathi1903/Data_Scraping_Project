import pandas as pd

# Input the income fields you would like extracted
incomeFields = [
    "Total Revenue",
    "Net Income",
    "EBIT",
    "Cost Of Revenue",
    "Selling General And Administration",
    "Research And Development",
    "Normalized EBITDA",
]

# Input the balance sheet fields you would like extracted
balanceFields = [
    "Total Assets",
    "Working Capital",
    "Total Debt",
    "Common Stock Equity",
    "Net PPE",
    "Goodwill And Other Intangible Assets",
    "Long Term Debt And Capital Lease Obligation",
    "Current Debt And Capital Lease Obligation",
]

# Input the cash flow fields you would like extracted
cashFields = ["Operating Cash Flow", "Free Cash Flow"]


# Extractor functions for each field
def prettifyIncome(income_df):
    df_output = income_df.loc[incomeFields].copy()
    return df_output


def prettifyBalance(balance_df):
    df_output = balance_df.loc[balanceFields].copy()
    return df_output


def prettifyCash(cash_df):
    df_output = cash_df.loc[cashFields].copy()
    return df_output


def main():
    print("hello")


if __name__ == "__main__":
    main()
