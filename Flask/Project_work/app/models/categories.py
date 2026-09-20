from app.models import db

class Category(db.Model):
    __tablename__ = 'categories'

    id: db.Mapped[int] = db.mapped_column(db.Integer, primary_key=True)
    name: db.Mapped[str] = db.mapped_column(db.String(100), nullable=False)

    questions: db.Mapped[list["Question"]] = db.relationship(
        "Question", back_populates="category"
    )

    def __repr__(self):
        return f"<Category(id={self.id}: {self.name}')>"
