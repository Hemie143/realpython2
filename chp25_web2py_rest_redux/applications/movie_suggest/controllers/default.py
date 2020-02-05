import requests
import json

def index():
    return dict()

def grab_movies():
    session.m = []
    TOKEN = "dd1004b9-e5bf-4c09-bb65-7b80b50b41c6"
    url = requests.get("https://www.myapifilms.com/imdb/inTheaters?token={0}&format=json&language=en-us".format(TOKEN))
    binary = url.content
    output = json.loads(binary)
    movies = output['data']['inTheaters']
    for movie in movies:
        all_movies = movie['movies']
        for meta in all_movies:
            if meta['title']:
                session.m.append(pulse(meta['title']))
    session.m.sort()
    return TABLE(*[TR(v) for v in session.m]).xml()

def pulse(movie):
    text = movie.replace('_', ' ')
    url = 'http://text-processing.com/api/sentiment/'
    data = {'text': text}
    r = requests.post(url, data=data)
    binary = r.content
    output = json.loads(binary)
    label = output['label']
    pos = output['probability']['pos']
    neg = output['probability']['neg']
    neutral = output['probability']['neutral']
    return text, label, pos, neg, neutral
