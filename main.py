import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load the trained Multinomial NB model
model = joblib.load('multinomial_nb_model.joblib')

# Load the CountVectorizer used during training
# Note: You need to have access to the vectorizer used during training
# to transform new email data in the same way.
vectorizer = joblib.load('count_vectorizer.joblib')

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
