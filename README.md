# Sentiment Analysis
## An Omnithink project

A tool for performing sentiment analysis on Instagram and Twitter comments using Natural Language API (gcloud) or the  [vaderSentiment](https://github.com/cjhutto/vaderSentiment) Python library.

## Requirements
- Python
- pip
- [Natural language API](https://cloud.google.com/python/docs/reference/language/latest)
- csv file with twitter/instagram comments (3rd, 6th column have to be date and text respectively)

## Set up

### Create virtual environment
```bash
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade
python3 -m pip install -r requirements.txt
```

## Start app
```bash
py src/> app.py
```

## Issues
With gcloud, we opted to take every message of every person and combine it in a string before doing the sentiment analysis. However, there is a [limitation](https://cloud.google.com/natural-language/quotas) in the amount of characters the string that the Google cloud service can take. Please be careful, not to go over that amount as it will create an error. If your file is bigger, please split it up in multiple smaller files if you are using the gcloud tool.
