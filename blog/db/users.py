from sqlalchemy.orm import Session
from blog.models.domain.users import User

# db.execute()
# curd
# db.transaction
# db.add(User)
# db.commit()
# db.add()
# db.add_all()
# db.transaction =
# query.filter(or_(User.name == 'ed', User.name == 'wendy'))
# session.query(User).from_statement(
#     ...
# session.query(User).from_statement(
#     ...
# text("SELECT * FROM users where name=:name")). \
#     ...params(name='ed').all()
from blog.models.mapper.users_mapper import LoginAccount

GET_BY_USER_NAME = """
select user_name,password from user where user_name = :user_name
"""


class UserRepository(object):
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_id(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).first()

    def get_user_by_name(self, user_name: str):
        return self.session.execute(GET_BY_USER_NAME, {"user_name": user_name}, LoginAccount).first()
