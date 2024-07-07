import os
from flask import Flask, jsonify, request
import uuid
from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")
app = Flask(__name__)


@app.route('/', methods=['POST'])
def generate_tags():
    if request.method == 'POST':
        text = request.form['text']
        pred = sentiment_analysis(text)
        return jsonify(list(pred))

if __name__ == '__main__':
    app.run()