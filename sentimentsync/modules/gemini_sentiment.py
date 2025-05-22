# Libraries 
import google.generativeai as genai
import math
import enum
import json
import re
from typing_extensions import TypedDict

# Gemini Method
class Sentiment(enum.Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"

class AnalysisResult(TypedDict):
    sentiment: Sentiment
    intensity: float

def get_gemini_sentiment(title: str, GEMINI_API_KEY: str, gemini_model: str) -> AnalysisResult:
    if not GEMINI_API_KEY:
        raise ValueError("Missing GEMINI_API_KEY")

    genai.configure(api_key=GEMINI_API_KEY)

    # Dynamically fetch available model names
    try:
        available_models = [m.name.split("/")[-1] for m in genai.list_models()]
    except Exception as e:
        raise ValueError(f"Failed to fetch Gemini model list: {e}")

    if gemini_model not in available_models:
        raise ValueError(f"'{gemini_model}' is not a valid Gemini model. Available models: {', '.join(available_models)}")

    model = genai.GenerativeModel(gemini_model)

    prompt = (
        f"Classify the sentiment of this headline as POSITIVE, NEGATIVE, or NEUTRAL. "
        f"Also provide a confidence score between 0 and 1. "
        f"Return only valid JSON like this:\n"
        f'{{"sentiment": "POSITIVE", "score": 0.85}}\n\n'
        f"Headline: \"{title}\""
    )

    response = model.generate_content(prompt)

    if response.candidates:
        raw_text = ''.join(part.text for part in response.candidates[0].content.parts).strip()
        raw_text = raw_text.strip("` \n")
        match = re.search(r'\{.*?\}', raw_text, re.DOTALL)
        if match:
            try:
                parsed = json.loads(match.group(0))
                sentiment = Sentiment[parsed["sentiment"].strip().upper()]
                raw_score = float(parsed["score"])
                intensity = round(math.exp(abs(raw_score) * 5) - 1, 3)
                return sentiment.value, intensity
            except Exception as e:
                print(f"Gemini parsing error: {e}")

    return Sentiment.NEUTRAL.value, 0.0
