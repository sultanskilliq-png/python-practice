# from pymongo import MongoClient
# # uri = "mongodb+srv://<username>:<password>@<cluster-url>/"
# # client = MongoClient(uri)
# # try:
# #     client.admin.command("ping")
# #     print("Connected successfully")
# #     client.close()

# # except Exception as e:
# #     raise Exception(
# #         "The following error occurred: ", e)

# # let's import the flask
# from flask import Flask, render_template
# import os # importing operating system module
# # MONGODB_URI = 'mongodb+srv://<username>:<password>@<cluster-url>/'
# # client = pymongo.MongoClient(MONGODB_URI)
# # print(client.list_database_names())

# # app = Flask(__name__)
# # if __name__ == '__main__':
# #     # for deployment we use the environ
# #     # to make it work for both production and development
# #     port = int(os.environ.get("PORT", 5000))
# #     app.run(debug=True, host='0.0.0.0', port=port)


# from flask import Flask, jsonify
# from flask import jsonify
# from pymongo import MongoClient

# # app = Flask(__name__)
# # mongo_uri = "mongodb+srv://<username>:<password>@<cluster-url>/"
# # client = MongoClient(mongo_uri)

# # @app.route("/ping-db")
# # def ping_db():
# #     try:
# #         client.admin.command("ping")
# #         return jsonify({"ok": True, "message": "MongoDB is reachable"})
# #     except Exception as e:
# #         return jsonify({"ok": False, "error": str(e)}), 500

# # @app.route("/")
# # def index():
# #     return "Flask + MongoDB is running. Try GET /ping-db"

# # if __name__ == "__main__":
# #     port = int(os.environ.get("PORT", 5000))
# #     app.run(debug=True, host='0.0.0.0', port=port)


# # let's import the flask
# from flask import Flask, render_template
# import os # importing operating system module
# from bson.objectid import ObjectId
# # import pymongo
# MONGODB_URI = 'mongodb+srv://<username>:<password>@<cluster-url>/'
# client = MongoClient(MONGODB_URI)
# print(client.list_database_names())

# db = client.therty_Days_of_Python

# students=(
#      {'name':'David','country':'UK','city':'London','age':34},
#         {'name':'John','country':'Sweden','city':'Stockholm','age':28},
#         {'name':'Sami','country':'Finland','city':'Helsinki'},
#     {"name" : "sultan",
#     "contry" : "yemen",
#     "city": "sanaa",
#     "age":24
# })
# for student in students:
#     db.students.insert_one(student)

# search_id = db.students.find_one({'_id':ObjectId('6ae643a37ec5f2ea1521592d')})
# # print(search_id)
# print(client.list_database_names())
# sttudint= db.students.find()

# for sttudintt in sttudint:
#     print(sttudintt)

# sttudint= db.students.find({},{'_id':0}).limit(3)

# for i in sttudint:

#   print(i)
# qury = {
#     'city': "Stockholm"
# }
# studint = db.students.find(qury)
# db.students.delete_many({})

# for sttudintt in studint:
#     print(sttudintt)
# print(client.list_database_names())
# print(db.name)
# print(db.students.count_documents({}))

# app = Flask(__name__)

# @app.route('/')
#     # for deployment we use the
# def home():
#     return 'evry think is ok'

# # if __name__ == '__main__':environ
#     # to make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)


# let's import the flask


# from pymongo import MongoClient
# from flask import Flask,render_template

# Mongo_url = 'mongodb+srv://<username>:<password>@<cluster-url>/'
# clint = MongoClient(Mongo_url)

# db = clint.unvercity
# # db.Class_Room.insert_one({'class_1':'Ahmed','age':25,"contry":'Yemen',"city":'sanna'})
# # malty_data = ({'class_1':'Ahmed','age':25,"contry":'Yemen',"city":'sanna'},{'class_1':'soni','age':29,"contry":'holinda',"city":'chana'},{'class_1':'Saied','age':30,"contry":'sadi',"city":'reaid'})

# # for stedent in malty_data:
# #     db.Class_Room.insert_one(stedent)
# from bson.objectid import ObjectId
# search = db.Class_Room.find_one({'_id': ObjectId('6ae6896f3b0db10f2eca1884')})
# print(search)
# search = [
#     {'_id': ObjectId('6ae6896f3b0db10f2eca1884')},
#     {'_id': ObjectId('6ae689713b0db10f2eca1885')}
# ]

# search = ()

# searchh = db.Class_Room.find({},{'_id':0,'contry':1,'city':1})
# searchh = db.Class_Room.find({},{'_id':0}).limit(2)

# qury={'contry':'Yemen'}
# qury={'age':{'$lte':25}}
# query = {'class_1': {'$in': ['Ahmed']}}

# searchh = db.Class_Room.find({},{'_id':0}).sort('age',-1)

# for ser in searchh:
#     print(ser)


# # for ser in search:
# #     result = db.Class_Room.find_one(ser)
# #     print(result)

# from flask import Flask, jsonify
# from pymongo import MongoClient
# import os

# app = Flask(__name__)
# # MONGODB_URI = 'mongodb+srv://<username>:<password>@<cluster-url>/'


# MONGODB_URI = os.environ.get("MONGODB_URI")
# client = MongoClient(MONGODB_URI)
# db = client["streaming_platform"]
# # db.movies.insert_one({'name': 'sultan','age':20,'skills':'backend'})
# @app.route("/movies")
# def get_movies():
#     movies = list(db.movies.find({}, {"_id": 0}))
#     return jsonify(movies)

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)
