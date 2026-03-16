from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    return conn

@app.route("/")
def home():
    return redirect("/login")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        conn.execute("INSERT INTO users (username,password) VALUES (?,?)",(username,password))
        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password)).fetchone()
        conn.close()

        if user:
            return "Login Successful"
        else:
            return "Invalid Credentials"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
