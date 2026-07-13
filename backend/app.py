from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

@app.route("/")
def home():
    return "Welcome to the Multi-Tier Flask Application!"

@app.route("/db")
def db():
    cursor = db.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    return f"Database Connected Successfully! Time: {result[0]}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
