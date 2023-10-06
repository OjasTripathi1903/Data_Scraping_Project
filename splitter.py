import pandas as pd

input = pd.read_excel("Data.xlsx", sheet_name="Sheet1")


def split(raw_frame: pd.DataFrame):
    print(raw_frame.columns[2])
    year = str(raw_frame.columns[2])
    if "2022" in year:
        column_name = raw_frame.columns[2]
        columns = [2]
        output = raw_frame.iloc[:, columns]
        indexes = raw_frame.iloc[:, [0]]
        output.rename(columns={column_name: "MMM"}, inplace=True)
        indexes[output.columns[0]] = output.iloc[:, [0]]
        print(indexes)


if __name__ == "__main__":
    split(input)
