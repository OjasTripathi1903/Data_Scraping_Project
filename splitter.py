import pandas as pd
import time
import openpyxl
import extractor as ex

sheets = ["2022", "2021", "2020", "2019"]


# Check if the sheet already exists inside the book
def sheet_exists(year, sheets: list[str]):
    output = False
    for years in sheets:
        if year in sheets:
            output = True
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
    print(sheetnames)
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
        for i in range(len(outputs)):
            if outputs[i].empty:
                continue
            else:
                ex.excel_inserter(
                    dataframe=outputs[i],
                    file_name="Data.xlsx",
                    sheetname=sheets[i],
                    append_by="column",
                    indexing=False,
                )


def runner():
    first = second = third = fourth = pd.DataFrame()
    output_names = [first, second, third, fourth]
    masterframe = pd.read_excel("Data.xlsx", sheet_name="Master")
    x = split(masterframe, "MMM", output_names)
    return x


if __name__ == "__main__":
    runner()
