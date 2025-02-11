from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your_openweather_api_key"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()
        if response["cod"] == 200:
            weather = {
                "city": city,
                "temperature": response["main"]["temp"],
                "description": response["weather"][0]["description"]
            }
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
