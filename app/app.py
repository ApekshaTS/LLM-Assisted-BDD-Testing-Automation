from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["email"] == "test@example.com" and request.form["password"] == "Password123":
            session["user"] = True
            return redirect("/dashboard")
        return "Invalid credentials", 401
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not session.get("user"):
        return redirect("/login")
    return render_template("dashboard.html")  # UPDATED

@app.route("/")
def home():
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
