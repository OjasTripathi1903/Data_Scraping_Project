import pandas as pd

input = pd.read_excel("Data.xlsx", sheet_name="Sheet1")


def split(raw_frame: pd.DataFrame):
    print(raw_frame.columns[2])
    year = str(raw_frame.columns[2])
    if "2022" in year:
        columns = [0, 2]
        output = raw_frame.iloc[:, columns]
        print(output)


if __name__ == "__main__":
    split(input)
