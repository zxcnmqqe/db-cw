from flask import Flask
from flask import request, jsonify
from model import Users

app = Flask(__name__)

users = Users()

@app.route("/users", methods=["GET"])
def get_all_users():
    result = users.get_all_users()
    return jsonify(result), 200

@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    result = users.get_user(id)
    return jsonify(result), 200

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    result = users.add_user(data)
    return jsonify(result), 200

@app.route("/users", methods=["PATCH"])
def update_user():
    data = request.get_json()
    result = users.update_user(data)
    return jsonify(result), 200

@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = users.delete_user(id)
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)