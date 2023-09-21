import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.exceptions import NotFittedError

app = Flask(__name__)

# Load the trained Multinomial NB model
model = joblib.load('multinomial_nb_model.joblib')

# Load the CountVectorizer used during training
# Note: You need to have access to the vectorizer used during training
# to transform new email data in the same way.
vectorizer = joblib.load('count_vectorizer.joblib')

# Check if the vectorizer is fitted
try:
    # Test if the vectorizer is fitted
    vectorizer.transform(['test'])
except NotFittedError:
    # If not fitted, fit the vectorizer
    # You should replace 'training_data' with the data the vectorizer was originally trained on
    vectorizer.fit_transform(['training_data'])

@app.route('/', methods=['GET'])
def default_route():
    return "This is the API endpoint for email classification. Use /classify_email to classify an email."

@app.route('/classify_email', methods=['POST'])
def classify_email():
    data = request.get_json()
    email_content = data['email_content']
    
    # Preprocess the email content and transform using the CountVectorizer
    email_count = vectorizer.transform([email_content])
    
    # Predict using the model
    prediction = model.predict(email_count)
    
    # Assume 1 indicates spam and 0 indicates ham
    result = 'spam' if prediction[0] == 1 else 'ham'
    
    return jsonify({'prediction': result})

if __name__ == '__main__':
    # Heroku dynamically sets the port
    port = int(os.environ.get('PORT', 5000))
    # Start the server
    app.run(host='0.0.0.0', port=port)
