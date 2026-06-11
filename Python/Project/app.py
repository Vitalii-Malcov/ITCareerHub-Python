from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard")
def dashboard():
    email = request.args.get("email")
    return render_template("dashboard.html", email=email)

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return "Заполни все поля!"

    if email == "admin@mail.com" and password == "1234":
        return redirect(f"/dashboard?email={email}")

    return "Неверный логин или пароль"

if __name__ == "__main__":
    app.run(debug=True)
