#!//Users/himat.varsani/.pyenv/shims/python

import json
from flask_sqlalchemy import SQLAlchemy
from config import Config

from flask import Flask, request, Response

app = Flask(__name__, instance_relative_config=False)
app.config.from_object(Config)

db = SQLAlchemy

#Database
#Dictionaires

# movies_db = {
#     "1": {"Name" : "Stargate", "release date" : "1994"},
#     "2": {"Name" : "Sunshine", "release date" : "2007"},
#     "3": {"Name" : "The Holiday", "release date" : "2006"},
# }

class Movies(db.Model):
    id=db.column('id', db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=255))
    release_year = db.Column(db.Integer)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/hello")
def world():
    return "<h1>Hello World!!</h1>"

@app.route("/movies")
def movies():
    movies = Movies.query.all()
    #RETRIEVE ALL MOVIES FROM TABLE MOVIES
    html_response = "<ul>"
    for m in movies:
        html_response += "<li>" + "<a href='/movies/" + str(m.id) + "'>" + m.name + "</a>" + "</li>"
        html_response += "</ul>"
    return html_response
        #return json.dumps(movie_db)

#READ - GET
@app.route("/movies/<movies_id>")
def get_movie(movies_id):
    movie = Movies.query.get(movies_id)
    return "h1" + movie.name + "-" + str(movie.release_year) + "</h1>"

#CREATE - POST
@app.route("/movies/add", methods=['POST'])
def add_movie():
    req_data = request.get_json()
    movies = req_data['movies']
    
    new_movies = Movies(name=movies["name"], release_year=movies["release_year"])
    db.session.add(new_movies)
    db.session.commit()
    
    return "Movies was added successfully"
    

if __name__ == "__main__":
    app.run(host='127.0.0.1')
    

### New movie format
# {"movies" : {"name" : "The Matrix", "release_date" : "1999"}}

## Terminal : add - curl -X POST http://127.0.0.1:5000/movies/add -d '{"movies" : {"name" : "The Matrix", "release_date" : "1999"}}' -H 'Content-Type: application/json'
    
#CRUD

#Update - put
#Delete - Get