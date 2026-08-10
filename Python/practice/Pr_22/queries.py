books_query = """
   CREATE TABLE IF NOT EXISTS books (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(200),
       author VARCHAR(100),
       price DECIMAL(10, 2),
       stock INT CHECK (stock >= 0)
   )
"""

users_query = """
   CREATE TABLE IF NOT EXISTS users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(100),
       password VARCHAR(100),
       balance DECIMAL(10, 2) CHECK (balance >= 0)
   )
"""

text_main_menu = """
Please input 1, 2, 3 or 0:
    1: Load books from file,
    2: Register new user,
    3: Login as user,
    0: Exit.\n"""

text_user_menu = """
\n--- User Menu (ID {user_id}) ---")
Please choose action:
    1. View available books
    2. Search books by title
    3. Purchase a book
    4. View most frequent search queries
    0. Logout
"""

purchases_query = """
    CREATE TABLE IF NOT EXISTS purchases (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        book_id INT,
        quantity INT,
        purchase_date DATE,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
    )
"""