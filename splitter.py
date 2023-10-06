import pandas as pd
import time

input = pd.read_excel("Data.xlsx", sheet_name="Sheet1")


def split(raw_frame: pd.DataFrame):
    t2022 = pd.DataFrame()
    t2021 = pd.DataFrame()
    t2020 = pd.DataFrame()
    t2019 = pd.DataFrame()

    for column in range(len(raw_frame.columns)):
        year = str(raw_frame.columns[column])
        if "2022" in year:
            column_name = raw_frame.columns[column]
            columns = [0, column]
            output = raw_frame.iloc[:, columns]
            output.rename(columns={column_name: "MMM"}, inplace=True)
            t2022 = pd.concat([t2022, output], axis=1)

        if "2021" in year:
            column_name = raw_frame.columns[column]
            columns = [0, column]
            output = raw_frame.iloc[:, columns]
            output.rename(columns={column_name: "MMM"}, inplace=True)
            t2021 = pd.concat([t2021, output], axis=1)

        if "2020" in year:
            column_name = raw_frame.columns[column]
            columns = [0, column]
            output = raw_frame.iloc[:, columns]
            output.rename(columns={column_name: "MMM"}, inplace=True)
            t2020 = pd.concat([t2020, output], axis=1)

        if "2019" in year:
            column_name = raw_frame.columns[column]
            columns = [0, column]
            output = raw_frame.iloc[:, columns]
            output.rename(columns={column_name: "MMM"}, inplace=True)
            t2019 = pd.concat([t2019, output], axis=1)
        else:
            continue

        outputs = [t2022, t2021, t2020, t2019]
        for years in outputs:
            sheetname = [name for name, value in locals().items() if value is years][0]
            with pd.ExcelWriter("Data.xlsx", engine="openpyxl", mode="a") as writer:
                years.to_excel(
                    writer,
                    sheet_name=sheetname,
                    index=False,
                )


def runner():
    print(split(input))


if __name__ == "__main__":
    runner()
