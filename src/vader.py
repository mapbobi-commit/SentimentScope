from vaderSentiment.vaderSentiment import (
    SentimentIntensityAnalyzer,
)
import pandas as pd
from datetime import datetime
import time
import numpy as np

# Function which rounds and gets the sentiment out of a string


def sentiment_compound(x, analyzer, key="compound"):
    return round(
        SentimentIntensityAnalyzer().polarity_scores(x)[
            key
        ],
        1,
    )


def vader_execution(number_random_rows, table):
    # Takes random rows and creates a new column by applying sentiment_analyisis on the text of each person
    random_row_table = table.sample(number_random_rows)

    random_row_table["sentiment_score"],
    random_row_table["date"] = (
        random_row_table["text"].apply(
            sentiment_compound,
            args=[SentimentIntensityAnalyzer, "compound"],
        ),
    )

    return random_row_table
