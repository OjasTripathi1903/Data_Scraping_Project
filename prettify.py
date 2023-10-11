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
def prettifyIncome(income_df: pd.DataFrame):
    df_output = pd.DataFrame()
    indexes = list(income_df.columns)
    print(indexes)
    for i in range(len(incomeFields)):
        try:
            temp = income_df.loc[incomeFields[i]].copy()
            print(temp)
            df_output = pd.concat([df_output, temp], axis=1)
        except KeyError:
            data = []
            for i in range(len(indexes)):
                data.append("missing")

            print(data)
            temp = pd.Series(data, index=indexes, name=incomeFields[i])
            print(temp)
            df_output = pd.concat([df_output, temp], axis=1)
            continue
    return df_output


def prettifyBalance(balance_df: pd.DataFrame):
    df_output = pd.DataFrame()
    for i in range(len(balanceFields)):
        try:
            temp = balance_df.loc[balanceFields[i]].copy()
            df_output = pd.concat([df_output, temp], axis=1)
        except KeyError:
            df_output
    return df_output


def prettifyCash(cash_df: pd.DataFrame):
    df_output = pd.DataFrame()
    for i in range(len(cashFields)):
        try:
            temp = cash_df.loc[cashFields[i]].copy()
            df_output = pd.concat([df_output, temp], axis=1)
        except KeyError:
            continue
    return df_output


def main():
    masterframe = pd.read_excel("Data.xlsx", sheet_name="Master")
    print(prettifyIncome(masterframe))


if __name__ == "__main__":
    main()
