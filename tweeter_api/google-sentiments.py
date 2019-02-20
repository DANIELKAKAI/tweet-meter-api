"""Demonstrates how to make a simple call to the Natural Language API."""
import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='apikey.json'


def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    if score < -0.1:
        print('negative')
    elif score >0.1:
        print('positive')
    else:
        print('neutral')
    return 0


def analyze(content):
    client = language.LanguageServiceClient()
    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)
    print_result(annotations)


if __name__ == '__main__':
    analyze("good morning asshole")