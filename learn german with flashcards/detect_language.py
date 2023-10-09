import requests

def detectlanguage(word): # Detects the language of the word user entered using Google Translate API
	url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

	payload = { "q": word }
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"Accept-Encoding": "application/gzip",
		"X-RapidAPI-Key": "11d195c660msh7c0095b6066a328p1184c6jsn18c275d7bb63",
		"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
	}

	response = requests.post(url, data=payload, headers=headers)
	detected_language = response.json().get('data', {}).get('detections', [[]])[0][0].get('language', 'Language not detected')
	
	return detected_language
