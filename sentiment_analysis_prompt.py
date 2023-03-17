import pandas as pd
from sentiment_analysis_gcloud import gcloud_execution
from sentiment_analysis_vader import vader_execution



path_to_file= input("What file do you want to read ?(write the relative path please)")

# Takes the date and text columns
data = pd.read_csv(
    "path_to_file",
    usecols=[2, 5],
    encoding="latin-1",
)


add = False
while add == False:
    
    
    
    number_random_rows = int(
        input("How many rows do you want in your csv file?")
    )
    vader_glcoud = input(
        "Do you want to to run sentiment analysis with vader or gcloud( press 1 for vader or 2 for gcloud)"
    )
    if vader_glcoud == "1":
        vader_execution(number_random_rows, data)
    else:
        gcloud_execution(number_random_rows, data)

    something_add = input(
        "Do you want to do something else (type 1 if you wish to make another table and anything else if you want to stop)"
    )
    if something_add != "1":
        add = True
