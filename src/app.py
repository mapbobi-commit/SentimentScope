import pandas as pd
from gcloud import gcloud_execution
from vader import vader_execution
from utils import config
import datetime
import random


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

number_rows = int(input("How many rows do you want the table to have?"))
csv_file_name = input("Path to the csv file you want to create."
                      ) or "../data/nameless_csv_file" + str(
                          random.randint(0, 100))
method_analysis = input(
    'What method would you like to use for sentiment analysis (type "gcloud" or "vader")?'
)

problem = True
while problem:
    if method_analysis == "vader":
        table = vader_execution(number_rows, data)
        write(method_analysis, table, csv_file_name)
        problem = False
    elif method_analysis == "gcloud":
        table = gcloud_execution(number_rows, data)
        write(method_analysis, table, csv_file_name)
        problem = False
    else:
        print(
            "There are only 2 methods you can choose (please type vader or gcloud)"
        )
        method_analysis = input(
            'What method would you like to use for sentiment analysis (type "gcloud" or "vader")?'
        )
