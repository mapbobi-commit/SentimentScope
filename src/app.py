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


def write(method, table):
    if method == "gcloud":
        table.to_csv(
            "sentiment_analysis_file.gcloud.csv",
            index=False,
        )
    else:
        table.to_csv(
            "sentiment_analysis_file.vader.csv", index=False
        )


number_rows = config["rows"]
method_analysis = config["method"]
number_of_tables = config["number_of_tables"]
path_to_file = config["path_to_file"]

# Takes the date and text columns
data = pd.read_csv(
    path_to_file,
    usecols=[0, 1],
    encoding="latin-1",
)

if method_analysis == "gcloud":
    table = vader_execution(number_rows, data)
    table["date"] = table["date"].apply(
        date_time_changer
    )
    write(method_analysis, table)
else:
    table = gcloud_execution(number_rows, data)
    table["date"] = table["date"].apply(
        date_time_changer
    )
    write(method_analysis, table)
