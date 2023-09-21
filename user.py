import requests
import json

# Specify the URL of your Heroku app's classify_email endpoint
url = "https://spamham1-7fde22e64f9c.herokuapp.com/classify_email"

# Sample email content to classify
email_content = "This is a spam email."

# Create a dictionary with the email content
data = {
    "email_content": email_content
}

# Convert the data to JSON
json_data = json.dumps(data)

# Set the headers to specify the content type as JSON
headers = {
    "Content-Type": "application/json"
}

# Make a POST request to the classify_email endpoint
response = requests.post(url, data=json_data, headers=headers)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the response JSON
    result = response.json()
    prediction = result["prediction"]
    print("Prediction:", prediction)
else:
    print("Error:", response.status_code)
