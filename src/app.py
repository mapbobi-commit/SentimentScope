import pandas as pd
from gcloud import gcloud_execution
from vader import vader_execution
import utils
import random


path_to_file = (
    input("What's the name of the file you want to use (must be csv)?")
    or "example_csv_file.csv"
)
path_to_file = f"../data/input_csv/{path_to_file}"

number_rows = int(input("How many rows do you want the table to have?"))
method_analysis = input(
    'What method would you like to use for sentiment analysis (type "gcloud" or "vader")?'
)

storage_file_name = (
    input(
        "What do you want the name of the file you will create to be(type sqlite if you wish to store it in a database)?"
    )
    or f"csv_file_without_name{random.randint(0, 100)}"
)
storage_file_name = f"../data/output_csv/{storage_file_name}"



data = utils.read(path_to_file)
wrong_method = True
while wrong_method:
    if method_analysis == "vader":
        data_with_sentiment_analysis = vader_execution(number_rows, data)
        utils.write(data_with_sentiment_analysis, storage_file_name)
        wrong_method = False
    elif method_analysis == "gcloud":
        data_with_sentiment_analysis = gcloud_execution(number_rows, data)
        utils.write(data_with_sentiment_analysis, storage_file_name)
        wrong_method = False
    else:
        print(
            "There are only 2 methods you can choose (please type vader or gcloud)"
        )
        method_analysis = input(
            'What method would you like to use for sentiment analysis (type "gcloud" or "vader")?'
        )
