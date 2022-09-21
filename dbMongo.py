from pymongo import MongoClient
import datetime



def insert_user(username, password):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['users']

    user = {
        "username": str(username),
        "password": str(password)
    }

    users = db.users
    user_id = users.insert_one(user)

    return user_id

def find_user(username):

    client = MongoClient('mongodb://localhost:27017/')
    db = client['users']

    users = db.users
    result = users.find_one({
        "username": str(username)
    })

    return result

def find_link(username, filename):

    client = MongoClient('mongodb://localhost:27017/')
    db = client['links']

    links = db.links
    for result in links.find({
        "username": str(username),
        "filename": str(filename)
    }):

        if (result['downloadLink'] != None and result['downloadLink'] != str(None)):

            return result['downloadLink']


    return None



def insert_link(owner, filename, downloadLink):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['links']

    link = {
            "username": str(owner),
            "filename": str(filename),
            "downloadLink": str(downloadLink)}

    posts = db.links
    post_id = posts.insert_one(link).inserted_id


