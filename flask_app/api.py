# from flask import Flask, jsonify,request

# app = Flask(__name__)
# app.json.sort_keys = False
# student = [
#     {'id': 1, 'name': 'sultan', 'country': 'yemen', 'city': 'sanna'},
#     {'id': 2, 'name': 'sammar', 'country': 'US', 'city': 'san francisco'},
#     {'id': 3, 'name': 'sonak', 'country': 'japan', 'city': 'Tokyo'}
# ]

# # ROUTE 1: all students
# @app.route('/api/v1.0/students', methods=['GET'])
# def get_api():
#     ordered = sorted(student, key=lambda s: s['name'])
#     return jsonify(ordered)
#     # ROUTE 2: ONE student
# @app.route('/api/v1.0/students/<int:id>', methods=['GET'])   # <int:id> = the number in the address
# def get_student(id):                      # BLANK 1: write the same name as in <int:id>
#     for s in student:
#         if s['id'] == id:                  # is this the student with that number?
#             return jsonify(s)
#     return jsonify({'error':'Not found'}), 404    # BLANK 2: comma or colon?


# @app.route('/api/v1.0/students',methods=['POST'])

# def add_students():
#     data = request.get_json()
#     new={
#         'id': len(student)+1,
#         'name': data['name'],
#         'country': data['country'],
#         'city':data['city']
#     }
#     student.append(new)
#     return jsonify(new),201

# @app.route('/api/v1.0/students/<int:id>',methods=['DELETE'])

# def delet(id):
#     for s in student:
#         if s['id']==id:
#             student.remove(s)
#             return jsonify({'result': 'DELET','id':id})
#     return jsonify({'erorr':'Not found'}),404

# @app.route('/api/v1.0/students/<int:id>',methods=['PUT'])
# def updeate(id):
#     data = request.get_json()
#     for s in student:
#         if s ['id']==id:
#             s['name']=data['name']
#             s['country']=data['country']
#             s['city']=data['city']
#             return jsonify(s)
#     return jsonify({'error':'Not found'}),400


# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask,jsonify,request

# app = Flask(__name__)

# app.json.sort_key =False

# stedents = [
#    {'id': 1, 'name': 'sultan', 'country': 'yemen', 'city': 'sanna'},
#    {'id': 2, 'name': 'sammar', 'country': 'US', 'city': 'san francisco'},
#     {'id': 3, 'name': 'sonak', 'country': 'japan', 'city': 'Tokyo'}]

# @app.route('/aip/v.1/stedent',methods=['GET'])

# def get_stedent():
#     order =sorted(stedents,key=lambda s:s['name'])
#     return jsonify(order)

# @app.route('/aip/v.1/stedent/<int:id>',methods=['GET'])

# def found(id):
#     for s in stedents:
#         if s['id']==id:
#             return jsonify(s)
#     return jsonify({'erorr': 'Noot Found'}),404


# @app.route('/aip/v.1/stedent',methods=['POST'])

# def Post():
#     data = request.get_json()
#     new={
#         "id":len(stedents)+1,
#         "name":data["name"],
#         "country":data["country"],
#         "city":data["city"]
#     }
#     stedents.append(new)
#     return jsonify(new)


# @app.route('/aip/v.1/stedent/<int:id>',methods=["DELETE"])

# def DELETE(id):

#     for s in stedents:
#         if s["id"]==id:
#             stedents.remove(s)
#             return jsonify({'result':'succsc','id':id})
#     return jsonify({"erorr":"Not Found"})


# @app.route('/aip/v.1/stedent/<int:id>',methods=['PUT'])

# def Put(id):

#     data = request.get_json()
#     for s in stedents:
#         if s['id']==id:
#             s['name']=data['name']
#             s['country']=data['country']
#             s['city']=data['city']
#             return jsonify(s)
#     return jsonify({'erorr':'Not Found'}),404


# ====================================================================

# the same above but with PYMONG


from flask import Flask,request,jsonify

from pymongo import MongoClient

mongo_url = 'localhost:27017'


client = MongoClient(mongo_url)
# print(client.list_database_names())
# db  = client.un_studint

# st = db.studeants


# st.insert_many(data)

# print(st.count_documents({}))


# app = Flask(__name__)

# @app.route('/api/v1.0/students',methods=['GET'])


# @app.route('/api/v1.0/students/<int:id>',methods=['GET'])

# def GET_STUDENT(id):

#     s = st.find_one({'id':id},{'_id':0})

#     if s:
#         return jsonify(s)
#     return jsonify({'eroor':'Not find'}),404


# @app.route('/api/v1.0/students',methods=['POST'])

# def post():

#     data= request.get_json()
#     new={
#         'id':st.count_documents({})+1,
#         'name':data['name'],
#         'country':data['country'],
#         'city':data['city']
#     }
#     st.insert_one(new)
#     new.pop('_id', None)
#     return jsonify(new),201


# @app.route('/api/v1.0/students/<int:id>',methods=['DELETE'])

# def DEL(id):

#     result = st.delete_one({'id':id})

#     if result.deleted_count == 0:
#      return jsonify({'error': 'Not found'}), 404

#     return jsonify({'result': 'Deleted', 'id': id})


# @app.route('/api/v1.0/students/<int:id>',methods=['PUT'])

# def put(id):

#     data = request.get_json()

#     new={
#         'name':data['name'],
#         'country':data['country'],
#         'city':data['city']
#     }

#     rusult = st.update_one({'id':id},{'$set':new})

#     if rusult.matched_count==0:
#         return jsonify({'reorr':'Not Found'})
#     new['id']=id
#     return jsonify(new)

db = client.fake_stedent

st = db.cslss_student


data = [
       {'id': 1, 'name': 'sultan', 'country': 'yemen', 'city': 'sanna'},
    {'id': 2, 'name': 'sammar', 'country': 'US', 'city': 'san francisco'},
    {'id': 3, 'name': 'sonak', 'country': 'japan', 'city': 'Tokyo'}
]


# st.insert_many(data)

app=Flask(__name__)

@app.route('/api',methods=['GET'])

def Get_student():
    stedents = list(st.find({}, {'_id': 0}))
    return jsonify(stedents)

@app.route('/api/<int:id>',methods=['GET'])

def search(id):
    r= st.find_one({'id':id},{'_id':0})
    if r:
        return jsonify(r)
    return jsonify({'error':'Not Found'}),404


@app.route('/api/<int:id>',methods=['POST'])

def post(id):

    data = request.get_json()
    new = {
        'id':st.count_documents()+1,
        'name': data['name'],
        'conutry':data['country'],
        'city':data['city']
    }
    st.insert_one(new)
    new.pop('_id',None)
    return jsonify(new),201

@app.route('/api/<int:id>',methods=['DELETE'])

def DEL(id):

    r = st.delete_one({'id':id})

    if r.deleted_count == 0:
        return jsonify({'eroor':'Not Found'}),404
    return (r)

@app.route('/api/<int:id>',methods=['PUT'])

def put(id):

    data = request.get_json()
    fix = {
        'name': data['name'],
        'conutry':data['country'],
        'city':data['city']
    }

    r =st.update_one({'id':id},{'$set':fix})

    if r.matched_count==0:
        return jsonify({'erorr':'Not Found'})
    fix['id']=id
    return jsonify(fix)


if __name__=='__main__':
    app.run(debug=True)
