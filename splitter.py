import pandas as pd
import time
import openpyxl
import extractor as ex

sheets = ["2022", "2021", "2020", "2019"]


# Check if the sheet already exists inside the book
def sheet_exists(year, sheets: list[str]):
    output = False
    for years in sheets:
        if year in years:
            output = True
            return output
        else:
            continue
    return output


def year_splitter(year: str, series: pd.Series):
    sheetname = year
    temp = series.iloc[0]
    print(temp)
    if year in str(temp):
        series.iloc[0] = year
    return pd.DataFrame(series).T


def split(raw_frame: pd.DataFrame, symbol, output_frames: list[pd.DataFrame]):
    #    TODO: Loop this
    t2022 = output_frames[0]
    t2021 = output_frames[1]
    t2020 = output_frames[2]
    t2019 = output_frames[3]
    book = openpyxl.load_workbook("Data.xlsx")

    sheetnames = book.sheetnames
    print(sheetnames)


def runner():
    masterframe = pd.read_excel("Data.xlsx", sheet_name="Master")
    test_series = masterframe.iloc[0]
    test_series = year_splitter("2022", test_series)
    # split(masterframe, "MMM", output_names)

    ex.excel_inserter(test_series, "output.xlsx", "2022", "row", False)


if __name__ == "__main__":
    print(runner())
