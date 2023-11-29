#!//Users/himat.varsani/.pyenv/shims/python

import json


from flask import Flask, request, Response

app = Flask(__name__)

#Database
#Dictionaires

movies_db = {
    "1": {"Name" : "Stargate", "release date" : "1994"},
    "2": {"Name" : "Sunshine", "release date" : "2007"},
    "3": {"Name" : "The Holiday", "release date" : "2006"},
}

@app.route("/")
def hello():
    return "Hello World"

@app.route("/hello")
def world():
    return "<h1>Hello World!!</h1>"

@app.route("/movies")
def movies():
    html_response = "<ul>"
    for m in movies_db:
        html_response += "<li>" + "<a href='/movies/" + m + "'>" + movies_db[m]["Name"] + "</a>" + "</li>"
        html_response += "</ul>"
    return html_response
        #return json.dumps(movie_db)

#READ - GET
@app.route("/movies/<movies_id>")
def get_movie(movies_id):
    return json.dumps([movies_db[movies_id]])

#CREATE - POST
@app.route("/movies/add", methods=['POST'])
def add_movie():
    req_data = request.get_json()
    movies = req_data['movies']
    
    new_movie = {"4": movies}
    movies_db.update(new_movie)
    return "Movies was added successfully"
    

if __name__ == "__main__":
    app.run(host='127.0.0.1')
    

### New movie format
# {"movies" : {"name" : "The Matrix", "release_date" : "1999"}}

## Terminal : add - curl -X POST http://127.0.0.1:5000/movies/add -d '{"movies" : {"name" : "The Matrix", "release_date" : "1999"}}' -H 'Content-Type: application/json'
    
#CRUD

#Update - put
#Delete - Get