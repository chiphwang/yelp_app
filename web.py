from flask import Flask, render_template, request
import weather1
import os
import yelp_api


app = Flask(__name__)

@app.route("/")
def index():
    location = request.values.get('location')
    terms = request.values.get('terms')
    lang = "en"
    businesses = None
    if terms:
        businesses=yelp_api.get_business(terms,lang,location)
    return render_template('index.html',businesses=businesses)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0",port=port)
