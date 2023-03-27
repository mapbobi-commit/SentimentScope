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


# Function which performs a sentiment analysis for each row's text and rounds
def sentiment_analysis(x):
    return round(
        SentimentIntensityAnalyzer().polarity_scores(x)["compound"],
        1,
    )


def vader_execution(number_random_rows, data):
    # Takes random rows and creates a new column by applying sentiment_analyisis on the text of each person
    random_row_table = data.sample(number_random_rows)

    random_row_table["sentiment"] = random_row_table["text"].apply(
        sentiment_analysis
    )
    random_row_table["magnitude"] = None
    random_row_table["date"] = random_row_table["date"].apply(date_time_changer)
    random_row_table.insert(1, "method", "vader")
    return random_row_table
