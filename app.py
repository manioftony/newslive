from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
import requests


@app.route('/', methods=['POST', 'GET'])
def index():
#########
            # https://newsapi.org/sources
            # Create api above link
########
    apikey = 'Enter api key here'

    if request.method == 'GET':
        obj = requests.get(
            'https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=%s' % (apikey))
        obj = obj.json()
        obj_news = 'Times of India News'
        obj_data = obj.get('articles')
    if request.method == 'POST':
        obj = {"Bbc News": requests.get('https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=%s' % (apikey)),
               "Hindu News": requests.get('https://newsapi.org/v1/articles?source=the-hindu&sortBy=top&apiKey=%s' % (apikey)),
               "Sports News": requests.get('https://newsapi.org/v1/articles?source=sky-sports-news&sortBy=top&apiKey=%s' % (apikey)),
               "Times of India News": requests.get('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=%s' % (apikey)), }

        obj = obj.get(request.form.get('news'))
        obj_news = request.form.get('news')
        obj = obj.json()
        obj_data = obj.get('articles')
        # return jsonify({"name":"mani"})
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
