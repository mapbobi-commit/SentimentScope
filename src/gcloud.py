from google.cloud import language_v1
import six
import pandas as pd
from datetime import datetime
import time
import numpy as np


def gcloud_analyze_sentiment(content):
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


# Takes each random row and cleans it and then concatenates to the next row to create a single string
def string_concatenate(table):
    length_text_each_person = []
    overall_text = ""

    for row in table.index:
        if (
            table["text"][row]
            .strip(" ")
            .endswith("?")
            or table["text"][row]
            .strip(" ")
            .endswith(".")
            or table["text"][row]
            .strip(" ")
            .endswith("!")
        ):
            overall_text = "{}{} <br>".format(
                overall_text,
                table["text"][row].strip(" "),
            )
            length_text_each_person.append(
                len(
                    table["text"][row].strip(" ")
                )
            )
        else:
            overall_text = "{}{}.<br>".format(
                overall_text,
                table["text"][row].strip(" "),
            )
            length_text_each_person.append(
                len(
                    table["text"][row].strip(" ")
                )
            )
    return length_text_each_person, overall_text


# Puts the sentiment of every person into array
# If the text of a person is split into multiple sentences,
# it adds them up in the sentiment magnitude array and does the average of sentiment score
def string_splitter(sentences_sentiment, length_text_each_person):
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
                round(x.sentiment.magnitude, 1)
            )
            sentiment_magnitude[i] = round(
                sentiment_magnitude[i], 1
            )
            sentiment_score.append(
                [round(x.sentiment.score, 1)]
            )
            sentiment_score[i] = round(
                np.mean(sentiment_score[i]), 1
            )
            i += 1
    sentiment_score[i] = round(
        np.mean(sentiment_score[i]), 1
    )
    return sentiment_magnitude, sentiment_score


def gcloud_execution(number_of_randow_rows, table):
    # Reads random rows
    random_row_table = table.sample(number_of_randow_rows)

    length_text_each_person, overall_text = string_concatenate(
        random_row_table)

    sentences_sentiment = gcloud_analyze_sentiment(
        overall_text
    ).sentences

    sentiment_magnitude, sentiment_score = string_splitter(
        number_of_randow_rows, length_text_each_person)
    (
        random_row_table["sentiment_magnitude"],
        random_row_table["sentiment_score"],
    ) = (
        sentiment_magnitude,
        sentiment_score,
    )
    return random_row_table

