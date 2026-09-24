from flask import Flask, render_template, request, redirect, jsonify
import pyodbc

app = Flask(__name__)

def get_connection():
    print("=== CONNECT FUNCTION CALLED ===", flush=True)

    print("=== ABOUT TO CONNECT TO SQL SERVER ===", flush=True)

    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=host.docker.internal,1433;"
        "DATABASE=DevOpsAI;"
        "UID=devops_app;"
        "PWD=Nitha@12345;"
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

