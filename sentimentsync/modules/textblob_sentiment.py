# Libraries
from textblob import TextBlob
import math

# TextBlob Method
def get_textblob_sentiment(text):
    score = TextBlob(text).sentiment.polarity
    sentiment = "POSITIVE" if score > 0.05 else "NEGATIVE" if score < -0.05 else "NEUTRAL"
    intensity = round(math.exp(abs(score) * 5) - 1, 3)
    return sentiment, intensity