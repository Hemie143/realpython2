import json
import requests
import sqlite3


TOKEN = "dd1004b9-e5bf-4c09-bb65-7b80b50b41c6"
url = requests.get("https://www.myapifilms.com/imdb/inTheaters?token={0}&format=json&language=en-us".format(TOKEN))

binary = url.content
output = json.loads(str(binary, "utf-8"))
movies = output['data']['inTheaters']

with sqlite3.connect("movies.db") as connection:
    c = connection.cursor()
    for movie in movies:
        all_movies = movie['movies']
        for meta in all_movies:
            if meta['title'] and 'votes' in meta:
                c.execute("INSERT INTO new_movies VALUES(?, ?, ?, ?, ?, ?)", (meta['title'], meta['year'],
                                                                              meta['votes'], meta['releaseDate'],
                                                                              meta['metascore'], meta['rating']))
                c.execute("SELECT * from new_movies ORDER BY title ASC")
                rows = c.fetchall()
                for r in rows:
                    print(r[0], r[1], r[2], r[3], r[4], r[5])