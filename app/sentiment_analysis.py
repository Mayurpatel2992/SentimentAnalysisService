from textblob import TextBlob

def analyze_sentiment(comment):
    analysis = TextBlob(comment['text'])
    return {
        'id': comment['id'],
        'text': comment['text'],
        'polarity': analysis.sentiment.polarity,
        'classification': 'positive' if analysis.sentiment.polarity > 0 else 'negative'
    }
