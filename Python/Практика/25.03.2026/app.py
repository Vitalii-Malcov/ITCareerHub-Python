from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    with open("index.html", "r", encoding="utf-8") as file:
        return file.read()

@app.route('/about')
def about():
    with open("about.html", "r", encoding="utf-8") as file:
        return file.read()

@app.route("/dashboard")
def dashboard():
    email = request.args.get("email")
    with open("dashboard.html", "r", encoding="utf-8") as file:
        html = file.read()
    return html.replace("email", email)

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
