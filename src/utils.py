import pandas as pd
import sqlite3


def read(path_to_file):
    problem = True
    while problem:
        if path_to_file.split(".")[-1] == "scv":
            return pd.read_csv(
                path_to_file,
                usecols=[0, 1],
                encoding="latin-1",
            )
        elif (
            path_to_file.split(".")[-1] == "sqlite"
            or path_to_file.split(".")[1] == "db"
        ):
            table_name = input(
                "What's the name of the table you want to read?"
            )
            con = sqlite3.connect(path_to_file)
            table = pd.read_sql_query(
                f"SELECT * from {table_name}", con
            )
            con.close()
            return table
        else:
            print(
                "The path you have put in isn't csv or sqlite or db"
            )
            path_to_file = input(
                "What's the path to the file you want to use (either csv or sqlite or db)?"
            )


def write(table, path_name, path_to_file):
    if path_to_file.split(".")[1] == "scv":
        table.to_csv(
            path_name,
            index=False,
        )
    else:
        table_name = input(
            "What name do you want the table that you have created to have?"
        )
        con = sqlite3.connect(path_name)
        table.to_sql(table_name, con)
        con.close()
