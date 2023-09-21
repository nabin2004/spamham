import requests

def classify_email(email_content):
    # Endpoint URL for classifying email
    endpoint = "https://spamham1-7fde22e64f9c.herokuapp.com/classify_email"

    # Request payload
    payload = {
        "email_content": email_content
    }

    try:
        # Make a POST request to the endpoint
        response = requests.post(endpoint, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            return result['prediction']
        else:
            return "Error: Unable to classify email. Status code: " + str(response.status_code)
    except requests.exceptions.RequestException as e:
        return "Error: " + str(e)

# Example usage
email_content = "This is a spam email trying to sell you something."
prediction = classify_email(email_content)
print("The email is classified as:", prediction)
