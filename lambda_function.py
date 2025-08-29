import boto3
import json
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize Amazon Comprehend client
comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    # Extract the review text from the event
    review = event.get('review', '')

    if not review:
        logger.error("No review text found in event.")
        return {
            'statusCode': 400,
            'body': json.dumps('No review text provided.')
        }

    # Analyze sentiment
    response = comprehend.detect_sentiment(Text=review, LanguageCode='en')
    sentiment = response['Sentiment']
    sentiment_scores = response['SentimentScore']

    # Log the result
    logger.info(f"Review: {review}")
    logger.info(f"Sentiment: {sentiment}")
    logger.info(f"Scores: {sentiment_scores}")

    # Return result
    return {
        'statusCode': 200,
        'body': json.dumps({
            'review': review,
            'sentiment': sentiment,
            'scores': sentiment_scores
        })
    }
