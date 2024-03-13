from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", data=data)

def access_data():
	url = "https://api.spacexdata.com/v4/launches"
	response = requests.get(url)
	if response.status_code == 200:
		return response.json()
	else:
		return []

def categorize_data(data):
	successful = list(filter(lambda x : x["success"] and not x["upcoming"], data))
	failed = list(filter(lambda x : not x["success"] and not x["upcoming"], data))
	upcoming = list(filter(lambda x : x["upcoming"], data))

	return {
		"successful" : successful,
		"failed" : failed,
		"upcoming" : upcoming
	}

data = categorize_data(access_data())

if __name__ == "__main__":
	app.run(debug=True)