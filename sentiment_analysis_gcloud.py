from google.cloud import language_v1
import six
import pandas as pd
from datetime import datetime
import time
import numpy as np


# gcloud sentiment analysis function
def sample_analyze_sentiment(content):
    client = language_v1.LanguageServiceClient()

    if isinstance(content, six.binary_type):
        content = content.decode("utf-8")

    type_ = language_v1.Document.Type.HTML
    document = {"type_": type_, "content": content}

    encoding_type = language_v1.EncodingType.UTF8
    response = client.analyze_sentiment(
        request={
            "document": document,
            "encoding_type": encoding_type,
        }
    )
    return response


def date_time_changer(date):
    date_datetime = datetime.strptime(
        str(date).replace("PDT", ""), "%a %b %d %H:%M:%S %Y"
    )
    return date_datetime.strftime("%Y-%m-%d")


def gcloud_execution(number_of_randow_rows, table):
    start_execution_time = time.time()

    # Reads random rows
    random_row_table = table.sample(number_of_randow_rows)
    length_text_each_person = []
    overall_text = ""

    # Takes each random row, cleans it and then it concatenates it to the next row to create a single string
    for row in random_row_table.index:
        if (
            random_row_table["text"][row]
            .strip(" ")
            .endswith("?")
            or random_row_table["text"][row]
            .strip(" ")
            .endswith(".")
            or random_row_table["text"][row]
            .strip(" ")
            .endswith("!")
        ):
            overall_text = "{}{} <br>".format(
                overall_text,
                random_row_table["text"][row].strip(" "),
            )
            length_text_each_person.append(
                len(
                    random_row_table["text"][row].strip(" ")
                )
            )
        else:
            overall_text = "{}{}.<br>".format(
                overall_text,
                random_row_table["text"][row].strip(" "),
            )
            length_text_each_person.append(
                len(
                    random_row_table["text"][row].strip(" ")
                )
            )

    sentences_sentiment = sample_analyze_sentiment(
        overall_text
    ).sentences

    # Puts the sentiment of every person into array
    # If the text of a person is split into multiple sentences,
    # it adds them up in the sentiment magnitude array and does the average of sentiment score
    previous_offset = 0
    i = 0
    sentiment_score = []
    sentiment_magnitude = []
    for x in sentences_sentiment:
        if len(sentiment_magnitude) == 0:
            sentiment_magnitude.append(
                x.sentiment.magnitude
            )
            sentiment_score.append([x.sentiment.score])
        elif (
            x.text.begin_offset - previous_offset
            <= length_text_each_person[i]
        ):
            sentiment_magnitude[i] += x.sentiment.magnitude
            sentiment_score[i].append(x.sentiment.score)
        else:
            previous_offset = x.text.begin_offset
            sentiment_magnitude.append(
                x.sentiment.magnitude
            )
            sentiment_score[i] = np.mean(sentiment_score[i])
            sentiment_score.append([x.sentiment.score])
            i += 1
    sentiment_score[i] = np.mean(sentiment_score[i])

    # Puts the random_row_table in a csv file
    # Rounds the floats and changes the date format
    (
        random_row_table["sentiment_magnitude"],
        random_row_table["sentiment_score"],
    ) = (
        sentiment_magnitude,
        sentiment_score,
    )
    random_row_table["date"] = random_row_table[
        "date"
    ].apply(date_time_changer)
    random_row_table[
        "sentiment_magnitude"
    ] = random_row_table["sentiment_magnitude"].apply(
        round, [1]
    )
    random_row_table["sentiment_score"] = random_row_table[
        "sentiment_score"
    ].apply(round, [1])

    # Writes it in a file
    random_row_table.to_csv(
        "sentiment_analysis_file_twit.csv", index=False
    )

    # Looks how much time the operation took
    end_execution_time = time.time()
    total_time = end_execution_time - start_execution_time
    print("\n" + str(total_time))
