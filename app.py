from flask import Flask, render_template, request, redirect, jsonify
import pyodbc
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

def get_connection():
    print("=== CONNECT FUNCTION CALLED ===", flush=True)

    print("DB_SERVER =", os.getenv("DB_SERVER"), flush=True)
    print("DB_NAME =", os.getenv("DB_NAME"), flush=True)
    print("DB_USER =", os.getenv("DB_USER"), flush=True)
    print("DB_PASSWORD SET =", bool(os.getenv("DB_PASSWORD")), flush=True)

    print("=== ABOUT TO CONNECT TO SQL SERVER ===", flush=True)

    connection = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        "TrustServerCertificate=yes;"
    )

    return connection


@app.route("/")
def home():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT Id, Name, Email FROM dbo.Users")
    users = cursor.fetchall()

    connection.close()

    return render_template("index.html", users=users)


@app.route("/api/test", methods=["POST"])
def test_post():
    return "POST is working"


@app.route("/add-user", methods=["POST"])
def add_user():
    name = request.form["name"]
    email = request.form["email"]

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO dbo.Users (Name, Email) VALUES (?, ?)",
        name,
        email
    )

    connection.commit()
    connection.close()

    return redirect("/")
@app.route("/api/users", methods=["GET"])
def get_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT Id, Name, Email FROM dbo.Users")
    rows = cursor.fetchall()

    connection.close()

    users = []

    for row in rows:
        users.append({
            "id": row[0],
            "name": row[1],
            "email": row[2]
        })

    return jsonify(users)

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()

    name = data["name"]
    email = data["email"]

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO dbo.Users (Name, Email) VALUES (?, ?)",
        name,
        email
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "User created successfully"
    }), 201

print(app.url_map)
if __name__ == "__main__":

    print("MY APP.PY IS RUNNING")
    print("STARTING ON PORT 5001")
    app.run(debug=True,host="0.0.0.0", port=5001)

