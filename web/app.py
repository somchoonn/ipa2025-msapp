from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from pymongo import MongoClient
from bson import ObjectId
app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")
mydb = client["router"]
mycol = mydb["myrouter"]

@app.route("/")
def main():
    return render_template("index.html", data=mycol.find())

@app.route("/add", methods=["POST"])
def add_comment():
    ip_address = request.form.get("ip")
    username = request.form.get("username")
    password = request.form.get("password")
    if ip_address and username and password:
        mycol.insert_one({ "ip_address": ip_address, "username": username, "password": password })
    return redirect(url_for("main"))

@app.route("/delete", methods=["POST"])
def delete_comment():
    try:
        idx = ObjectId(request.form.get("idx"))
        if idx:
            mycol.delete_one({'_id': idx})
    except Exception:
        pass
    return redirect(url_for("main"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)