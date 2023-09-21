import requests
import json

url = 'https://spamham1-7fde22e64f9c.herokuapp.com/classify_email'
data = {'email_content': 'This is a sample email to classify as spam or ham.'}

response = requests.post(url, json=data)

print('Response:', response.json())
