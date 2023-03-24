from vaderSentiment.vaderSentiment import (
    SentimentIntensityAnalyzer,
)
import pandas as pd
from datetime import datetime
import time
import numpy as np


def date_time_changer(date):
    date_datetime = datetime.strptime(
        str(date).replace("PDT", ""), "%a %b %d %H:%M:%S %Y"
    )
    return date_datetime.strftime("%Y-%m-%d")



# Function which rounds and gets the sentiment out of a string
def sentiment_compound(x):
    return round(
        SentimentIntensityAnalyzer().polarity_scores(x)["compound"],
        1,
    )


def vader_execution(number_random_rows, table):
    # Takes random rows and creates a new column by applying sentiment_analyisis on the text of each person
    random_row_table = table.sample(number_random_rows)

    random_row_table["sentiment_score"] = random_row_table["text"].apply(
        sentiment_compound
    )

    random_row_table["date"] = random_row_table["date"].apply(date_time_changer)
    return random_row_table
