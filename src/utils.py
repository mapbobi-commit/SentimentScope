import pandas as pd
import sqlite3


def read(path_to_file):
    wrong_path_to_file = True
    while wrong_path_to_file:
        if path_to_file.split(".")[-1] == "csv":
            return pd.read_csv(
                path_to_file,
                usecols=[0, 1],
                encoding="latin-1",
            )
        else:
            print("The path you have put in isn't csv")
            path_to_file = input(
                "What's the path to the file you want to use (csv)?"
            )


def write(table, path_name):
    if "sqlite" in path_name:
        con = sqlite3.connect("db/sentiment_analysis.sqlite")
        table.to_sql("sentiment_analysis", con, if_exists="append")
        con.close()
    else:
        table.to_csv(
            path_name,
            index=False,
        )
