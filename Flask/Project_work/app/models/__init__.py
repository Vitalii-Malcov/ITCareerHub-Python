from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .categories import Category
from .questions import Question
from .answers import Answer
