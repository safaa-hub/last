from sqlalchemy import Column, Integer, String, Date
from ..common_file import Base, engine


class User(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(first_name='%s', last_name='%s', birth_date='%s' , gender='%s')>" % (
            self.first_name, self.last_name, self.birth_date, self.gender)


Base.metadata.create_all(engine)
