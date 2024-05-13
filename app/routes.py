from flask import Blueprint, request, jsonify
from .sentiment_analysis import analyze_sentiment
from .feddit_client import fetch_comments

main = Blueprint('main', __name__)

@main.route('/comments', methods=['GET'])
def get_comments():
    subfeddit = request.args.get('subfeddit', 'general')
    comments = fetch_comments(subfeddit)
    results = [analyze_sentiment(comment) for comment in comments]
    return jsonify(results)
