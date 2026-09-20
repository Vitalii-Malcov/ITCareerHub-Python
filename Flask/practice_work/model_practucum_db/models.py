
from pathlib import Path

from  sqlalchemy import select
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker, Session
from sqlalchemy import create_engine


Base_DIR = Path(__file__).parent
DB_PATH = Base_DIR / "practicum3.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int]

    addresses: Mapped[list["Address"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.name!r}, age={self.age})>"


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"<Address(id={self.id}, description={self.description!r}, user_id={self.user_id})>"


if __name__ == "__main__":
    init_db()

    session: Session = SessionLocal()
    try:
        # sql_query = select(User).where(User.name=='Alice')
        # users = session.scalars(sql_query).all()
        #
        # sql_query_2 = select(User).filter(User.age > 20)
        # users_2 = session.scalars(sql_query_2).all()
        #
        # sql_query_3 = select(User).where(User.name == 'Bob')
        # users_3 = session.scalar(sql_query_3)
        # users_3.age = 25
        #
        # sql_query_4 = select(User).where(User.age < 30)
        # users_4 = session.scalars(sql_query_4).all()

        # new_user = User(name='Charlie', age=28)
        # session.add(new_user)

        new_user = 'Charlie'
        user_to_delite = session.query(User).filter(User.name == new_user).first()
        if user_to_delite:
            session.delete(user_to_delite)
            session.commit()
            print(f'Пользователь {new_user} успешно удален.')
        else:
            print(f'Пользователь {new_user} не найден в базе данных.')



        # print('\nПервые 5 пользователей из базы:')
        # for user in users:
        #     print(user)
        #
        # print('\nПользователи старше 20 лет:')
        # for user in users_2:
        #     print(user)
        #
        # print(f'\nОбновление возраста пользователя Bob: {users_3.age}')
        #
        # print('\nПользователи младше 30 лет:')
        # for user in users_4:
        #     print(user)
        #
        # print(f'\nДобавлен новый пользователь: {new_user}')

        # print(f'\nУдален пользователь: {user_to_delite}')

    finally:
        session.close()
