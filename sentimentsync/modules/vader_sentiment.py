# Libraries
from nltk.sentiment import SentimentIntensityAnalyzer
import math
import nltk

# Download VADER lexicon
nltk.download('vader_lexicon')

# VADER Method
def get_vader_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    sentiment = "POSITIVE" if compound >= 0.05 else "NEGATIVE" if compound <= -0.05 else "NEUTRAL"

    # Scaled Intensity
    intensity = round(math.exp(abs(compound) * 5) - 1, 3)
    
    return sentiment, intensity
