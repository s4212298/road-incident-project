from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather")
def weather():
    return render_template("weather-analysis.html")

@app.route("/insights")
def insights():
    return render_template("deep-insights.html")

if __name__ == "__main__":
    app.run(debug=True)