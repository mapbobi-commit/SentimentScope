import pandas as pd
from datetime import datetime
import time
import numpy as np
import logging


def date_time_changer(date):
    date_datetime = datetime.strptime(
        str(date).replace("PDT", ""), "%a %b %d %H:%M:%S %Y"
    )
    return date_datetime.strftime("%Y-%m-%d")


def write(table, method):
    if method == "gcloud":
        table.to_csv(
            "sentiment_analysis_file.gcloud.csv",
            index=False,
        )
    else:
        table.to_csv(
            "sentiment_analysis_file.vader.csv", index=False
        )
