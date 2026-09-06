from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    """Возвращает простое приветствие при обращении к главной странице."""
    return "Hello, World!"

@app.route("/user/<name>")
def greet_user(name):
    """Возвращает персонализированное приветствие с именем из URL."""
    return f"Привет, {name}!"

@app.route("/double/<int:number>")
def double_number(number):
    """Возвращает удвоенное значение числа из URL."""
    return f"Удвоенное значение {number} равно {number * 2}."

@app.route("/square/<float:number>")
def square_number(number):
    """Возвращает квадрат числа из URL."""
    return f"Квадрат числа {number} равен {number ** 2}."

@app.route("/reverse/<path:text>")
def reverse_text(text):
    """Возвращает перевернутый текст из URL."""
    return f"Перевернутый текст: {text[::-1]}"

if __name__ == "__main__":
    app.run(debug=True)
