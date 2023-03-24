import pandas as pd
from gcloud import gcloud_execution
from vader import vader_execution
import utils
import datetime
import random

# Takes the date and text columns
number_rows = int(
    input("How many rows do you want the table to have?")
)
csv_file_name = (
    input(
        "What's the path to the file you want to create?"
    )
    or f"../data/nameless_csv_file {random.randint(0, 100)}"
)
method_analysis = input(
    'What method would you like to use for sentiment analysis (type "gcloud" or "vader")?'
)
path_to_file = (
    input(
        "What's the path to the file you want to use (either csv or sqlite or db)?"
    )
    or "..data/example_csv/example_csv_file.csv"
)

data = utils.read(path_to_file)
problem = True
while problem:
    if method_analysis == "vader":
        table = vader_execution(number_rows, data)
        utils.write(table, csv_file_name, path_to_file)
        problem = False
    elif method_analysis == "gcloud":
        table = gcloud_execution(number_rows, data)
        utils.write(table, csv_file_name, path_to_file)
        problem = False
    else:
        print(
            "There are only 2 methods you can choose (please type vader or gcloud)"
        )
        method_analysis = input(
            'What method would you like to use for sentiment analysis (type "gcloud" or "vader")?'
        )
