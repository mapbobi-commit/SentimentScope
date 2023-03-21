import pandas as pd
from gcloud import gcloud_execution
from vader import vader_execution
from utils import config
import datetime


def date_time_changer(date):
    date_datetime = datetime.strptime(
        str(date).replace("PDT", ""), "%a %b %d %H:%M:%S %Y"
    )
    return date_datetime.strftime("%Y-%m-%d")


def write(method, table, csv_name):
    if method == "gcloud":
        table.to_csv(
            csv_name + ".csv",
            index=False,
        )
    else:
        table.to_csv(csv_name + ".csv", index=False)


path_to_file = config["path_to_file"]

# Takes the date and text columns
data = pd.read_csv(
    path_to_file,
    usecols=[0, 1],
    encoding="latin-1",
)

method_analysis = input(
    'What method would you like to use for sentiment analysis(type "gcloud" or "vader")? '
)
number_rows = int(input("How many rows do you want the table to have? "))
csv_file_name = input("What name do you want your csv file to have? ")


if method_analysis == "gcloud":
    table = vader_execution(number_rows, data)
    table["date"] = table["date"].apply(date_time_changer)
    write(method_analysis, table, csv_file_name)
else:
    table = gcloud_execution(number_rows, data)
    table["date"] = table["date"].apply(date_time_changer)
    write(method_analysis, table, csv_file_name)
