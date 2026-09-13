from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os, logging

from Python.homework.lists.task_4_1 import result
Base = declarative_base()
logging.basicConfig(level=logging.INFO)
engine = create_engine('sqlite:///practicework.db', echo=True)

with engine.connect() as connection:
    connection.execute(text('CREATE TABLE user (id INTEGER PRIMARY KEY, username TEXT, password TEXT, email TEXT)'))
    connection.execute(text("INSERT INTO user (username, password, email) VALUES ('john_doe', 'securePassword123', 'john.doe@example.com')"))
    result = connection.execute(text("SELECT * FROM user"))
    for row in result:
        print(row)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()

users = session.query(User).all()
for user in users:
    print(user)
