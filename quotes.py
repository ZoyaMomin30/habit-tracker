from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://zenquotes.io/api/random")
    quote = response.json()[0]
    return render_template('index.html', quote_text=quote["q"], author=quote["a"])

if __name__ == '__main__':
    app.run(debug=True)
