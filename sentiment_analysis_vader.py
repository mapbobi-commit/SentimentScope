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
def sentiment_compound(
    x, analyzer, key="compound"
):
    return round(analyzer.polarity_scores(x)[key], 1)


analyzer = SentimentIntensityAnalyzer()


def vader_execution(number_random_rows, table):
    start_execution_time = time.time()

    # Takes random rows and creates a new column by applying sentiment_analyisis on the text of each person
    random_row_table = table.sample(number_random_rows)

    random_row_table["sentiment_score"] = random_row_table[
        "text"
    ].apply(sentiment_compound, args=[analyzer, "compound"])

    # Fixes the date
    random_row_table["date"] = random_row_table[
        "date"
    ].apply(date_time_changer)

    # Writes it in a file
    random_row_table.to_csv(
        "sentiment_analysis_file_vader.csv", index=False
    )

    end_execution_time = time.time()
    total_time = end_execution_time - start_execution_time
    print("\n" + str(total_time))
