import pymongo
from flask import Flask,request,jsonify
from flask_cors import CORS
from bson import ObjectId  # Import ObjectId to handle MongoDB _id fields



app=Flask(__name__)
CORS(app)  # Enable CORS for all routes

class API:
    def __init__(self):
        self.db_url = "mongodb+srv://mohana:mohana@cluster0.cqguvdh.mongodb.net/mentorassign?retryWrites=true&w=majority&appName=Cluster0"
        self.client = pymongo.MongoClient(self.db_url)
        # Access the database and collection
        self.db = self.client['school']
        self.collection = self.db['students']
    
    def create_data(self, data_list):
        try:
            data = self.collection.insert_many(data_list)
            return {"message": "Data inserted successfully", "inserted_ids": [str(id) for id in data.inserted_ids]}
        except Exception as e:
            return {"error": str(e)}

    def get_data(self, query={}):
        try:
            data = self.collection.find(query)
            # Convert documents to a list of dictionaries and format ObjectId to string
            result = []
            for doc in data:
                doc['_id'] = str(doc['_id'])
                result.append(doc)
            return result
        except Exception as e:
            return {"error": str(e)}

    def update_data(self, query, new_value):
        try:
            result = self.collection.update_one(query, {"$set": new_value})
            if result.modified_count > 0:
                return {"message": "Update successful", "modified_count": result.modified_count}
            else:
                return {"message": "No document found to update", "modified_count": result.modified_count}
        except Exception as e:
            return {"error": str(e)}

    def delete_data(self, query):
        try:
            result = self.collection.delete_one(query)
            if result.deleted_count > 0:
                return {"message": "Deleted successfully", "deleted_count": result.deleted_count}
            else:
                return {"message": "No matching document found to delete", "deleted_count": result.deleted_count}
        except Exception as e:
            return {"error": str(e)}


#crate object
# a1=api()
#object calling create
# new_student = [{"name": "John Doe", "age": 25, "course": "Math"},
# {"name": "hello", "age": 28, "course": "science"}
# ]

# a1.createdata(new_student)
# a1.getdata({"name":"John Deo"})

#update the value

# a1.update({"name":"hello"},{"name":"mohana"})

# a1.delete({"course": "science"})

# create an isinstance of api
api_instance = API()

@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    response = api_instance.create_data(data)
    return jsonify(response), 201 if "inserted_ids" in response else 400

@app.route('/getstudents', methods=['GET'])
def get_student():
    query = request.args.to_dict()
    data = api_instance.get_data(query)
    return jsonify(data), 200

@app.route('/updatestudents', methods=['PUT'])
def update_student():
    data = request.json
    query = data.get("query", {})
    new_value = data.get("new_value", {})

    # Convert _id to ObjectId if it exists in the query
    if '_id' in query:
        try:
            query['_id'] = ObjectId(query['_id'])
        except Exception as e:
            return jsonify({"error": "Invalid ObjectId format", "details": str(e)}), 400

    # Call update_data instead of update
    response = api_instance.update_data(query, new_value)

    if response.get("modified_count", 0) > 0:
        return jsonify({"message": "Student updated successfully", "modified_count": response["modified_count"]}), 200
    else:
        return jsonify({"message": "No document found to update", "modified_count": response["modified_count"]}), 400


@app.route('/delstudents', methods=['DELETE'])
def delete_student():
    query = request.json
    # Convert the _id to ObjectId if it exists
    if '_id' in query:
        query['_id'] = ObjectId(query['_id'])
    response = api_instance.delete_data(query)
    return jsonify(response), 200 if "deleted_count" in response else 400

if __name__ == "__main__":
    app.run(debug=True)





    # FRONT END  REPOLINK

    # https://github.com/MohanapriyaThirumurugan/STUDENTWEBPAGE