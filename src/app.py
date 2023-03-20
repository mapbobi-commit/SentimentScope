import pandas as pd
from sentiment_analysis_gcloud import gcloud_execution
from sentiment_analysis_vader import vader_execution
from utils import config
import generator as gen

number_rows = config["rows"]
method = config["method"]
number_of_tables = config["number_of_tables"]
path_to_file = config["path_to_file"]


# Takes the date and text columns
data = pd.read_csv(
    path_to_file,
    usecols=[2, 5],
    encoding="latin-1",
)
for i in range(number_of_tables):
    if method == "gcloud":
        table = vader_execution(number_rows, data)
        table["date"] = table["date"].apply(
            gen.date_time_changer
        )
        gen.write(table)
    else:
        table = gcloud_execution(number_rows, data)
        table["date"] = table["date"].apply(
            gen.date_time_changer
        )
        gen.write(table)
