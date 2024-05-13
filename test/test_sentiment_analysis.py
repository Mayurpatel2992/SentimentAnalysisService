from app.sentiment_analysis import analyze_sentiment

def test_positive_sentiment():
    comment = {'id': '1', 'text': 'I love this product!'}
    result = analyze_sentiment(comment)
    assert result['classification'] == 'positive'

def test_negative_sentiment():
    comment = {'id': '2', 'text': 'I hate this thing.'}
    result = analyze_sentiment(comment)
    assert result['classification'] == 'negative'
