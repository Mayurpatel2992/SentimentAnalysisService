Sentiment Analysis Microservice

Features

- Fetch the latest 25 comments from a specified subfeddit on Feddit.
- Analyze the sentiment of each comment.
- Provide an API endpoint to get sentiment analysis data.
- Docker support for easy deployment and scalability.

Requirements

- Python 3.8+
- Docker
- Docker Compose

Getting Started

Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/Mayurpatel2992/SentimentAnalysisService.git
cd SentimentAnalysisService
```

Setup Environment

Set up a Python virtual environment and install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run Locally

You can run the Flask application locally using:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

This will start the server on `http://localhost:5000/`, where you can make API requests to `/comments`.

Using Docker Compose

To run the entire stack including the Feddit service and the PostgreSQL database:

```bash
docker-compose up --build
```

This will start all services defined in the `docker-compose.yml` file.

API Usage

Get Comments

Request:

```http
GET /comments?subfeddit=exampleSubfeddit
```

Response:

```json
[
  {
    "id": "1",
    "text": "I really enjoyed this!",
    "polarity": 0.8,
    "classification": "positive"
  },
  {
    "id": "2",
    "text": "This was terrible.",
    "polarity": -0.6,
    "classification": "negative"
  }
]
```

Testing

Run the automated tests with:

```bash
pytest
```
