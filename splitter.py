import pandas as pd
import time
import openpyxl


# Check if the sheet already exists inside the book
def sheet_exists(years, sheets: list[str]):
    output = False
    for year in sheets:
        if years in sheets:
            output = False
            return output
        else:
            continue
    return output


def split(raw_frame: pd.DataFrame, symbol, output_frames: list[pd.DataFrame]):
    #    TODO: Loop this
    t2022 = output_frames[0]
    t2021 = output_frames[1]
    t2020 = output_frames[2]
    t2019 = output_frames[3]
    book = openpyxl.load_workbook("Data.xlsx")

    sheetnames = book.sheetnames

    for column in range(len(raw_frame.columns)):
        year = str(raw_frame.columns[column])
        #   TODO: Functionise this
        if "2022" in year:
            if sheet_exists("2022", sheetnames) == True:
                columns = [column]
            else:
                columns = [0, column]
            column_name = raw_frame.columns[column]

            output = raw_frame.iloc[:, columns]
            output.rename(columns={column_name: symbol}, inplace=True)
            t2022 = pd.concat([t2022, output], axis=1)

        if "2021" in year:
            if sheet_exists("2021", sheetnames) == True:
                columns = [column]
            else:
                columns = [0, column]

            column_name = raw_frame.columns[column]
            output = raw_frame.iloc[:, columns]
            output.rename(columns={column_name: symbol}, inplace=True)
            t2021 = pd.concat([t2021, output], axis=1)

        if "2020" in year:
            if sheet_exists("2020", sheetnames) == True:
                columns = [column]
            else:
                columns = [0, column]

            column_name = raw_frame.columns[column]
            output = raw_frame.iloc[:, columns]
            output.rename(columns={column_name: symbol}, inplace=True)
            t2020 = pd.concat([t2020, output], axis=1)

        if "2019" in year:
            if sheet_exists("2019", sheetnames) == True:
                columns = [column]
            else:
                columns = [0, column]

            column_name = raw_frame.columns[column]
            output = raw_frame.iloc[:, columns]
            output.rename(columns={column_name: symbol}, inplace=True)
            t2019 = pd.concat([t2019, output], axis=1)
        else:
            continue

        outputs = [t2022, t2021, t2020, t2019]
        write_to_sheets(outputs, sheetnames, book)
        # return output
        # Dev Halted for ease


def write_to_sheets(
    inputs: list[pd.DataFrame],
    sheetnames: list[str],
    book: openpyxl.Workbook,
):
    for years in inputs:
        sheetname = [name for name, value in locals().items() if value is years][0]
        if sheetname in sheetnames:
            empty = book[sheetname].max_column + 1
        else:
            empty = 0
        with pd.ExcelWriter(
            "Data.xlsx", engine="openpyxl", mode="a", if_sheet_exists="overlay"
        ) as writer:
            years.to_excel(writer, sheet_name=sheetname, index=False, startcol=empty)


def runner():
    first = second = third = fourth = pd.DataFrame()
    output_names = [first, second, third, fourth]
    masterframe = pd.read_excel("Data.xlsx", sheet_name="Sheet1")
    split(masterframe, "MMM", output_names)


if __name__ == "__main__":
    runner()
