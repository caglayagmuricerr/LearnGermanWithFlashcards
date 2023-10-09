import requests

def translate(word, language): # Translates the word user entered to German using Google Translate API
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2" # API URL

    payload = { 
        "q": word,          # Text to translate
        "target": "de",     # Target language (German)
        "source": language  # Source language (any language)
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip", 
        "X-RapidAPI-Key": "11d195c660msh7c0095b6066a328p1184c6jsn18c275d7bb63", 
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com" 
    }

    response = requests.post(url, data=payload, headers=headers) # Send post request to API to get a response

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Access the translated text from the JSON response
        translated_text = response.json().get('data', {}).get('translations', [{}])[0].get('translatedText', 'Translation not available') 
        return translated_text

    else:
        # Print an error message if the request was not successful
        print("Error:", response.status_code, response.text)